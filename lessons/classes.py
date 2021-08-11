class Planet:
    def __init__(self):
        self.name = "hoth"
        self.radius = 20000
        self.gravity = 5.5
        self.system = "hoth system"

hoth = Planet()

print(f"Name is : {hoth.name}")
print(f"Radius is : {hoth.radius}")
print(f"The gravity is : {hoth.gravity}")


