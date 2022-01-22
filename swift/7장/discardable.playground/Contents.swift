import UIKit

func say(_ something : String) -> String {
    print(something)
    return something
}

@discardableResult
func discardableResultSay(_ something : String) -> String {
    print(something)
    return something
}

discardableResultSay("hello")
say("hello")
