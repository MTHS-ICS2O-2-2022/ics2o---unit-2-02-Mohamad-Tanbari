// Made by Mohamad
// Made on: March 2023
//
// This program does simple math

package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println("7 + 3 =", (7+3))
	fmt.Println("7 - 3 =", (7-3))
	fmt.Println("7 * 3 =", (7*3))
	fmt.Println("7 / 3 =", (7/3))
	fmt.Println("8 + 2^2", (8+math.Pow(2, 2)))

	//end of program
	fmt.Println("\nDone")
}
