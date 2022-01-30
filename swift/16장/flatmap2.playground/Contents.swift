import UIKit

func stringToInteger(_ string : String) -> Int? {
    return Int(string)
}

func integerToString(_ integer : Int) -> String? {
    return "\(integer)"
}

var optaionalString : String? = "2"

let flattenResult = optaionalString.flatMap(stringToInteger)
.flatMap(integerToString)
.flatMap(stringToInteger)
print(flattenResult)

let mappedResult = optaionalString.map(stringToInteger)
print(mappedResult)
