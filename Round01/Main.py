###### Init and import stuff
import re # Import regex library
student_count = 5 # Assuming 5 for simplicity
counter = 0 # Counter init


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

            # Duplicate check check
            flag2 = 0 # Will be more than 0 if duplicate found

            # Compare each element of ID list with ID input
            for x in id_list:
                if x == temp:
                    flag2 += 1

            # Repeat loop (without appending list or incrementing counter)
            if flag2 > 0:
                print("Value exists")
                continue
            

            ###### Email generation and verification start

            # Add to ID list (And append `@scholastica.online` to ID to form email)
            temp += "@scholastica.online"
            id_list.append(temp) # Add `id_input` to set

            # Infinite loop to keep asking user until user inputs right email
            while True:
                temp2 = input("Enter email: ")
                if temp2 == temp:
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

print(id_list)