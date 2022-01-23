import UIKit

class AClass {
    static func staticTypeMethod() {
        print("AClass staticTypeMethod")
    }
    
    class func classTypeMethod() {
        print("AClass classTypeMethod")
    }
}

class BClass : AClass {
    /*
    override static func staticTypeMethod(){
        
    }
    */
    override class func classTypeMethod() {
        print("BClass classTypeMethod")
    }
}

AClass.staticTypeMethod()
AClass.classTypeMethod()
BClass.classTypeMethod()
