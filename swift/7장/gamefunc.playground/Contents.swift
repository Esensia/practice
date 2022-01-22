import UIKit

typealias MoveFunc = (Int) -> Int

func goRight(_ currentPosition : Int) -> Int {
    return currentPosition + 1
}

func goLeft(_ currentPosition : Int) -> Int {
    return currentPosition - 1
}

func functionForMove(_ shouldGoLeft : Bool) -> MoveFunc {
    return shouldGoLeft ? goLeft : goRight
}

var position : Int = 3

let moveToZero : MoveFunc = functionForMove(position > 0 )
print("원점으로 갑시당")

while position != 0 {
    print("\(position)...")
    position = moveToZero(position)
}
