import UIKit

typealias CalculateTwoInts = (Int, Int) -> Int

func addTwoInts(_ a : Int, _ b: Int) -> Int {
    return a + b
}

func multiplyTwoInts(_ a : Int, _ b : Int) -> Int {
    return a * b
}

func printMathResult(_ mathFunction: CalculateTwoInts, _ a : Int, _ b : Int) -> Void {
    print("Result: \(mathFunction(a,b))")
}

printMathResult(addTwoInts(_:_:), 3, 3)

func chooswMathFunction(_ toAdd: Bool) -> CalculateTwoInts {
    return toAdd ? addTwoInts : multiplyTwoInts
    
}

printMathResult(chooswMathFunction(true),3,5)
