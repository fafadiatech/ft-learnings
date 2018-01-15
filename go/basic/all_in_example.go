package main

import (
	"fmt"
	"math/rand"
	"time"
)

// This eample is all in one example, that is based on the Tour of Golang

// This is how you define functions, you do have to specify datatypes
// and return types of the function
func add(x, y int) int {
	return x + y
}

// This is a void function, doesn't take any agruments
func greetTenTime() {
	message := "Yo Yo Honey Singh!"

	// This is how you loop over elements
	for i := 0; i < 10; i++ {
		fmt.Println("Message:", message)
	}
}

// Like python you can also have multiple return values
// Parantheses on the left talks about argument (x int)
// Parantheses on the right (int, int) is return type
func calcPlusOneAndPlusTwo(x int) (int, int) {
	return x + 1, x + 2
}

func main() {

	// This is how you hello world
	fmt.Println("Hello World")

	// aka Exported Names
	// Now lets print time in Golang
	// Couple of things to know
	// 1. "fmt" is a package
	// 2. "Println" function begins with capital letter
	// these are exported function, anything that starts with
	// lowercase is private only to that package
	// Note: A package can have multiple files what this implies is
	// scope of code across multiple files as long is avilable in
	// same package
	// This is sometimes also called EXPORTED NAMES
	fmt.Println(time.Now())

	// This is how you generate random numbers
	fmt.Println("Some random number:", rand.Intn(10))

	// This is function call that demonstrates how to do a for loop
	greetTenTime()

	// This is functional call that has multiple return values
	fmt.Println(calcPlusOneAndPlusTwo(100))

	// This is an example of how you can iterate over an arrays
	nums := []int{1, 2, 3}
	for _, current := range nums {
		fmt.Println(current)
	}

	// var is used to declare variables
	var c, python, java bool
	fmt.Println(c, python, java)

	// := operator is used for short variable declaration
	k := 10
	fmt.Println(k)

	// Following built in types are avilable
	// bool
	// string
	// int  int8  int16  int32  int64
	// uint uint8 uint16 uint32 uint64 uintptr
	// byte // alias for uint8
	// rune // alias for int32 // represents a Unicode code point
	// float32 float64
	// complex64 complex128
	// const keyword is also
	const yup bool = true
	fmt.Println(yup)

	// There is no "while" keyword
	// this is how while loops are done
	sum := 1
	for sum < 1000 {
		sum += sum
	}
	fmt.Println(sum)

	// NOTE:
	// if you want to implement "while True" equivalent of Python
	// use for {} which will run that block of code infinitely

	// This is an example of how if statement is written
	magic := 10
	if magic%2 == 0 {
		fmt.Println("Yep magic is even")
	}

	// Unlike python, go lang has "switch", "case" keywords
	// It is evaluated top to bottom -- it does greedy matching
	switch magic {
	case 10:
		fmt.Println("Yes we're even @ 10")
	default:
		fmt.Println("Seems like we're not even @ 10")
	}

	// "defer" keyword is used to delay execution of statement till end of function
	// More details: https://tour.golang.org/flowcontrol/12

	// Pointers
	// Like C there is NO POINTER ARITHMETIC
	var magic_pointer *int
	magic_pointer = &magic
	fmt.Print("Value of magic is:")

	// Accessing contents of pointer is call de-referrencing
	fmt.Println(*magic_pointer)

	// Structs are used to hold set of related fields together
	type Product struct {
		name     string
		sku      string
		category int
	}
	iphone_7 := Product{"iPhone 7", "12345", 1}
	fmt.Println("You will be winning this product, end of competition:", iphone_7.name)

	// When referencing pointers to struct to make reading cool, following notation is used
	// Note how de-referencing of structure doesn't require * in fron of iphone_7_pointer.sku line
	iphone_7_pointer := &iphone_7
	fmt.Println("SKU of the project that you will be willing will be:", iphone_7_pointer.sku)

	// These are how array are defined
	primes := [6]int{2, 3, 5, 7, 9}
	fmt.Println(primes)

	// You can also slice them like following
	// Note: negative indexing like Python is not avilable
	fmt.Println(primes[:3])

	// Maps are Golangs equivalent of Python's dictionaries {}
	// "make" keyword is used for creating a map
	mobile_numbers := make(map[string]int)
	mobile_numbers["manan"] = 123
	mobile_numbers["sidharth"] = 456
	fmt.Println(mobile_numbers)
}
