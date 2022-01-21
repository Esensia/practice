import UIKit
// repeat-while == do-while
var names : [String] = ["Joker","Jenny","Nova","yagom"]

repeat {
    print("Good bye \(names.removeFirst())")
} while names.isEmpty == false
