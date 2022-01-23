import UIKit

class AClass {
    
    static var typeProperty : Int = 0
    
    var instanceProperty : Int = 0 {
        didSet {
            Self.typeProperty = instanceProperty + 100
        }
    }
    
    static var typeComputerProperty : Int {
        get {
            return typeProperty
        }
        set {
            typeProperty = newValue
        }
    }
}

AClass.typeProperty = 123

let classInstance : AClass = AClass()

classInstance.instanceProperty = 100

print(AClass.typeProperty)
print(AClass.typeComputerProperty)

class Account {
    
    static let dollarExchangeRate : Double = 1000.0
    
    var credit : Int = 0
    
    var dollarValue : Double {
        get {
            return Double(credit) / Self.dollarExchangeRate
        }
        set {
            credit = Int(newValue * Account.dollarExchangeRate)
            print("잔액을 \(newValue)달러로 변경 중입니다.")
        }
    }
}
