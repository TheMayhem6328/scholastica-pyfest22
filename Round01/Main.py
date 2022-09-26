import re # Regex support

student_count = 5 # Assuming 5 for simplicity

counter = 0
while counter < student_count:
    temp = input("Enter student ID")
    if re.search("\d{1,4}[-]{1}\d{1,2}[-]{1}\d{1,4}", temp): # If input matches format `xxxx-xx-xxxx` (x being num)
        print("VALID")
    counter += 1