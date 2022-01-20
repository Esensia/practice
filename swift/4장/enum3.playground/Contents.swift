import UIKit

enum PastaTaste {
    case cream, tomato
}

enum PizzaDough {
    case cheeseCrust, thin, original
}

enum PizzaTopping {
    case pepperoni, cheese, bacon
}

enum MainDish {
    case pasta(taste: PastaTaste)
    case pizza(dough: PizzaDough, topping : PizzaTopping)
    case chicken(withSauce : Bool)
    case rice
}

var dinner : MainDish = MainDish.pasta(taste: PastaTaste.tomato)
dinner = .pizza(dough: PizzaDough.cheeseCrust, topping : PizzaTopping.bacon)
dinner = .chicken(withSauce: true)
dinner = .rice
