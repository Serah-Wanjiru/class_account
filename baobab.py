empty_list =[]
class Possible_Fruit:
    def __init__(self,powers,effect,season,name):
        self.powers=powers
        self.effect=effect
        self.season=season
        self.name=name
    def __repr__(self):
         return f"{self.name} {self.effect} {self.powers} {self.season}"
fruits = Possible_Fruit(powers="changecolor",effect="gives energy",season="wet",name="big baobab")
empty_list.append(fruits)
print(fruits)
print(empty_list)
class Seasons:
    def __init__(self,seasons):
        self.seasons = seasons
 
    def predict_fruit(self):
        for item in empty_list:
            if self.seasons == item.season:
                print( f"{item.name} was produced in this {self.seasons} season")
s = Seasons(seasons="wet")
s.predict_fruit()