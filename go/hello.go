package main

//This is how you import modules/libs
import (
	"fmt"
	"math"
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

func hello_world() {
	/*Defer function halts execution of a function until surrounding
	  function's execution gets done*/
	defer fmt.Println("world")
	fmt.Println("hello")
}

type LatLong struct {
	Lat, Long float64
}

//There are no clases in Go lang, but you can define methods on structs
func (v *LatLong) Abs() float64 {
	return math.Sqrt(v.Lat*v.Lat + v.Long*v.Long)
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

	//Alternative syntax for for loop
	//This is also considered as while as there is no explicit while construct
	sum = 1
	for sum < 1000 {
		sum += sum
	}

	//This is syntax for forever aka while(1)
	// for {
	// }

	//This is how an if looks like
	if (sum % 2) == 0 {
		fmt.Println("We're even!")
	} else {
		fmt.Println("Well thats odd!")
	}

	//This kind of assign and check if statement
	// if v := math.Pow(x, n); v < lim {
	// 	return v
	// }

	//This is a switch construct, no need for break, it automatically breaks
	var current = "rock"
	switch current {
	case "rock":
		fmt.Println("Do you smell for rock is cooking?")
	case "rick":
		fmt.Println("Whoo!")
	default:
		fmt.Println("3:16")
	}

	hello_world()

	//This is how you use pointers
	var x = 10
	var px *int

	//& points to address of var
	px = &x

	//* points to value pointed by &
	fmt.Println(*px)

	//Struct is collection of fields/vars
	type Vertex struct {
		X int
		Y int
	}

	fmt.Println(Vertex{1, 2})

	//Dot notation can also be used
	//v.X = 4

	//This is how numbers are defined
	var nums [10]int
	nums[0] = 10
	fmt.Println(nums)

	//Shothand for arrays
	s := []int{2, 3, 5, 7, 11, 13}

	//Slicing arrays
	fmt.Println("s[1:4] ==", s[1:4])

	//Range in golang is a little different from python
	var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}
	for i, v := range pow {
		fmt.Printf("2**%d = %d\n", i, v)
	}

	//We're creating a hash/map from string to LatLong struct
	var m map[string]LatLong
	m = make(map[string]LatLong)
	m["Bell Labs"] = LatLong{
		40.68433, -74.39967,
	}
	fmt.Println(m["Bell Labs"])

	//Map literals are like struct except keys are required
	var m1 = map[string]LatLong{
		"Bell Labs": LatLong{
			40.68433, -74.39967,
		},
		"Google": LatLong{
			37.42202, -122.08408,
		},
	}

	fmt.Println(m1)

	//Functions are values too -- this of these as Lambdas in Python
	hypot := func(x, y float64) float64 {
		return math.Sqrt(x*x + y*y)
	}

	fmt.Println(hypot(3, 4))

	//In go lang there are no classes, you define method on Structs to achieve same effect
	v1 := &LatLong{3, 4}
	fmt.Println(*v1)
}
