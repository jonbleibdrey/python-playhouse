from space.planet import Planet
from space.calc import planet_mass,planet_vol

PlanetX = Planet("poopooo planet", 5000, 6.0, "big planet sytem")

PlanetX_mass = planet_mass(PlanetX.gravity, PlanetX.radius)
PlanetX_vol = planet_vol(PlanetX.radius)

print(f"{PlanetX.name} has a mass of {PlanetX_mass} and a volume of {PlanetX_vol} ")
