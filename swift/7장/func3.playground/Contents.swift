import UIKit

func sayHello(_ name: String,_ times: Int = 3) -> String {
    var result : String = ""
    
    for _ in 0..<times {
        result += "Hello \(name)! "
    }
    return result
}

print(sayHello("Chope"))

func sayHelloToFriends(me : String, friends names: String...) -> String {
    var result : String = ""
    
    for friend in names {
        result += "Hello \(friend)! "
    }
    
    result += "I'm " + me + "!"
    return result
}

print(sayHelloToFriends(me: "yagom", friends: "John","Mad"))
