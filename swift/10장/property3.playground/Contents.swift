import UIKit

struct CoordinatePoint {
    var x : Int
    var y : Int
}
class Position {
    var point : CoordinatePoint?
    let name : String
    
    init(name : String){
        self.name = name
    }
    
}

let yagomPosition : Position = Position(name : "yagom")

yagomPosition.point = CoordinatePoint(x : 20, y: 10)
