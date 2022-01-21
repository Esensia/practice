import UIKit

class Car {
    var modelYear : Int?
    var modelName : String?
}

struct SmartPhone {
    var company : String?
    var model : String?
}

func == (lhs: Car, rhs : Car) -> Bool {
    return lhs.modelName == rhs.modelName
}

func == (lhs: SmartPhone, rhs : SmartPhone) -> Bool{
    return lhs.model == rhs.model
}

let myCar = Car()
myCar.modelName = "S"

let yourCar = Car()
yourCar.modelName = "S"

var myPhone = SmartPhone()
myPhone.model = "SE"

var yourPhone = SmartPhone()
yourPhone.model = "6"

print(myCar == yourCar)
print(myPhone == yourPhone)
