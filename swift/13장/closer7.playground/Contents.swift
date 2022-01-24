import UIKit

var customerInLine : [String] = ["minki","mings","gid"]
print(customerInLine.count)

// 클로저를 만들어두고 클로저 내부의 코드를 미리 실행하지 않고 갖고만 있는다.
let customerProvider : () -> String = {
    return customerInLine.removeFirst()
}
print(customerInLine.count)

print("Now serving \(customerProvider())!")
print(customerInLine.count)
