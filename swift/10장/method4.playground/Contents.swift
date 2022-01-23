import UIKit

struct Puppy {
    
    var name : String = "멍멍이"
    
    func callAsFunction() {
        print("멍멍")
    }
    
    func callAsFunction(destination : String){
        print("\(destination)(으)로 달려갑니다")
    }
    
    func callAsFunction(something: String, times : Int){
        print("\(something)(을)를 \(times)번 반복합니다")
    }
    
    func callAsFunction(color: String) -> String {
        return "\(color) 응가"
    }
    
    mutating func callAsFunction(name : String){
        self.name = name
    }
}


var doggy : Puppy = Puppy()
doggy.callAsFunction()
doggy.callAsFunction(destination: "집")
doggy.callAsFunction(destination : "뒷동산")
doggy.callAsFunction(something : "재주넘기", times : 3)
print(doggy.callAsFunction(color:"무지개색"))
doggy.callAsFunction(name : "댕댕이")
print(doggy.name)
