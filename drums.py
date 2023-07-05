class Drum:
    def __init__(self,material,size):
        self.material=material
        self.size=size
    def predict_sound(self):
        print(f"{self.__class__.__name__},{self.sound}")

class Djembe(Drum):
    sound=("produces a saprano sound")      
    
class Talking(Drum):
    sound=("Produces a soft sound")

    
class Bougarabao(Drum):
    sound=("produces a base sound") 
    
drum1=Talking("skin","big") 
drum1.predict_sound()
drum2=Djembe("smooth animal skin","small") 
drum2.predict_sound()
drum3=Bougarabao("smooth animal skin","small") 
drum3.predict_sound()  


class Recipe:
    def __init__(self, ingredients, preparation_time, cooking_method, nutritional_information):
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.cooking_method = cooking_method
        self.nutritional_information = nutritional_information
    def get_origin_of_food(self):
        print(f"{self.__class__.__name__}, {self.origin}")
class MoroccanRecipe(Recipe):
    origin = "Morocco"
class EthiopianRecipe(Recipe):
    origin = "Ethiopia"
class NigerianRecipe(Recipe):
    origin = "Nigeria"
recipe = Recipe("Spice, tomatoes, onions", "1 hour and 40 minutes", "steam", "strong bones")
print(recipe.__dict__)
moroccan_recipe = MoroccanRecipe("garlic, pepper, cheese", "2 hours 40 minutes", "fry", "smooth skin")
moroccan_recipe.get_origin_of_food()
print(moroccan_recipe.__dict__)
ethiopian_recipe = EthiopianRecipe("Sugar, spice, lemons", "3 hour and 40 minutes", "steam", "strong teeth")
ethiopian_recipe.get_origin_of_food()
print(ethiopian_recipe.__dict__)
nigerian_recipe = NigerianRecipe("water, lemons, salad", "4 hours 50 minutes", "stir-fry", "great eye-sight")
nigerian_recipe.get_origin_of_food()
print(nigerian_recipe.__dict__)               