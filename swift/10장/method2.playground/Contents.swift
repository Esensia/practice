import UIKit

struct LevelStruct {
    var level : Int = 0 {
        didSet {
            print("Level \(level)")
        }
    }
    
    mutating func levelUp() {
        print("Level Up!")
        level += 1
    }
    
    mutating func levelDown() {
        print("Level Down")
        level -= 1
        if level < 0 {
            reset()
        }
    }
    
    mutating func jumpLevel(to : Int){
        print("Jump to \(to)")
        level = to
    }
    
    mutating func reset() {
        print("Reset!")
        level = 0
    }
}

var levelClassInstance : LevelStruct = LevelStruct()
levelClassInstance.levelUp()
levelClassInstance.levelDown()
levelClassInstance.levelDown()

levelClassInstance.jumpLevel(to: 3)
