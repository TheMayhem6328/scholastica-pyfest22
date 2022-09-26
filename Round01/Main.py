###### Init and import stuff
import re         # Import regex library
import random     # Import random num gen library
student_count = 3 # Assuming 2 for simplicity
counter = 0       # Counter init

# Define function to search (will be extensively used later)
def search(lst: list,trm: str):
    """A function to see if a given list (lst) has a given term (trm)

    Args:
        lst (list): The list to search `trm` in
        trm (str): The term to search in the list

    Returns:
        Bool: True if match found - False if not found
    """

    # Init boolean
    boolean = False
    for i in range(len(lst)):
        if str(lst[i]) == trm:
            boolean = True
            break
    return boolean


###### Input, validation, collection and organisation start

### Input
id_list = [] # Init list to store student IDs

### Loop n(Student) times
while counter < student_count:

    ## Init basic stuff
    flag = False # Flag init
    temp = input("Enter student ID: ")

    ## Ensure input matches desired format
    if re.search("\d{4}[-]{1}\d{2}[-]{1}\d{4}", temp): # If input matches format `XXXX-XX-XXXX` (X being number)
        if len(temp) == 12: # If length of input is 12
            flag = True
    if re.search("\d{10}", temp): # If input matches format `XXXXXXXXXX` (X being number)
        if len(temp) == 10: # If length of input is 10
            flag = True
    # I did this nested loop because otherwise the ID could be larger than the desired size and still be valid

    ## Do processing and input dump only if it passed through above check 
    if flag:

        # Remove hyphens from ID if not already in form `XXXXXXXXXX`
        if re.search("\d{4}[-]{1}\d{2}[-]{1}\d{4}", temp):
            temp = re.sub("[-]","",temp) # `XXXX-XX-XXXX` => `XXXXXXXXXX`

        # Don't append ID list if ID is in format `XXXX00XXXX` - but do increment counter
        if not re.search("\d{4}[0]{2}\d{4}",temp): # If ID does `not` match format `XXXX00XXXX`

            # Duplicate check
            if search(id_list,temp):
                print("Value exists")
                continue
            
            id_list.append(temp)
            

            ###### Email generation and verification start

            # Add to ID list (And append `@scholastica.online` to ID to form email)
            temp += "@scholastica.online"
            id_list.append(temp) # Add `id_input` to set

            while True:
                temp2 = input("Enter email: ")
                if search(id_list,temp2):
                    break
                else:
                    print("Input email did not match generated email\n(Hint: It's just the ID without hyphens, suffixed with '@scholastica.onine')")

            ###### Email generation and verification end


        # Let user know that the ID was skipped
        else:
            print("Format matches Mirpur ID - skipping...")
        
        # Increment counter
        counter += 1
        print("") # For output formatting reasons - serves no real purpose

    else:
        print("Wrong format - it must be only numbers and hyphens and must match format 'XXXX-XX-XXXX' or 'XXXXXXXXXX'")

### Sort (in ascending order)
id_list.sort()

###### Input, validation, collection and organisation end



###### Password generation start

### Declare a new list to store passwords in
pwd_list = []

### Re-initialise counter
counter = 0

### Generate password for each email
while counter != len(id_list):

    # Init temp list
    temp_list = []

    # Convenience variables for functions
    tla = temp_list.append
    rnr = random.randint

    # Generate 3 numbers and dump them to list 
    tla(str(rnr(0,9)))
    tla(str(rnr(0,9)))

    # Generate 2 ASCII nums (for `UPPERCASE`` letter), convert them to characters and dump them to list
    tla(chr(rnr(65,90)))
    tla(chr(rnr(65,90)))
    tla(chr(rnr(65,90)))
    
    # Generate 3 ASCII nums (for `lowercase`` letter), convert them to characters and dump them to list
    tla(chr(rnr(97,122)))
    tla(chr(rnr(97,122)))
    tla(chr(rnr(97,122)))

    # Ensure characters don't follow a pattern
    random.shuffle(temp_list)

    # Declare a utility variable
    temp = ""

    # Build a string
    for x in temp_list:
        temp += x

    # Check if it's already in list
    if search(pwd_list,temp):
        continue

    # Append built string to password list
    pwd_list.append(temp)

    # Increment counter
    counter += 1

print(pwd_list)

print(id_list)

###### Password generation end