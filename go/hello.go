package main

//This is how you import modules/libs
import "fmt"

//This is how you write a simple function in golang
func add(a, b int) int{
     return a + b
}

//This is where main code execution get started
func main(){
     fmt.Println("Hello World")
     fmt.Println(add(100, 1))
     fmt.Println(add(100, 100))

     //This is how a for loop works in golang     
     sum := 0
     for i := 0; i < 10; i++{
     	 sum += i
     	 fmt.Println(sum)
     }
}    

