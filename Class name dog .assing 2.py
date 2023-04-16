class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color= coat_color
    def description(self):
        return "name: {} and age: {}".format(self.name, self.age)   
    def get_info(self):
        return "Coat color of the dog: {}".format(self.coat_color)
class JackRussellTerrier(Dog):
    def __init__(self,name,age,coat_color, fav_food, fav_game, button_shape):
        super(). __init__(name,age, coat_color)
        self.fav_food = fav_food
        self.fav_game = fav_game
        self.button_shape = button_shape
    def food(self):
        print("Favorite food of {} is {}". format(self.name,self.fav_food))
    def game(self):
        return "Favorite game of {} is {}". format(self.name, self.fav_game)
    def shape(self):
        return "{} is like to wear {} color coat with {} shape buttons".format(self.name,self.coat_color, self.button_shape)
class Bulldog(Dog):
     def __init__(self,name,age,coat_color, variety, year):
         super(). __init__(name,age, coat_color)
         self.variety = variety
         self.year = year
     def breed(self):
          print("{} dog breed is {}".format(self.name,self.variety))
     def year_1(self):
          print("we brought {} dog to our home on {} year at his {} age". format(self.name,self.year, self.age))
    
    
a = Dog("Simba", 1, "red")
print(a.description())
print(a.get_info())
b= JackRussellTerrier("Tiger", 3,"green", "bone", "water play", "Circle")
b.food()
print(b.game())
print(b.shape())
c= Bulldog("Vicky", 3, "yellow", "Labo", "2022")
c.breed()
c.year_1()


