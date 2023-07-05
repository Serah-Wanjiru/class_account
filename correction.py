class Ankara:
    def __init__(self, temperature, mood):
        self.temperature = temperature
        self.mood = mood

    def get_pattern(self):
        if self.temperature >= 20 and self.mood >= 5:
            return "Wear light and more patterned Ankara."
        else:
            return "Wear dull and less patterned Ankara."

    def set_temperature(self, temperature):
        self.temperature = temperature

    def set_mood(self, mood):
        self.mood = mood

ankara = Ankara(20, 7)
print(ankara.get_pattern())

ankara=Ankara(15,3)
print(ankara.get_pattern())


class Ankara:
    def __init__(self,temperature,moods):
        self.temperature=temperature
        self.moods=moods
        
    def get_pattern(self):
        mood=range(2,10)
        temperature=range(20,30)  
        if self.temperature in temperature and self.moods in mood:
            return f"wear light and more flowery ankara" 
        else:
            return f"wear dull and less pattern ankara" 
        
ankara=Ankara(15,1)   
print(ankara.get_pattern())     