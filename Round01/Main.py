import re # Regex support

student_count = 5 # Assuming 5 for simplicity

id_array = [] # Init array to store student IDs

counter = 0 # Counter init
while counter < student_count:
    temp = input("Enter student ID: ")
    if (
        re.search("\d{4}[-]{1}\d{2}[-]{1}\d{4}", temp) or # If input matches format `XXXX-XX-XXXX` (X being number)
        re.search("[0-9]{10}", temp) # Or if input matches format `XXXXXXXXXX` (X being number)
    ):
        if re.search("\d{4}[-]{1}\d{2}[-]{1}\d{4}", temp):
            temp = re.sub("[-]","",temp) # `XXXX-XX-XXXX` => `XXXXXXXXXX` (Remove hyphens [by replacing hyphen with empty char] basically)
        if not re.search("\d{4}[0]{2}\d{4}",temp): # If ID is `not` matching format `XXXX00XXXX`
            id_array.append(int(temp))
        counter += 1 # Increment counter
    else:
        print("Wrong format - it must match format 'XXXX-XX-XXXX' or 'XXXXXXXXXX' (10 numbers total)")

print(id_array)