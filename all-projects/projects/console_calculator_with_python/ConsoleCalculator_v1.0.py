print("This program does addition and subtraction.")
print("")

def FindOperation(List): # Returns the operation symbol in the list if any.
    Operation = None
    GotOperation = False
    if "+" in List:
        GotOperation = True
        Operation = "+"
    if "-" in List and GotOperation == False:
        GotOperation = True
        Operation = "-"
    return Operation

def FindNumbers(List):
    Index = 0
    NumbersList = []

    for Character in List:
        if Character.isdigit():
            if Index < len(NumbersList): # "len" gets the length of the list.
                NumbersList[Index] = NumbersList[Index] + Character
            else:
                NumbersList.append(Character) # Append adds "character" to the string.
        else:
            Index = Index + 1
    return NumbersList

while True:
    UserInput = input()
    ListedUserInput = list(UserInput)
    Operation = FindOperation(ListedUserInput)

    if Operation == None:
        print("You didn't provide any operation symbols.")
        continue # To restart the while loop.

    NumbersList = FindNumbers(ListedUserInput)
    if len(NumbersList) > 2:
        print("There are more than 2 numbers in your input.")
        continue

    if Operation == "+":
        Result = float(NumbersList[0]) + float(NumbersList[1])
    if Operation == "-":
        Result = float(NumbersList[0]) - float(NumbersList[1])

    print("the operation is ", Operation)
    print("the numbers in the list are ", NumbersList)
    print("Result: ", Result)