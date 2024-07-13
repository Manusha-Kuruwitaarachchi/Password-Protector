from cryptography.fernet import Fernet



def write_key(): #used to generate the key
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file: #create a file called key.key in write in bit mode
        key_file.write(key) 
        
write_key()

def load_key(): #used to load the created key
    file = open("key.key", "rb") #opening the file in read bit mode
    key = file.read()
    file.close()
    return key

master_password = input("What is the master password? ")
key = load_key() + master_password.encode() #loading the key and adding it to the master_password and creating the key
fer = Fernet(key) #encode takes the string and turns into bytes


def view ():
    with open("password.txt", "r") as f: #when you use "with" u don't have to manually close the file python will automatically do it for u 
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",fer.decrypt(passw.encode()).decode())
            
            
def add():
    name = input("Account Name: ")
    password = input("Password: ")
    
    
    with open("password.txt", "a") as f: #when you use "with" u don't have to manually close the file python will automatically do it for u 
        f.write(name + "|" + fer.encrypt(password.encode()).decode() +"\n")


while True:
    
    mode = input("Would you like to add a new password or view existing ones (a,v) and press q to quit: ").lower()
    if mode == "q":
        break
    
    if(mode == "v"):
        view()
    elif (mode == "a"):
        add()
    else:
        print("Invalid mode.")
        continue #bring back to the top of the while loop