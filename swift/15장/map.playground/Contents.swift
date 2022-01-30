import UIKit

let numbers : [Int] = [0,1,2,3,4]

var doubledNumbers : [Int] = [Int]()
var strings : [String] = [String]()

// for 구문 사용
for number in numbers {
    doubledNumbers.append(number * 2)
    strings.append("\(number)")
}

print(doubledNumbers)
print(strings)

// map 메서드 사용
doubledNumbers = numbers.map({ (number : Int) -> Int in
    return number * 2
})
strings = numbers.map({ (number : Int) -> String in
    return "\(number)"
})

print(doubledNumbers)
print(strings)
