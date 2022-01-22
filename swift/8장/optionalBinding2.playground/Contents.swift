import UIKit

var myName : String? = "minki"
var yourName : String? = nil

if let name = myName, let friend = yourName {
    print("We are friend! \(name) & \(friend)")
}

yourName = "erick"

if var name = myName, var friend = yourName {
    print("We are friend! \(name) & \(friend)")
}
