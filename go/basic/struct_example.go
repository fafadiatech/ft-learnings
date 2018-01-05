package main

import "fmt"

type Person struct {
	name string
	age  int
}

func (p *Person) age_after(n int) int {
	return p.age + n
}

func main() {
	sidharth := Person{"Sidharth", 32}
	fmt.Println(sidharth.name)
	final_message := fmt.Sprintf("%s will be %d in 5 years", sidharth.name, sidharth.age_after(5))
	fmt.Println(final_message)
}
