from pyparsing import Word, alphas, OneOrMore, Literal, oneOf

# define grammar
greet = Word(alphas) + "," + Word(alphas) + "!"

# input string
hello = "Hello, World!"

# parse input string
print hello, "->", greet.parseString(hello)


# define grammer for more complex case
word = Word(alphas+"'.")
salutation = OneOrMore(word)
comma = Literal(",")
greete = OneOrMore(word)
endpunc = oneOf("? !")
greeting = salutation + comma + greete + endpunc

test_cases = ["Hello, Sidharth!", "Hello, Sidharth how is your day?"]
print map(greeting.parseString, test_cases)
