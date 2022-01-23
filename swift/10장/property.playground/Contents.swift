import UIKit

struct CoordinatePoint {
    var x : Int     // 저장 프로퍼티
    var y : Int     // 저장 프로퍼티
}

let yagomPoint : CoordinatePoint = CoordinatePoint(x : 10, y : 15)

class Position {
    var point : CoordinatePoint
    let name : String
    
    init(name : String, currentPoint : CoordinatePoint){
        self.name = name
        self.point = currentPoint
    }
}


let yagomPosition : Position = Position(name : "yagom", currentPoint : yagomPoint)
