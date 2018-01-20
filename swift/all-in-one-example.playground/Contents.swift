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
// f-strings in Python 3+. Technically this is called string interpolation
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

// This is how arrays are defined, similar to Python
let laFamilia = ["Dilip", "Jayshree", "Sidharth", "Khyati", "Manan", "Vyoma"]

// This is how arrays are defined which you can append to, above array
// is constant
var laFavColors = Array<String>()
laFavColors.append("Blue")
laFavColors.append("Yello")
laFavColors.append("Red")
laFavColors.append("Green")
laFavColors.append("White")

// This is how you iterate over arrays {and possibly over other collections aswell}
for current in laFavColors{
    print("Someone from your family loves \(current) color")
}

// Set is another datastructure, its similar to tuples in Python
// Set cannot have duplicates, however unlike Python tuples you can
// insert elements to it
var laFavFoods = Set<String>()
laFavFoods.insert("Dosa")
laFavFoods.insert("Chole")
laFavFoods.insert("Undhiya")
laFavFoods.insert("Chole")
print("Family as a whole love \(laFavFoods.count) items")

// Dictionaries in swift compared to python have a wiered syntax
let laFavNums = ["Dilip": 7, "Jayshree": 8];
print("Dilip's Fav number is \(laFavNums["Dilip"]!)")

// This is how classes are define
// Note the init function is initializer, withSomeState is a "tag"
// think of it as helper text that gives programmer hints to what those
// value could be
class SomeBaseClass{
    var someState: String
    
    init(withSomeState givenState:String){
        self.someState = givenState
    }
    
    // This is how you define a method that doesnt take any argument but returns you
    //
    func greet() -> String{
        return "Hello \(self.someState)"
    }
}

// This is how you extend some class
class SomeExtendedClass : SomeBaseClass{
    func specialFoo(){
        print("Yo! this foo is so special its only avilable in SomeExtendedClass")
    }
}

// This is how classes are instansiated
let myInstance = SomeExtendedClass(withSomeState: "Yo Yo!")
myInstance.specialFoo()
print(myInstance.greet())

// This is show range is specified, using "...", this is similar
// to how varadic functions are defined in golang
for currentIndex in 1...5{
    print("We've iterated \(currentIndex) times already")
}

// This is how a function is defined in Swift
func addOne(paramOne: Int) -> Int {
    return paramOne + 1
}
addOne(paramOne: 10)

// This is how variadic functions are defined
func greetEveryOne<N> (attendees: N...){
    for currentPerson in attendees{
        print("Aloha, \(currentPerson)")
    }
}
greetEveryOne(attendees: "Manan", "Sidharth")
