import UIKit

prefix operator **

prefix func ** (value : Int) -> Int {
    return value * value
}

prefix func ! (value : String) -> Bool {
    return value.isEmpty
}

let minusFive : Int = -5
let sqrtMinusFive : Int = **minusFive

print(sqrtMinusFive)

var stringValue : String = "yagom"
var isEmptyString : Bool = !stringValue

print(isEmptyString)

stringValue = ""
isEmptyString = !stringValue

print(isEmptyString)
