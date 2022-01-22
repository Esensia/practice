import UIKit

func sayHello(_ name: String, _ times: Int) -> String {
    var result : String = ""
    
    for _ in 0..<times {
        result += "Hello \(name)! "
    }
    return result
}

func sayHello(to name : String, _ times : Int) -> String {
    var result : String = ""
    
    for _ in 0..<times {
        result += "Hello \(name)! "
    }
    
    return result
}

func sayHello(to name : String, repeatCount times : Int) -> String {
    var result : String = ""
    
    for _ in 0..<times {
        result += "Hello \(name)! "
    }
    return result
}
print(sayHello("Chope",2))

print(sayHello(to: "Chope", 2))
print(sayHello(to: "Chope", repeatCount : 2))
