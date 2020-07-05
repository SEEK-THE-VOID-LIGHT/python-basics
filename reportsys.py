#Felix Report system 0.1 alpha

version = "v0.3 alpha"

rep={}

def save():
    try:
        with open("repo.txt","r") as f:
            buffer = f.read()
        with open("repo.txt","w") as f:
            for i in rep:
                f.write(rep[i]+"\n")
            f.write(buffer)
        rep.clear()
    except:
        print("\nCreated file repo.txt")
        with open("repo.txt","w") as f:
            for i in rep:
                f.write(rep[i]+"\n")
        rep.clear()

def reportroutine():
    try:
        name = input("-----\nWhom would you like to report?\n-----\n")
        reason = input("\nOk. And for what reason? ")
        print("\nOK. Thank you for your report!")
        rep[name] = name+" - "+reason
        press()

    except:
        print("\nAn error ocurred. Pls try again later :(")
        press()

def lookroutine():
    finder = input("\nWhich person do you wish to find?\n ")
    with open("repo.txt","r") as f:
        for line in f:
            if line.find(finder) != -1:
                result = line.replace(finder+" - ","")
                print(f"\n!!!\nYes, the person is registered because of: {result}\n!!!")
                break
            else:
                print("searching...")
                continue
    press()
def deleteroutine():
    save()
    delchoise = input("\nInput Name of the person you want to delete from the database: ")
    with open("repo.txt","r") as file:
        lines = file.readlines()
    with open("repo.txt","w") as file:
        for line in lines:
            if line.strip("\n").startswith(delchoise) != True:
                file.write(line)
                print("searching")
            else:
                file.write("<deleted>\n")
                print("\ndeleted successfull!")
    press()
def listroutine():
    print("\n")
    try:
        with open("repo.txt","r") as file:
            for line in file:
                print(line)
        press()
    except:
        print("\nthe file semms not to exist :(")
        press()

def press():
    enter = input("\npress ENTER\n")
    if enter == "":
        pass
    else:
        print("ok?..")
        pass

print("""
=========================================================================
______                      _    ___   _   _                             
| ___ \                    | |  / _ \ | | | |                            
| |_/ /___ _ __   ___  _ __| |_/ /_\ \| |_| |_   _ _ __ ___   __ _ _ __  
|    // _ \ '_ \ / _ \| '__| __|  _  ||  _  | | | | '_ ` _ \ / _` | '_ \ 
| |\ \  __/ |_) | (_) | |  | |_| | | || | | | |_| | | | | | | (_| | | | |
\_| \_\___| .__/ \___/|_|   \__\_| |_/\_| |_/\__,_|_| |_| |_|\__,_|_| |_|
          | |                                                            
          |_|                                                            
========================================================================="""+version)
while True:
    print("----------\nWhat command is to be executed?\n----------\n")
    choise = input()
    if choise == "report":
        reportroutine()
    elif choise == "search":
        lookroutine()
    elif choise == "help":
        print("\nreport,search,list,delete or exit")
        press()
    elif choise == "list":
        listroutine()
    elif choise == "save":
        save()
    elif choise == "delete":
        deleteroutine()
    elif choise == "exit":
        quiteingabe = input("\nDo you really want to save and quit? <Yes or No> ")
        if quiteingabe.lower() == "yes":
            save()
            exit()
        else:
            print("returning...")
    else: print("\nYou have not chosen anything")