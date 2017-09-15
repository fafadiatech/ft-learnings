package demo

// This is how a function is written
fun add(x: Int, y: Int) = x + y

// Example of a conditional
fun isEven(x: Int): Boolean{
    if(x % 2 == 0){
        return true
    }
    return false
}


fun main(args: Array<String>) {
    println("Hello World")

    println(add(100, 1))

    // val is used to define values {these are non-mutable}
    // i.e. once assigned it cannot be changed
    val a: Int = 1

    // Int is inferred
    val b = 2

    // When value is not immediately assigned it type need to define
    val c: Int
    c = 10

    println(a)
    println(b)
    println(c)

    // var is used to define variables that are mutable
    var x = 10
    x++
    println("Value of x is:" + x.toString())

    println("Is 21 Even:" + isEven(21).toString())

    // ? allows a variable to be null -> Aka Nullable
    var name: String?
    name = null

    // Example of iteration, listOf returns read-only list of elements
    val family = listOf("Manan", "Sidharth", "Khyati", "Vyoma", "Jayshree", "Dilip")
    for(member in family){
        println("In da familiy" + member)
    }

    //Ranges in kotlin
    for(i in 1..20 step 3){
        println("I've repeated myself " + i.toString() + " time!")
    }

    // Functional styles in Kotlin
    family.sortedBy{ it }
          .map{ it.toUpperCase() }
          .forEach{ println(it) }
}