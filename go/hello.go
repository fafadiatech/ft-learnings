package main

//This is how you import modules/libs
import (
	"fmt"
	"math/rand"
)

//This is how you write a simple function in golang
//In golang type comes after the variables names
func add(a, b int) int {
	return a + b
}

//Functions is go can return multiple values just like python
func magic(a, b int) (int, int) {
	return a + b, a - b
}

//Functions is go can return multiple named values
func magic_1(a, b int) (sum, diff int) {
	return a + b, a - b
}

//Functions is go can return multiple named values, return in following is considered "naked"
func magic_2(a, b int) (sum, diff int) {
	sum = a + b
	diff = a - b
	return
}

func magic_3() int {
	//:= is short hand for assignment alternative to var synatax only avilable within function
	//Any variable declaration outside function must begin with var,func etc..
	//Type is inferred here, value of RHS determindes type on LHS
	magic_number := 7
	return magic_number
}

//This is where main code execution get started
func main() {
	fmt.Println("Hello World")
	fmt.Println(add(100, 1))
	fmt.Println(add(100, 100))

	//This is how a for loop works in golang
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
		fmt.Println(sum)
	}

	//This is how you call functions
	fmt.Println("My fav number is", rand.Intn(10))
	fmt.Print(magic(10, 5))

	//var is used to declare variables
	var c, python, java bool
	fmt.Println(c, python, java)

	//These are variables with initializers
	var c1, python1, java1 = true, false, "no!"
	fmt.Println(c1, python1, java1)

	fmt.Println(magic_3())

	//Types in go
	// bool
	// string
	// int  int8  int16  int32  int64
	// uint uint8 uint16 uint32 uint64 uintptr
	// byte // alias for uint8
	// rune // alias for int32
	// // represents a Unicode code point
	// float32 float64
	// complex64 complex128

	//Variables without explicit initialization are set to 0
	var i int
	fmt.Println(i)

	i = 42
	var f = float64(i)
	fmt.Println(f)

	//Constansts are defined like so
	const Pi = 3.14
}
