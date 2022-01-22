import UIKit

struct BasicInformation {
    let name : String
    var age : Int
}

var yagomInfo : BasicInformation = BasicInformation(name : "yagom", age : 99)
yagomInfo.age = 100

var friendInfo : BasicInformation = yagomInfo

print(yagomInfo, friendInfo)
friendInfo.age = 9999

print(yagomInfo, friendInfo)

class Person {
    var height : Float = 0.0
    var weight : Float = 0.0
}

var yagom : Person = Person()
var friend : Person = yagom

print(yagom.height, friend.height)

friend.height = 175
print(yagom.height, friend.height)

func chageBasicInfo(_ info : BasicInformation){
    var copiedInfo : BasicInformation = info
    copiedInfo.age = 1
}

func changePersonInfo(_ info : Person){
    info.height = 155.3
}

chageBasicInfo(yagomInfo)
print(yagomInfo, friendInfo)

changePersonInfo(yagom)
print(yagom.height, friend.height)

let anotherFriend : Person = Person()

print(yagom === anotherFriend)
print(yagom === friend)
