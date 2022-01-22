import UIKit

func hello(name : String) -> String {
    return "Hello \(name)!"
}

func introduce(name : String) -> String {
    "제 이름은 "+name+"입니다."
}

let helloJenny : String = hello(name : "Jenny")

print(helloJenny)

print(introduce(name : "홍민기"))
