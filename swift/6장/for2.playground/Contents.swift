import UIKit

let friends : [String: Int] = ["Jay" : 35, "Joe" : 29, "Jenny" : 31]

for tuple in friends {
    print(tuple)
}

let 주소 : [String : String] = ["도" : "충청북도", "시군구" : "청주시 청원구", "동읍면" : "율량동"]

for (키 ,값) in 주소 {
    print("\(키) : \(값)")
}

let 지역번호 : Set<String> = ["02","031","032"]

for 번호 in 지역번호 {
    print(번호)
}
