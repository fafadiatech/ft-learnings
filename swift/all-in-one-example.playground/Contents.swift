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
// Some of the common types include Int, String, Char, Float, Double

// Using var, we can define variables whose type can be inferred
var dontKnowTheTypeYet = "You're a string"
print(dontKnowTheTypeYet)

// You can define custom types aswell using typealias
typealias Feet = Int
var distance:Feet = 100
print(distance)

// When you declare a variable, you can define its type, this is called
// Type annotations
var age:Int = 32
print("\(luckyPerson) is \(age) years old")

// Optionals are a type, they allow us to define null variables as well
// Think of it as hint of uncertainty
var genderDisclosure:String? = nil;
if(genderDisclosure != nil){
    print("\(luckyPerson) has disclosed gender \(String(describing: genderDisclosure))")
}else{
    print("\(luckyPerson)'s gender is unknown")
}

// You can access value of an optional using forced unwrapping {this is denoted by !}
// However there are consequences to forced unwrapping. If you force unwrap an optional
// it will cause runtime error, so when doing unwrapping avoid it at all costs
genderDisclosure = "M"
print(genderDisclosure) // Notice the Optional ahead
print(genderDisclosure!)

// Automatic unwrapping is also possible. You need to use "!" at time of declaration in place of "?"
// This will mean that any furthure unwrapping you will not need "!"

// Optional binding can also be used if optional value contains an item
// What is to the left of "=" is called constant name

if let correctValue = genderDisclosure {
    print("Yo \(luckyPerson), I see you're \(correctValue)")
}
