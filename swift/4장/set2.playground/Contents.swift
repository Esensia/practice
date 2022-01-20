import UIKit

enum School {
    case primary
    case elementary
    case middle
    case high
    case college
    case university
    case graduate
}

var highestEducationLevel : School = School.university
var highestEducationLevel2 : School = .university

print(highestEducationLevel)
