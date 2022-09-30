#DEBUG THE CODE

import random
import secrets
import hashlib
def cipher(choose, key, arg = 5):
    global num1
    count = 5
    num = str(random.randint(100,999))
    encrypted_message = ""
    decrypted_message = ""
    validatorkey = input("Please enter your unique key to continue: ")
    while validatorkey != key:
        count = count - 1
        print(f"Tries remaining: {count}")
        validatorkey = input("Please enter the correct unique key to continue: ")
        if count < 2 and validatorkey != key:
            print("ACCESS DENIED")
            exit()
    flag = True
    while flag:
        for k in range(arg):
            if choose == "E" or choose == "e":
                unencrypted = input("Enter message to be encrypted: ")
                for i in unencrypted:
                    encrypted_character = ord(i) + 5
                    encrypted_character = chr(encrypted_character)
                    encrypted_message = encrypted_message + encrypted_character
                encrypted_message = (num.join(map(str, encrypted_message)))
                print("Encrypted Message: ",encrypted_message)
                encrypted_message = ""
            if choose == "D" or choose == "d":
                decrypted = input("Enter encrypted message: ")
                for i in decrypted.replace(decrypted[1:4],""):
                    decrypted_character = ord(i) - 5
                    decrypted_character = chr(decrypted_character)
                    decrypted_message = decrypted_message + decrypted_character
                print("Decrypted Message: ",decrypted_message)
                decrypted_message = ""
        exterminator = int(input("Do you want input you'r set of messages again?(in case you made a\n (1) Yes \n (2) No \nYour response: "))
        while exterminator != 1 and exterminator != 2:
            exterminator = int(input("Do you want input you'r set of messages again?(in case you made a mistake)\n [1] for Yes \n [2] for No \nYour response: "))
        if exterminator == 2:
            flag = False

choose = input("Do you want to (e)encrypt or (d)decrypt? ")
arg = int(input("How many messages do you want to enter? "))
key = hashlib.sha256(secrets.token_urlsafe(32).encode())
key = key.hexdigest()
print("The unique key is: ",key)
cipher(choose, key, arg)