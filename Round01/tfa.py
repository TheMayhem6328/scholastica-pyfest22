###### 2FA generation start

import random     # Import random num gen library
# Define function to search
def search(lst,trm):
    """A function to see if a given list (lst) has a given term (trm)

    Args:
        lst (list): The list to search `trm` in
        trm (str): The term to search in the list

    Returns:
        Bool: True if match found - False if not found
    """

    # Init 
    boolean = False
    for i in range(len(lst)):
        if str(lst[i]) == trm:
            boolean = True
            break
    return boolean


mail_list=[1,1,1,1,1]

##---------------------------------REMOVE EVERYTHING ABOVE WHEN IMPLEMENTING


### Declare a new list to store passwords in
tfa_list = []

### Re-initialise counter
counter = 0

### Generate password for each email
while counter != len(mail_list):
    #generating random number between 100000 and 999999
    temp=random.randint(100000,999999)
    # Check if it's already in list
    if search(tfa_list,temp):
        continue
    # Append built code to password list
    tfa_list.append(temp)

    # Increment counter
    counter += 1

print(tfa_list)

