import UIKit

class Room { // 호실
    var number : Int
    
    init(number : Int){
        self.number = number
    }
    
}

class Building {
    var name : String
    var room : Room?
    
    init(name : String){
        self.name = name
    }
}

struct Address {
    var province : String
    var city : String
    var street : String
    var building : Building?
    var detailAddress : String?
}

class Person {
    var name : String
    var address : Address?
    
    init(name : String){
        self.name = name
    }
}

let yagom : Person = Person(name : "yagom")

let yagomRoomViaOptionalChaining : Int? = yagom.address?.building?.room?.number

let yagomRoomViaOptionalUnwraping : Int = yagom.address!.building!.room!.number

var roomNumber : Int? = nil

if let yagomAddress : Address = yagom.address{
    if let yagomBuilding : Building = yagomAddress.building{
        if let yagomRoom : Room = yagomBuilding.room{
            roomNumber = yagomRoom.number
        }
    }
}

if let number : Int = roomNumber{
    print(number)
} else {
    print("Can not find room number")
}
