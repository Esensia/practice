import UIKit

typealias CalculateTwoInts = (Int, Int) -> Int

func addTwoInts(_ a : Int, _ b: Int) -> Int {
    return a + b
}

func multiplyTwoInts(_ a : Int, _ b : Int) -> Int {
    return a * b
}

var mathFunction : CalculateTwoInts = addTwoInts

print(mathFunction(2,5))

mathFunction = multiplyTwoInts(_:_:)

print(mathFunction(2,5))
