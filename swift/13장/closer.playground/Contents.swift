import UIKit

func makeIncrementer(forIncrement amount : Int) -> (() -> Int){
    var runningTotal = 0
    func incrementer() -> Int {
        runningTotal += amount
        return runningTotal
    }
    return incrementer
}

let incrementByTwo : (() -> Int) = makeIncrementer(forIncrement: 2)
/*
let first : Int = incrementByTwo()
let second : Int = incrementByTwo()
let third : Int = incrementByTwo()
*/
let sameWithIncrementByTwo : (() -> Int) = incrementByTwo

let first : Int = incrementByTwo()
let seocnd : Int = sameWithIncrementByTwo()

