import UIKit

let first : Int = 5
let second : Int = 5
var biggerValue : Int = 0

if first > second {
    biggerValue = first
} else if first == second {
    biggerValue = first
} else if first < second {
    biggerValue = second
} else if first == 5 {
    biggerValue = 100
}

print(biggerValue)
