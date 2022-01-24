import UIKit

typealias VoidVoidClosure = () -> Void
let firstClosure : VoidVoidClosure = {
    print("Closure A")
}
let secondClosure : VoidVoidClosure = {
    print("Closure B")
}

// first와 second 매개변수 클로저는 함수의 반환 값으로 사용될 수 있으므로 탈출 클로저
func returnOneClosure(first : @escaping VoidVoidClosure, second : @escaping VoidVoidClosure,
                      shouldReturnFirstClosure : Bool) -> VoidVoidClosure {
    // 전달인자로 전달받은 클로저를 함수 외부로 다시 반환하기 때문에 함수를 탈출하는 클로저
    return shouldReturnFirstClosure ? first : second
}

// 함수에서 반환한 클로저가 함수 외부의 상수에 저장
let returnedClosure : VoidVoidClosure = returnOneClosure(first: firstClosure, second:
    secondClosure, shouldReturnFirstClosure: <#T##Bool#>)

returnedClosure()

var closures : [VoidVoidClosure] = []

// closure 매개변수 클로저는 함수 외부의 변수에 저장될 수 있으므로 탈출 클로저
func appendClosure(closure : @escaping VoidVoidClosure){
    // 전달인자로 전달받은 클로저가 함수 외부의 변수 내부에 저장되므로 함수를 탈출
    closures.append(closure)
}
