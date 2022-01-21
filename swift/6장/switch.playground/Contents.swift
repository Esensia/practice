import UIKit

let integerValue : Int = 5

switch integerValue {
case 0:
    print("Value == zero")
case 1...10:
    print("Value == 1~10")
    fallthrough
case Int.min..<0, 101..<Int.max:
    print("Value < 0 or Value > 100")
    break
default :
    print("10 < Value <= 100")
}

let doubleValue : Double = 3.0

switch doubleValue {
case 0 :
    print("Value == zero")
case 1.5...10.5 :
    print("1.5 <= Value <= 10.5")
default :
    print("Value == \(doubleValue)")
}

let stringValue : String = "Liam Neeson"

switch stringValue {
case "yagom" :
    print("He is yagom")
case "Jay":
    print("He is Jay")
case "Jenny", "Joker","Nova":
    print("He or She is \(stringValue)")
default :
    print("\(stringValue) said 'i don't know who you are'")
}
