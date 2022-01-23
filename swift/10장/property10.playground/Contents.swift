import UIKit

class Person {
    var name : String
    
    init(name : String){
        self.name = name
    }
}

struct Stuff {
    var name : String
    var owner : Person
}

print(type(of: \Person.name))
print(type(of: \Stuff.name))
