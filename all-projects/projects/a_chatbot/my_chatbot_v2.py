print("Don't use any punctuations. Don't use multiple lines. Keep the question simple. Click Enter to continue.")
Confirmation = str("_") #---Makes the User click Enter to continue.
while Confirmation != "":
    Confirmation = input()





ChatBotName = str("ChatBot")
Response = str("")
Username = str()
NumberOne = int()
NumberTwo = int()

def InputFunction(): #---Gets the input, make it all lowercase and split it into a list. Doesn't split if the input is empty.
    global Response
    Response = input("You: ")
    Response = Response.lower() #---.lower() method makes all the characters in a string lowercase.
    if Response != "":
        Response = Response.split() #---.split() method splits the string into a list.


def NumbersGettingFunction(): #---Function that gets the first two numbers in the response.
    global Response
    global NumberOne
    global NumberTwo
    NumberOfNumbers = int()
    x = 0

    while NumberOfNumbers != 1: #---Finding the first number.
        try:
            Response[x] = int(Response[x])
            NumberOfNumbers += 1
            NumberOne = Response[x]
            x += 1
        except:
            x += 1
    while NumberOfNumbers != 2: #---Finding the second number.
        try:
            Response[x] = int(Response[x])
            NumberOfNumbers += 1
            NumberTwo = Response[x]
            x += 1
        except:
            x += 1


def AdditionFunction():
    Sum = NumberOne + NumberTwo
    print(ChatBotName + ": " + "The sum of the numbers you provided is " + str(Sum) + ". Thanks.")
def MultiplicationFunction():
    Product = NumberOne * NumberTwo
    print("ChatBotName" + ": " + "Sure, the product is " + str(Product) + ". Thanks")







#---STARTING---#

print(ChatBotName + ": " + "Hello! I am " + ChatBotName + ". What is your name?") #---Getting Username.
InputFunction()
Username = Response[-1]

print(ChatBotName + ": " + "It looks like your name is " + Username + ". Right?") #---Confirming Username.
InputFunction()
while "yes" not in Response and "sure" not in Response and "exactly" not in Response and "yeah" not in Response and "yep" not in Response and "ya" not in Response and "m" not in Response and "mm" not in Response and "mmm" not in Response:
    print(ChatBotName + ": " + "Then What is your name?")
    InputFunction()
    print(ChatBotName + ": " + "Is it " + Response[-1] + "?")
    Username = Response[-1]
    InputFunction()

print(ChatBotName + ": " + "Ok, let's continue, " + Username + ". I can do addition, subraction, multiplication and divition. How can I help you?")



while True:
    InputFunction()
    ResponseUnderstood = False

    if "add" in Response or "plus" in Response or "+" in Response:
        ResponseUnderstood = True
        NumbersGettingFunction()
        AdditionFunction()
    if "multiply" in Response or "product" in Response or "*" in Response or "times" in Response:
        ResponseUnderstood = True
        NumbersGettingFunction()
        MultiplicationFunction()

    if "wow" in Response or "unbelievable" in Response or "extraordinary" in Response or "amazing"  in Response or "awesome" in Response:
        ResponseUnderstood = True
        print(ChatBotName + ": " + "I am glad that you liked me. I can help you more, and it's my pleasure.")

    if "perform" in Response or "do" in Response and "addition" in Response:
        ResponseUnderstood = True
        print(ChatBotName + ": " + "Sure. Provide me the numbers.")
        try:
            InputFunction()
            NumbersGettingFunction()
            AdditionFunction()
        except:
            print(ChatBotName + ": " + "Sorry. It seems like you didn't provide me the numbers or there is some other issue. Anyways, Sorry. Let's try again.")





    if ResponseUnderstood == False:
        print(ChatBotName + ": " + "Sorry, I didn't understand what you said. Let's start this over. How can I help you?")