class Woman:
    def __init__(self):
        self.heart = "daughter + mother"
        self.soft = True
        self.strong = True

    def pride(self):
        return f"Proud of this heart: {self.heart}"

    def desire(self):
        return "Chime of anklets, even on stones"

    def courage(self):
        if self.soft:
            return "Smile against storms, bow and arrow ready"
    
    def principles(self, matter):
        if matter == "principles":
            return "Ready to climb the gallows"
        elif matter == "promises":
            return "Takes the bullet in the heart"

    def sacrifices(self, name):
        return f"I suffer silently for {name}, yet carry strength in silence."

    def dreams(self):
        return ["become moon", "become stars", "seek knowledge", "wear bangles"]

    def cherish(self):
        return [
            "I cherish to be a Woman",
            "I cherish to be in Art",
            "I cherish to be in Science"
        ]

    def moon_and_night(self):
        return "Love to see the moon, yet ready to fight in night"

    def traditions_and_knowledge(self):
        return "Wearing traditions, yet seeking modern knowledge"

    def final_identity(self):
        return "I was, I am, I remain a Woman"
        

# Run the poetic code
me = Woman()
print(me.pride())
print(me.desire())
print(me.courage())
print(me.principles("principles"))
print(me.principles("promises"))
print(me.sacrifices("love"))
print(me.dreams())
print("\n".join(me.cherish()))
print(me.moon_and_night())
print(me.traditions_and_knowledge())
print(me.final_identity())
