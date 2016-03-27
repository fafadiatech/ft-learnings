import csv
import types

DEBUG = False
SELL_DEBUG = False
OPTIMIZE = False

file_name = "brittania.csv"
#file_name = "output.csv"

def read_feed(file_name):
    """
    This method is used to read feed and return a list of tuples
    """
    result = []
    with open(file_name) as feed:
        for row in feed.readlines():
            row = row.strip()
            rec = row.split(",")
            if rec[0].strip() == "Symbol" or rec[0].strip() == "SYMBOL_NAME":
                continue
            
            if file_name == "output.csv":
                dt, ts, open_val, high, low, close = row.split(",")[1:7]
            else:
                dt, ts, open_val, high, low, close = "TODAY", row.split(",")[2], "", "", "", row.split(",")[5]
            result.append((dt, ts, float(close)))
    result.reverse()
    return result

def lots_to_buy(current_level, buying_levels):
    """
    Given current level and buying_levels figure out how many lots to buy
    """
    lots_to_buy = 0
    buying_levels_processed = []
    if len(buying_levels) == 0:
        return 0, []

    potential_level = buying_levels[-1]
    while potential_level > current_level:
        current_buying_level = buying_levels.pop()
        buying_levels_processed.append(current_buying_level)
        if len(buying_levels) == 0:
            break
        
        potential_level = buying_levels[-1]
        lots_to_buy += 1

    return lots_to_buy, buying_levels_processed

def dip_trader(feed, start_range, end_range, dip_points=50):
    """
    This method emulates DIP strategy trader
    """
    buying_levels = []
    selling_levels = []
    lot_counts = {}
    price_to_lots_mappings = {}

    #Generate initial buying level
    current_range = start_range
    buying_levels.append(start_range)
    while current_range > end_range:
        buying_levels.append(current_range - dip_points)
        current_range -= dip_points
    buying_levels.reverse()
    
    
    print "Buying Levels:"
    print "\n".join(map(str, buying_levels))
    print ""

    #Main logic for buying and selling
    current_tick = feed.pop()
    
    #Loop while we have more ticks
    profit = 0

    while len(feed) > 0:
        dt, ts, current_level = current_tick
        
        if DEBUG:
            print "Processing: %s %s %f, Length of Stack: %s" % (dt, ts, current_level, len(buying_levels))
            print "\t".join(map(str, buying_levels))

        #Check if we need to buy, if so how much?
        total_lots_to_buy, lots_processed = lots_to_buy(current_level, buying_levels)
        if total_lots_to_buy > 0:
            print "%s %s:Buy %d Lot(s) @ %.2f" % (dt, ts, total_lots_to_buy, current_level)
            selling_levels.append(current_level)
            lot_counts[str(current_level)] = total_lots_to_buy
            #Keep track of buying levels at which we bough certain item in a given point in time
            price_to_lots_mappings[str(current_level)] = lots_processed
            current_tick = feed.pop()
            continue

        #Check if we need to sell, if so how much?
        if len(selling_levels) > 0:
            selling_item = None
            for i in range(len(selling_levels)):
                if current_level >= (selling_levels[i] + dip_points):
                    selling_item = selling_levels[i]
                    break

            if not isinstance(selling_item, types.NoneType):
                print "%s %s:Sell %d Lots(s) @ %.2f Bought @ %.2f" % (dt, ts, lot_counts[str(selling_item)], current_level, selling_item)
                profit += (lot_counts[str(selling_item)] * (current_level - selling_item + dip_points))
                selling_levels.remove(selling_item)
                
                #After selling a certain item, mark its levels as empty
                for empty_buying_level in price_to_lots_mappings[str(selling_item)]:
                    buying_levels.append(empty_buying_level)
                
                buying_levels.sort()

                del lot_counts[str(selling_item)]
                del price_to_lots_mappings[str(selling_item)]

                if SELL_DEBUG:
                    print lot_counts

        current_tick = feed.pop()
    
    print ""
    print "Total Profit:%.2f" % profit
    
    return profit

if __name__ == "__main__":
    feed = read_feed(file_name)
    max_profit = 0

    if not OPTIMIZE:
        if file_name == "output.csv":
            dip_trader(feed, 8056.75, 7562.10)
        else:
            dip_trader(feed, 3920.9, 2720.9)
    else:
        max_profit = 0
        best_dip_points = 0
        for i in range(10, 100):
            feed = read_feed(file_name)
            current_profit = dip_trader(feed, 8056.75, 7562.10, i)
            
            if current_profit > max_profit:
                best_dip_points = i
                max_profit = current_profit
        
        print "Best setting for DIP Points:%d will achieve %.2f profit" % (best_dip_points, max_profit)
