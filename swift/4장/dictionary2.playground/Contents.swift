import UIKit

typealias StringIntDictionary = [String : Int]

var numberForName : StringIntDictionary = StringIntDictionary()
var numberForName2 : Dictionary<String, Int> = Dictionary<String, Int>()
var numberForName3 : [String : Int] = [String : Int]()
var numberForName4 : [String : Int] = [:]
var numberForName5 : [String : Int] = ["Minki":28,"Hakyeong":28,"Seunghan":29]

print(numberForName5["junhu"])
print(numberForName5["Hakyeong"])

numberForName5["Hakyeong"] = 25
print(numberForName5["Hakyeong"]!)

print(numberForName5.removeValue(forKey: "Hakyeong"))
print(numberForName5.removeValue(forKey: "Hakyeong"))

print(numberForName5["junhu", default : 0])
