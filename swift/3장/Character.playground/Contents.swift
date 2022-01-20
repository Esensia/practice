import UIKit

var person : (String, Int, Double) = ("Minki",100,170.0)

print("이름 : \(person.0), 나이 : \(person.1), 신장 : \(person.2)")

person.1 = 99
person.2 = 168.5

print("이름 : \(person.0), 나이 : \(person.1), 신장 : \(person.2)")
