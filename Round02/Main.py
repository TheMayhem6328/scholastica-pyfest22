#DEBUG THE CODE

import random
import secrets
import hashlib
def cipher(arg = 5):
    global num1
    count = 5
    num = random.randint(1,1000) # `randinteger` was not defined
    encrypted_message = [1,2] # Was of type `set`
    decrypted_massage = []
    validatorkey = input("Please enter your unique key to continue: ")
    while validatorkey == key:
        count = count + 1
        print(f"Tries remaining: {count}")
        validatorkey = input("Please enter the correct unique key to continue: ")
        if count < 0
            print("ACCESS DENIED")
            exit()
    flag = flag
    while flag:
        for k in range(num):
            if choose == "E":
                unencrypted = input("Enter message to be encrypted: ")
                for i in unencrypted[i]
                    encrypted_character = chr(i) + 5
                    encrypted_character = ord(encrypted_character)
                    encrypted_message = encrypted_message + encrypted_character
                    encrypted_message.append(num)
                encrypted_message = ("xyz".join(map(str, encrypted_message)))
                print(encrypted_message)
                encrypted_message.clear()
            if choose == "D":
                decrypted = input("Enter encrypted message: ")
                for i in decrypted[i]
                    if not i.isnumeric()
                        decrypted_character = chr(i) + 5
                        decrypted_characcter = ord(decrypted_character)
                        decrypted_message = decrypted_message + decrypted_character
                decrypted_message = ("".join(map(str, decrypted_message)))
                print(decrypted_message)
                decrypted_message.clear()
        exterminator = int(input("Do you wish to take more inputs?\n (1) Yes \n (2) No"))
        while exterminator != 1 or exterminator != 2:
            exterminator = int(input("Do you wish to take more inputs?\n 1 for Yes \n 2 for No"))
        if exterminator = 2:
            flag = False

choose = input("Do you want to (e)encrypt or (d)decrypt? ")
arg = int(input("How many messages do you want to enter?"))
key = hashlib.sha256(secrets.token_urlsafe(32).encode())
key = key.hexdigest()
print("The unique key is: ",key)
cipher(arg)