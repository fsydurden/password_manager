msp = input("Whats your master password?")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, psw = data.split("|")
            print(f"User: ${user} \nPassword: ${psw}\n\n")



def add():
    name = input("Account Name: \t")
    password = input("Password: \t")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|"+ password + "\n")

while True:
    mode = input("Would you like to add new password or list existing ones? (view/add or q to quit)").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode")

