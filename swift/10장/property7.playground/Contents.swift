import UIKit

class Account {
    var credit : Int = 0{
        willSet {
            print("잔액이 \(credit)원에서 \(newValue)으로 변경될 예정입니다.")
        }
        
        didSet {
            print("잔액이 \(oldValue)원에서 \(credit)으로 변경됐습니다.")
        }
    }
    var dollarValue : Double {
        get {
            return Double(credit)
        }
        set {
            credit = Int(newValue * 1000)
            print("잔액을 \(newValue)달러로 변경 중입니다.")
        }
    }
}

class ForeignAccount : Account {
    override var dollarValue : Double {
        willSet {
            print("잔액이 \(dollarValue)달러에서 \(newValue)달러로 변경될 예정입니다.")
        }
        didSet {
            print("잔액이 \(oldValue)달러에서 \(dollarValue)달러로 변경됐습니다.")
        }
    }
}

let myAccount : ForeignAccount = ForeignAccount()

// 잔액이 0원에서 1000원으로 변경될 예정입니다.
myAccount.credit = 1000
// 잔액이 0원에서 1000원으로 변경되었습니다.

// 잔액이 1.0달러에서 2.0달러로 변경될 예정입니다.
// 잔액이 1000원에서 2000원으로 변경될 예정입니다.
// 잔액이 1000원에서 2000원으로 변경되었습니다.
myAccount.dollarValue = 2
// 잔액이 1.0달러에서 2.0달러로 변경되었습니다.
