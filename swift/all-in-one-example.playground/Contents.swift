// This is all in one example covers major aspects of Swift language
/*
 There are few style guides that are followed, some important ones are
 
 1. RW's Style Guide: https://github.com/raywenderlich/swift-style-guide#naming
 2. LinkedIn's Style Guide: https://github.com/linkedin/swift-style-guide
 
*/
import UIKit

// Constants are declared using let keyword. Also note camel case is preffered
// while naming in Swift
let welcomeMessage = "Hello, playground"
print(welcomeMessage)

// Following is an example of string formatting, this is equivalent to
// f-strings in Python 3+
let luckyPerson: String = "Sidharth Shah"
let customizedWelcomeMessage = "Hello \(luckyPerson)"
print(customizedWelcomeMessage)

// Like C/C++ there are variety of Data Types, you can find more details
// https://www.tutorialspoint.com/swift/swift_data_types.htm
// Some of the common 
