package main

import "golang.org/x/tour/pic"

func Pic(dx, dy int) [][]uint8 {
    board := make([][]uint8, dy)
    for i := range board {
        board[i] = make([]uint8, dx)
        for j := range board[i] {
            board[i][j] = uint8((i + j) * i * j)
        }
    }
    return board
}

func main() {
    pic.Show(Pic)
}

