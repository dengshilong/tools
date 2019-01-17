package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {
    y := 0
    a := 0
    b := 1
    return func() int {
       y = a
       t := a + b
       a = b
       b = t   
       return y
    }
}

func main() {
    f := fibonacci()
    for i := 0; i < 10; i++ {
        fmt.Println(f())
    }
}

