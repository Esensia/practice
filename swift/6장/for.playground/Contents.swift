import UIKit

for i in 0...2 {
    print(i)
}

for i in 0...5 {
    
    if i.isMultiple(of: 2){
        print(i)
        continue
    }
    print("\(i) == 홀수")
}

let helloSwift : String = "Hello Swift!"

for char in helloSwift {
    print(char)
}

var result : Int = 1

for _ in 1...3 {
    result *= 10
}

print("\(result)")
