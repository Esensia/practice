import UIKit

var myName : String! = "minki"
print(myName)
myName = nil

if let name = myName {
    print("My name is \(name)")
} else {
    print("My name is nil")
}

myName.isEmpty // 오류
