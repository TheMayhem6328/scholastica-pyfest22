####### Import required libraries
import re         # Import regex library
import random     # Import random num gen library



###### Master procedure start
def studentMail(student_count = 5):
    """This procedure is there to make email and auth info based on inputted student IDs 

    Arg:
        student_count (int, optional): Number of inputs to take. Defaults to 5. Input loop can be terminated by pressing `Ctrl+C` on keyboard

    Returns:
        Prints out a psuedo-table of emails, their unique password and their 2FA code
    """

    ### Define function to search (will be extensively used later)
    def search(scanList: list,scanTerm):
        """A function to see if a given list (lst) has a given term (trm)

        Args:
            scanList (list): The list to search the given term in
            scanTerm (any): The term to search in the list

        Returns:
            Bool: True if match found - False if not found
        """

        # Init boolean
        boolean = False
        for i in range(len(scanList)):
            if str(scanList[i]) == str(scanTerm):
                boolean = True
                break
        return boolean


    ###### Input, validation, collection and organisation start

    ### Initialize variables
    counter = 0 # Counter init
    id_list, mail_list = [], [] # Init list to store student ID numbers and mails

    ### Try-except statements so that user can terminate this loop by `Ctrl+C`
    try:
        ### Loop n(Student) times
        while counter < student_count:

            ## Init basic stuff
            flag = False # Flag init
            temp = input("Enter student ID: ")

            ## Ensure input matches desired format
            if re.search("20[0-2]\d{1}[-]\d{2}[-]\d{4}", temp): # If input matches format `XXXX-XX-XXXX` (X being number)
                if len(temp) == 12 and int(temp[0:4]) >= 2000 and int(temp[0:4]) <= 2022: 
                    # If length of input is 12 and the first 4 digit is within 2000 and 2022
                    flag = True
            if re.search("\d{10}", temp): # If input matches format `XXXXXXXXXX` (X being number)
                if len(temp) == 10 and int(temp[0:4]) >= 2000 and int(temp[0:4]) <= 2022:
                    # If length of input is 10 and the first 4 digit is within 2000 and 2022
                    flag = True
            # I did this nested loop because otherwise the ID could be larger than the desired size and still be valid

            ## Do processing and input dump only if it passed through above check 
            if flag:

                # Remove hyphens from ID if not already in form `XXXXXXXXXX`
                if re.search("\d{4}[-]{1}\d{2}[-]{1}\d{4}", temp):
                    temp = re.sub("[-]","",temp) # `XXXX-XX-XXXX` => `XXXXXXXXXX`

                # Duplicate check
                if search(id_list,temp):
                    print("Value exists")
                    continue

                # Append to ID list (yes - even `XXXX00XXX` ones so that they can't be duplicated either)
                id_list.append(temp)

                # Don't append ID list if ID is in format `XXXX00XXXX` - but do increment counter
                if not re.search("\d{4}[0]{2}\d{4}",temp): # If ID does `not` match format `XXXX00XXXX`


                    ###### Email generation and verification start

                    # Add to ID list, append `@scholastica.online` to ID to form email and print out email
                    temp += "@scholastica.online"
                    mail_list.append(temp) # Add `id_input` to set
                    print("Mail generated: " + temp)

                    # Input and validate email - bug user if input is wrong
                    while True:
                        temp2 = input("Repeat email:   ")
                        if temp == temp2:
                            break
                        else:
                            print("Input email did not match generated email\n(Hint: It's just the ID without hyphens, suffixed with '@scholastica.onine')")

                    ###### Email generation and verification end


                # Let user know that the ID was skipped
                else:
                    print("Format matches Mirpur ID (matches format XXXX00XXXX or XXXX-00-XXXX)- skipping...")

                # Increment counter
                counter += 1
                print("") # For output formatting reasons - serves no real purpose

            else:
                print(
                    "Wrong format - it must be only numbers and hyphens and must match format 'XXXX-XX-XXXX' or 'XXXXXXXXXX'"
                    + "\nAdditionally, the first 4 digits must be within 2000 and 2022 (Boundaries Inclusive)"
                )
    except KeyboardInterrupt:
        print(f"\n\n!! Input loop terminated by user. {counter} iterations done !!\n")

    ### Sort (in ascending order)
    mail_list.sort()

    ###### Input, validation, collection and organisation end



    ###### Password generation start

    ### Declare a new list to store passwords in
    pwd_list = []

    ### Re-initialise counter
    counter = 0

    ### Generate password for each email
    while counter != len(mail_list):

        # Init temp list
        temp_list = []

        # Convenience variables for functions
        tla = temp_list.append
        rnr = random.randint

        # Generate 2 numbers and dump them to list 
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

    ###### Password generation end


    ###### 2FA generation start

    ### Declare a new list to store passwords in
    tfa_list = []

    ### Re-initialise counter
    counter = 0

    ### Generate password for each email
    while counter != len(mail_list):

        # Generate random number between 100000 and 999999
        temp = str(random.randint(100000,999999))

        # Check if it's already in list
        if search(tfa_list,temp):
            continue

        # Otherwise append to password list and increment counter
        else:
            tfa_list.append(temp)
            counter += 1

    ###### 2FA generation end


    ###### Fancy output start

    print("         Mail                 |   Pwd    |  OTP  ")
    print("=================================================")
    for i in range(len(mail_list)):
        print(mail_list[i],"|",pwd_list[i],"|",tfa_list[i])

    ###### Fancy output end

###### Master procedure end



studentMail()