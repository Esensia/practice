import UIKit

var myName : String? = "minki"

var minki : String = myName!

//myName = nil
//minki = myName!

if myName != nil {
    print("My name is \(myName!)")
} else {
    print("myName == nil")
}

// 옵셔널 바인딩
if let name = myName {
    print("My name is \(name)")
} else {
    print("myName is nil")
}

if var name = myName {
    name = "wizplan"
    print("My name is \(name)")
} else {
    print("myName is nil")
}
