class Pokemon():
    """ This is a class that represents the main character in a game. """
    def __init__(self):
        """ This is a method that sets up the variables in the object. """
        self.name = ""
        self.type1 = ""
        self.type2 = ""
        self.hp = None
        self.attack = None
        self.sp_attack = None
        self.sp_defense = None
        self.speed = None

# for example
pidgey = Pokemon()
pidgey.name = "Pidgey"
pidgey.type1 = "Normal"
pidgey.hp = 40
pidgey.attack = 45
pidgey.sp_attack = 35
pidgey.sp_defense = 35
pidgey.speed = 56
