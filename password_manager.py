from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


write_key()
'''


def load_key():
    return open("key.key", "rb").read()


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            user, pwd = line.rstrip().split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(pwd.encode()).decode())


def add():
    name = input("Account Name : ")
    pwd = input("Password : ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add new passwords or view existing ones (view/add), or q to quit? ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
