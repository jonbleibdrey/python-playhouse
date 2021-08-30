class Planet:

    # class level attribute- has acesss to all instances
    shape = "round"

    #class methods
    @classmethod
    def commons(cls):
        return f"All planets are {cls.shape} becuase of gravity"

    #static methods
    @staticmethod
    def spin(speed = " 2000 miles per hour"):
        return f"The planet spin and spins at {speed}"
    #instint attribute- has acesss to the individual instants created
    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f"{self.name} is orbittin in the {self.system}"

# print(f"Name is : {PlanetX.name}")
# print(f"Radius is : {PlanetX.radius}")
# print(f"The gravity is : {PlanetX.gravity}")
# print(PlanetX.orbit())
