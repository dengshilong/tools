package main

import (
    "fmt"
)

/*func Sqrt(x float64) float64 {
    z := 1.0
    for i:= 0; i < 10; i++ {
        z = z - (z * z - x) / (2 * z)
    }
    return z
}*/
func Sqrt(x float64) float64 {
    z := 1.0
    for {
        y := z - (z * z - x) / (2 * z)
        t := y - z
        if t < 0 {
            t = -t
        }
        if t < 0.0000001 {
            return y
        } else {
            z = y
        }
    }
}
    

func main() {
    fmt.Println(Sqrt(2))
}

