import UIKit

struct CoordinatePoint {
    var x : Int
    var y : Int
    
    func oppositePoint() -> Self {
        return CoordinatePoint(x: -x, y: -y)
    }
    
    mutating func setOppositePoint(_ opposite: CoordinatePoint){
        x = -opposite.x
        y = -opposite.y
    }
}

var yagomPosition : CoordinatePoint = CoordinatePoint(x : 10, y : 20)

print(yagomPosition)

print(yagomPosition.oppositePoint())

yagomPosition.setOppositePoint(CoordinatePoint(x: 15, y: 10))

print(yagomPosition)
