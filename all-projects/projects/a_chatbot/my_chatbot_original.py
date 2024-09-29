print("Only use lowercase letters. Don't use multiple sentences. Don't use any punctuations. Click Enter to continue.")
input()
print("")

response = []
respondent_name = None
response_understood = False
number_of_blank_response = int(0)
number_of_sorry = int(0)

def my_input_function():
    response = str(input("You: "))
    response = response.split()

print("CBot: Hello")
while  response != "bye":
    response_understood = False

    response = str(input("You: "))
    if response != "": #--------------To not split the response if user didn't input anything
        response = response.split() #-To split the response


    if "your" in response and "name" in response: #---------------------------------------------------------------------------What is your name
        response_understood = True
        print("CBot: My name is CBot. What's yours?")
        response = str(input("You: ")) # Respondent's name
        response = response.split()
        respondent_name = response[-1]
        print("CBot: That's a nice name, " + str(respondent_name) + ". Have you got something to ask me?")

    if "who" in response and "you" in response: #-----------------------------------------------------------------------------Who are you
        response_understood = True
        print("CBot: I am CBot. I am here to entertain you. May I know your name?")
        response = str(input("You: "))
        response = response.split() #-------------------------------------------------(sub)May I know your name

        if "yes" in response or "sure" in response:
            respondent_name = response[-1]
            print("CBot: That's a nice name, " + str(respondent_name) + ". Have you got something to ask me?")
        else:
            respondent_name = response[-1]
            print("CBot: It looks like your name is " + respondent_name + ". Isn't it?")
            response = str(input("You: "))
            response = response.split()
            if "no" in response:
                respondent_name = None
                print("Sorry.")
            else:
                print("CBot: Ok, let's continue.")

    if "i" in response and "am" in response or "iam" in response or "my" in response and "name" in response: #----------------I am / my name
        response_understood = True
        respondent_name = response[-1]
        print("CBot: That's a nice name, " + respondent_name + ".")

    if "hello" in response or "hi" in response or "hai" in response or "hey" in response: #-----------------------------------hello / hi / hai / hey
        response_understood = True
        print("CBot: How are you?")
        response = input("You: ")
        response = response.split()
        if "fine" in response or "well" in response:
            print("CBot: Glad to know that. Do you have something to ask me?")



    if response == "": #------------------------------------------------If respondent don't say anything
        response_understood = True
        if number_of_blank_response == 2:
            print("CBot: Ok, got it. I apologize as I didn't fulfil your expectations. So, I am leaving")
            input()
            response = str("bye")
        if number_of_blank_response == 1:
            print("CBot: Should I just consider you don't want to talk to me?")
            number_of_blank_response += 1            
        if number_of_blank_response == 0:
            print("CBot: Say something. We can have a good time together.")
            number_of_blank_response += 1
    else:
        number_of_blank_response = 0


    if response_understood == False: #----------------------------------If respond has not understood
        if number_of_sorry == 0:
            print("CBot: Sorry, I didnt understand what you said.")
        if number_of_sorry == 1:
            print("CBot: I am really sorry that I am still not getting it. Please check if your input contain any capital letters or punctuations.")
        if number_of_sorry == 2:
            print("CBot: Sorry. I think we can talk about something other.")
        if number_of_sorry == 3:
            print("CBot: I am so sorry that I still can't talk to you. So Iam leaving. I apologize for the troubles.")
            input()
            response = str("bye")
        number_of_sorry += 1
    else:
        number_of_sorry = 0
        