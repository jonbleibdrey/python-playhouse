items = [1,2,3,4,5]

# for item in items:
#     print(item)

# for n in range(5):
#     print(n)
#above will print out a range up to 4 but not include 5

# for n in range(3,10):
#     print(n)
#above will print out a range from 3 to ten but not include ten

# for n in range(0,20,4):
#     print(n)
#above will rpint out range between 0 and twenty but in mutiple of fours ex: 0 4 8 12 etc....

burgers = ["beef", "chicken", 'veg', 'supreme', 'double']

# for n in range(len(burgers)):
#     print(n, burgers[n])

for n in range(len(burgers) - 1, -1, -1):
    print(n, burgers[n])