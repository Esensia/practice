import UIKit

class Person {
    var name : String
    var age : Int?
    
    init(name : String){
        self.name = name
    }
}

let yagom : Person = Person(name: "yagom")
print(yagom.name)

print(yagom.age)

