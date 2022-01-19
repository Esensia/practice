import UIKit

let name : String = "yagom"

var introduce : String = String()

introduce.append("제 이름은")

introduce = introduce + " " + name + "입니다"

print(introduce)

print("name의 글자 수: \(name.count)")

print("introduce가 비어있습니까? \(introduce.isEmpty)")

let unicodeScalarValue : String = "\u{2665}"
print(unicodeScalarValue)
