import UIKit

class Person {
    var height : Float = 0.0
    var weight : Float = 0.0
    
    deinit {
        print("객체가 소멸됩니다.")
    }
}

var minki : Person = Person()
minki.height = 10
minki.weight = -1

let july : Person = Person()
// 클래스는 구조체와 다르게 참조타입이므로 클래스의 인스턴스를 상수 let으로 선언해도 내부 프로퍼티 값을 변경할 수 있다.
july.height = 111
july.weight = 1500

var yagom : Person? = Person()
yagom = nil
