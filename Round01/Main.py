### Init and import stuff
import re # Import regex library
student_count = 5 # Assuming 5 for simplicity
counter = 0 # Counter init

### Input
id_list = [] # Init list to store student IDs

### Loop n(Student) times
while counter < student_count:

    ## Init basic stuff
    flag = False # Flag init
    temp = input("Enter student ID: ")

    ## Ensure input matches desired format
    if (re.search("\d{4}[-]{1}\d{2}[-]{1}\d{4}", temp)): # If input matches format `XXXX-XX-XXXX` (X being number)
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
            
            # Add to ID list
            id_list.append(temp) # Add `id_input` to set
        
        # Increment counter
        counter += 1

    else:
        print("Wrong format - it must be only numbers and hyphens and must match format 'XXXX-XX-XXXX' or 'XXXXXXXXXX'")

### Sort (in ascending order) and output the list
id_list.sort()
print(id_list)