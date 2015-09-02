from pyparsing import Word, alphas, oneOf

color = oneOf("red blue")
category = oneOf("shirts shoes")
color_category = color.setResultsName("color") + category.setResultsName("category")
category_color = category.setResultsName("category") + color.setResultsName("color")
query = color_category | category_color

print map(query.parseString, ["red shirts", "blue shoes", "shoes blue", "shirts red"])
