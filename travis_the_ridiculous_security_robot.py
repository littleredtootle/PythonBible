known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

while True:
    print("Hi! My name is Travis the Security Robot.")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the security system? (Y/N): ").upper()

        if remove == "Y":
            known_users.remove(name)
            print("OK, I have removed you from the security system. Sorry to see you go {}!".format(name))
        elif remove == "N":
            print("No problem, I didn't want you to leave anyway! ")
        
    else:
        print("Name NOT recognised.")
        answer = input("Did you type it correctly? (Y/N): ").strip().capitalize()
        if  answer == ("Y"):
            add_name = input("OK, I don't think we have met before {}. Would you like me to add your name to the security system? (Y/N): ".format(name)).strip().capitalize()
            if add_name == "Y":
                known_users.append(name)
                print("Great! You are now on our security system {}! ".format(name))
            else:
                print("OK. Nice to meet you {}!".format(name))
        else:
            print("OK. Please try again. ")

            

        

