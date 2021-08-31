def cough_dec(function):

    def func_wrapper():
        #code before function
        print("*cough*")
        function() #this is  the question function down below
        #code after the function
        print("*cough*")
        # then we fire the func wrapper funciton
    return func_wrapper

@cough_dec
def question():
    print("can you give me a discount? ")

@cough_dec
def answer():
    print("its only 50 cents you cheap sake")

question()
answer()