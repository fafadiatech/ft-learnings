import logging 

# There are few main concepts for logging 
# 1. Config: This is a dictionary that tell how logigng should behave
# 2. Stream Handler: They emit collected log entries to respective output E.g:
#		1. File
#		2. stdin/stdout
# 3. Formatter: Responsible for formatting the log to a format that we're in control of
# 4. Filters: Allow fine-grain control on which log should be passed through

# Logging is singleton, if you define it in your mail sript
# coressponding imported script can also use the logging module in same context

# Sample entries
logging.basicConfig(filename="simple_logger.log", level=logging.DEBUG)
logging.info("this should go to log file")
logging.warning("this is the warning log entry")
logging.debug("this is the debug log entry")