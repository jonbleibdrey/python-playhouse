# ninja_belts = {"crystal" : "red", "ryu": "black"}
def ninja_intro(dictionary):
    for key,val in dictionary.items():
        print(f"i am {key} and i am a {val} belt")

ninja_belts = {}

while True:
    ninja_name = input("enter a nija name")
    ninja_belt = input("enter the color of the belt")
    ninja_belts[ninja_name] = ninja_belt

    another = input("add another? (y/n)")
    if another == "y":
        continue
    else:
        break

ninja_intro(ninja_belts)

# to find all the keys in a varibale
# dict_keys(['crystal', 'ryu'])
# print(ninja_belts.keys())

# dictionaries are basically objects in python!

# to find if a key is actually in the dictionarie
# print("ryu" in ninja_belts)

# this will return a list of all the keys
# print(list(ninja_belts.keys()))

# return the vlaues in a list
# print(list(ninja_belts.values()))

# how to add a object to the array
# ninja_belts["yoshi"] = "red"
