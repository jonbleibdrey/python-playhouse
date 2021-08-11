class Planet:

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f"{self.name} is orbittin in the {self.system}"


hoth = Planet("Hoth", 2000, 5.5, "hoth system")
print(f"Name is : {hoth.name}")
print(f"Radius is : {hoth.radius}")
print(f"The gravity is : {hoth.gravity}")
print(hoth.orbit())

PlanetX = Planet("poopooo planet", 5000, 6.0, "big planet sytem")
print(f"Name is : {PlanetX.name}")
print(f"Radius is : {PlanetX.radius}")
print(f"The gravity is : {PlanetX.gravity}")
print(PlanetX.orbit())

