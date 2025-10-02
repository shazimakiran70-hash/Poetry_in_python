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
        return [f"Suffer silently for {name}" for _ in range(3)]

    def dreams(self):
        return [
            "Love to see the moon, yet ready to fight in night",
            "Wearing traditions yet seeking modern knowledge",
            "Cherish to be in Art",
            "Cherish to be in Science"
        ]

    def final_identity(self):
        return "I was, I am, I remain a Woman"


# --- Run poetry ---
me = Woman()
print(me.pride())
print(me.desire())
print(me.courage())
print(me.principles("principles"))
print(me.principles("promises"))
print(me.sacrifices("your name"))
print(me.dreams())
print(me.final_identity())
