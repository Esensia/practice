import UIKit

var names : Set<String> = Set<String>()
var names2 : Set<String> = []

var names3 : Set<String> = ["100","200","300","200"]

print(names3.count)
print(names3)

names3.insert("500")

print(names3.remove("100"))
