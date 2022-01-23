import UIKit

class LevelClass {
    var level : Int = 0
    
    func reset() {
        // 클래스는 self 프로퍼티 참조 불가 immutable
        //self = LevelClass()
    }
}

struct LevelStruct {
    var level : Int = 0
    
    mutating func levelUp() {
        print("Level Up!")
        level += 1
    }
    
    mutating func reset() {
        print("Reset!")
        self = LevelStruct()
    }
}

var levelStructInstance : LevelStruct = LevelStruct()
levelStructInstance.levelUp()
print(levelStructInstance.level)

levelStructInstance.reset()
print(levelStructInstance.level)

enum OnOffSwitch {
    case on, off
    mutating func nextState() {
        self = self == .on ? .off : .on
    }
}

var toggle : OnOffSwitch = OnOffSwitch.off
toggle.nextState()
print(toggle)
