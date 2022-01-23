import UIKit

struct CoordinatePoint {
    var x : Int = 0   // 저장 프로퍼티
    var y : Int = 0   // 저장 프로퍼티
}

let yagomPoint : CoordinatePoint = CoordinatePoint()

let wizplanPoint : CoordinatePoint = CoordinatePoint(x : 10, y : 5)
class Position {
    var point : CoordinatePoint = CoordinatePoint()
    let name : String = "unknown"
    
}


let yagomPosition : Position = Position()

