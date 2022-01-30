import UIKit

let multipleContainer = [[1,2,Optional.none], [3, Optional.none], [4,5,Optional.none]]

let mappedMultipleContainer = multipleContainer.map{ $0.map{ $0 }}
let flatmappedMultipleContainer = multipleContainer.flatMap{ $0.flatMap{ $0 }}

print(mappedMultipleContainer) // [[Optional(1), Optional(2), nil], [Optional(3), nil], [Optional(4), Optional(5), nil]]

print(flatmappedMultipleContainer) // [1, 2, 3, 4, 5]
