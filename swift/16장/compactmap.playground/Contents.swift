import UIKit

let optionals : [Int?] = [1,2,nil,5]

let mapped : [Int?] = optionals.map { $0 }
let compactMapped : [Int] = optionals.compactMap{ $0 }

print(mapped) // [Optional(1), Optional(2), nil, Optional(5)]
print(compactMapped) // [1, 2, 5]
