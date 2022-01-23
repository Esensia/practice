import UIKit

public struct SomeType {
    private var count : Int = 0
    
    public var publicStoredProperty : Int = 0
    
    public private(set) var publicGetOnlyStoredProperty : Int = 0
    
    internal var internalComputedProperty : Int {
        get {
            return count
        }
        set {
            count += 1
        }
    }
    
    internal private(set) var internalGetOnlyComputedProperty : Int {
        get {
            return count
        }
        set {
            count += 1
        }
    }
    
    public subscript() -> Int {
        get {
            return count
        }
        set {
            count += 1
        }
    }
    
    public internal(set) subscript(some : Int) -> Int {
        get {
            return count
        }
        set {
            count += 1
        }
    }
}

var someInstance : SomeType = SomeType()

// 외부에서 접근자, 설정자 모두 사용 가능
print(someInstance.publicStoredProperty)
someInstance.publicStoredProperty = 100

// 외부에서 접근자만 사용 가능
print(someInstance.publicGetOnlyStoredProperty)
//someInstance.publicGetOnlyStoredProperty = 100

// 외부에서 접근자, 설정자 모두 사용 가능
print(someInstance.internalComputedProperty)
someInstance.internalComputedProperty = 100

// 외부에서 접근자만 사용 가능
print(someInstance.internalGetOnlyComputedProperty)
//someInstance.internalGetOnlyComputedProperty = 100

// 외부에서 접근자, 설정자 모두 사용 가능
print(someInstance)
someInstance[] = 100

// 외부에서 접근자만, 같은 모듈 내에서는 설정자도 사용 가능
print(someInstance[0])
someInstance[0] = 100
