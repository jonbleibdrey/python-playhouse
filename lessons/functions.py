# name = input("Enter your name: ")
# time = input("enter time of day: ")

# def greet(name = "jacky", time = "morning"):
#     print(f"Good {time} {name}, hope you are well")

# greet()


def area(radius):
    return 3.142 * radius * radius

def vol(area, length):
    print(area * length)

radius = int(input("enter the radius: "))
length = int(input("enter the length: "))


vol(area(radius), length)



