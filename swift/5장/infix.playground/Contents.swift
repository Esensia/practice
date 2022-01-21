import UIKit
import Foundation

infix operator ** : MultiplicationPrecedence

func ** (lhs: String, rhs : String) -> Bool {
    return lhs.contains(rhs)
}

let helloYagom : String = "Hello yagom"
let yagom : String = "yagom"
let isContainsYagom : Bool = helloYagom ** yagom

print(isContainsYagom)
