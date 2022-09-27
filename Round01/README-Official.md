# Round 1 - CRISIS

## Scenario

Scholastica Uttara’s email database has been accidentally deleted due to a software failure. It is required to be restored as soon as possible. However, due to the software failure, the remote database cannot be accessed directly and hence the application cannot be used to input or output any sort of data. to revert this crisis, the use of a python program is suggested by the authority.

## Primary Objectives - Official

1. Declare constants to make a **reasonable estimate of the total number** of students in the school
2. Take the inputs of the ID numbers of the estimated amount of students
3. Form the email in the format
     - First Half: ID number
     - Second Half : "@scholastica.online"
     - E.g. "2014070017@scholastica.online"
4. Generate a **random** password for every email (does _not_ need to be unique for every email)
5. The password must be **at least 8 characters** long
6. Display the emails and their corresponding password
7. Validate the inputs
8. Take an input of the email and check whether the entry matches with the email formed
9. Make the entire program run in a **continuous loop** which ends on command

## Bonus Objectives - Official

### The EXTENDED program

1. Store all the ID numbers, in **ascending** order
2. If the same ID is repeated, an input of a different ID should be taken
3. Make the passwords (in _Primary Objectives - Point 4_) unique
4. The password must have at least 1 uppercase letter, 3 lowercase letters and 2 digits
5. The password must not contain any special characters
6. The ID numbers containing a "00" after the year of registration - e.g. `2017-00-0024` - must be omitted as they are students of SRM
7. The passwords of the omitted ID numbers should also be deleted (?)
8. Each email must be given an unique 6 digit numeric two-factor authentication code
9. Be converted to a reusable procedure

## Bonus Question

> This question is to be answered in the Google Doc

Another masking algorithm is used to convert all numeric values to "#"s, alphabets to "%", and special characters to "¥" in the school ID.

What can you deduce about the format of the ID? Hence, how will this be beneficial for the school?

## Submission Instructions

- You have to solve the program and copy paste the entire program into a doc file OR upload the python file directly. (The latter is more preferred)
- You have to solve the program in your IDLE/Interpreter and compile them into the same doc file.  
(You must reduce the number of iterations for this task)
- If you are attempting the program solo, rename the doc file in the format `Name_Grade_ISPF1`
- If you are attempting the program in a duo, rename the doc file in the format `Name1_Name2_Grade_ISPF1`
- Upload the files into the classroom assignment