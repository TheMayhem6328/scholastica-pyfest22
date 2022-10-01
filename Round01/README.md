# Round 1 - [CRISIS](README-Official.md)

## Objective (`Primary` & `Extended` Combined )

> Make sure to do validation wherever possible

Make a program that takes `n` amount of ID numbers (`n` being number of students in school [estimate] ) as input.  
ID numbers have to be sorted in ascending order. They can't be repeated - repetitive inputs should be discarded (they don't add to counter). They have to match the format `XXXX-XX-XXXX`.

ID numbers matching the format `XXXX-00-XXXX` have to be omitted (they do add to the counter - (suppose user inputted 40 SRM IDs within 1500 - only 1460 of them will stay, after SRM ones have been deleted).

Then, form an email out of them by stripping the hyphens off ( i.e. convert the format `XXXX-XX-XXXX` to `XXXXXXXXXX`) and suffixing it with `@scholastica.online`  
(E.g `2013-06-0031 ==> 2013060031@scholastica.online`)

After that, passwords have to be generated for each email.  
The password has to meet these criteria:

- Alphanumeric
- 8 characters long
- 1 uppercase letter
- 3 lowercase letters
- 2 digits / numbers
- Unique for each ID

A unique OTP (6 digit numeric code) for each email has to be generated too.

Later on, print them (the set of email-password-OTP triplets) out

Lastly, make it a procedure (not a function - no need to assign `return` values) so that it can be recalled at any time.

## Bonus Question

### Question (Quoted From [Official](README-Official.md))

Another masking algorithm is used to convert all numeric values to "#"s, alphabets to "%", and special characters to "¥" in the school ID.

What can you deduce about the format of the ID? Hence, how will this be beneficial for the school?

### Answer (by Taz2040)

> We forgot to submit this answer this on time due to last-moment stress :)

All the emails would end up being `##########¥%%%%%%%%%%%¥%%%%%%`.
This means that all the school emails have a very specific format,where it starts with a list of numeric values,followed by a special characters then a list of alphabets a special character and then another list of alphabets.

The school can easily change the list of the part of email that contains alphabets to anything else to generate new type of email

## Methodology

### Preamble

For this, we were given approximately 2.5 days (assignment was posted at 5pm GMT+6 on 26th September - deadline was on 28th September, 11:59pm GMT+6).

We spent the first day planning the code out - Zahir (TheMayhem6328) read the official instructions, made an objective summary out of it and outlined the checklist as seen in the below section. Zahir essentially directed the trajectory of this code, while Shabab (Taz2040) primarily helped with testing and optimization. Also, since this was Shabab's first time using git and GitHub, we took out time to mess around with a git-centric workflow.

### Idea

We took a more objective-oriented approach to this problem - we mostly followed the checklist we compiled (with slight deviation and addition every now and then). We mostly used descriptive variable names named in mostly `snake_case`, but some in `camelCase` too (just a preference thing, really).

### Validation

#### ID numbers

For validating `ID number` inputs, we used a set of various checks. All of these conditions had to pass:

- (Format check) Input matches format either `XXXX-XX-XXXX` or `XXXXXXXXXX` format.
- (Length check) Input had to be of exact length as format
- (Range Check) The first 4 digits of the input had to be within 2000 and 2022 - boundary inclusive

For checking format, we matched input with regex with the help of a built-in python library (`re`).

[Regular Expression](https://www.wikiwand.com/en/Regular_expression) (aka. `Regex` or `Regexp`) is a specialized statement which defines a precise search query. The python library `re` offers functions to match a string with regex and take actions based on it.  
We particularly used `re.search()` to return boolean `True` if the input conformed to the regex.

A slight problem - this function would just _partially_ check the string - if the input was erroneous but had even one portion where it would match the regex, the function would return `True` (so strings like `My name is XXXX-XX-XXXX` and `yyXXXXXXXXXXy` would be valid too)

This is where the length check comes in. If we additionally ensured that the length was exactly the length of the format, the user would have no way of typing in extra content.

We also had to make certain that the first 4 characters were between `2000` and `2022`. For that, we just took the first 4 characters (through string index range notation - something like `input[0:4]`) and did a normal number range check.

If all of this was valid, the ID number was dumped into a list. Otherwise, we just informed the user of the error and kept repeated input until user stopped giving us an erroneous input (without incrementing counter). If it matched format `XXXX-00-XXXX`, then we did increment the counter but never processed it (we isolated `id_list` and `mail_list` - we put all valid and unique ID numbers into `id_list` for duplication checking, but made emails [by just appending `@scholastica.online` to non-`XXXX-00-XXXX` IDs and appending them to `mail_list`] out of them _only_ if they didn't match the aforementioned format).

#### Duplication Check

For every input we took or value we generated (basically any set of values that had a common purpose and needed to be unique) we stored it to a relevant list (For example `id_list` for ID input). We also made a function `search()` to check for duplicate. It took 2 parameters - `scanList`, the list we were going to check duplicate in, and `scanTerm`, the term (anything that could be converted to a string). It returned boolean `True` if `scanTerm` was found in `scanList`.

We needed three lists to be unique - `id_list` (ID numbers inputted), `pwd_list` (passwords generated) , and `tfa_list` (2FA codes generated). All three of these had some randomness to them, and while the latter two list had low chances of generating duplicated (For instance, roughly `2.18e14` combinations are possible for an element of `pwd_list`), but we couldn't allow even luck to interfere.

### Value Generation

#### Password

To make unique passwords, we extensively relied on the library `random` and on inbuilt functions `str()` and `chr()`. We made a list `temp_list` to store generated characters and then built a string out of its elements.

We needed at least an 2 numbers, 3 lowercase letters and an uppercase letter. Numbers were easy - we used the function `random.randint()` to generate a two random integers between 0 to 9 (basically two individual random 1-digit numbers), converted them to strings, and appended them to `temp_list`.

For generating the letters, it is essential to know how [ASCII encoding](https://www.wikiwand.com/en/ASCII) works. In short, computers don't understand `ABC` - they only understand numbers. To allow a computer to deal with numbers, a mapping table mapping numbers to characters (and some instructions too) was developed. See the image below for a set of mappings.

![ASCII Table](ASCII_Table.gif)

As per this standard of mapping, decimal values `65 - 90` translate to characters `A-Z` (uppercase letter), and `97-122` translate to `a-z` (lowercase letters).

Having this in mind, and also remembering the fact that we have a function to generate random integers within any range we want (`random.randint()`), what if we were to translate random number to its ASCII counterpart?

We did exactly that for the letters - we used the inbuilt function `chr()` for this. Function `chr()` took an integer as a parameter and converted it to its ASCII character. For example, `chr(69)` would return `"E"`. Since we needed randomness, we ran `chr(random.randint(x,y))`, `x` being the lower bound of the range (`65` for uppercase letters, `97` for lowercase letters), and `y` being the upper bound of the range (`90` for uppercase letters, `122` for lowercase letters).

We made 3 lowercase letters and 3 uppercase letters (extra 2 to fill the 8 character requirement mentioned in the [official guideline](README-Official.md)) and appended them to `temp_list`.

Since we generated exactly the characters we wanted, we ruled out the possibility of dealing with special characters. We were left with one problem now - the password was not as random was we wanted.

The password was in format `XXYYYZZZ` - `X` being numbers, `Y` being uppercase letters and `Z` being lowercase letters. We didn't want the password to conform to this pattern. Remember that we stored all of our characters in `temp_list`? We had a function defined in `random` that could shuffle the indexes of each elements in a list. Function `random.shuffle()` accepted the name of a list as a parameter and shuffle the elements in the provided list. We used this on `temp_list` and randomized that pattern (and therefore broke the aforementioned pattern).

After that, we built a string out of it by initializing another utility variable `temp` as an empty string, running `for x in temp_list: temp += x` (would take each element in `temp_list` and add that to `temp` sequentially). We would check if `temp` was already there in `pwd_list`, append `temp` to `pwd_list` if it was not there already, reinitialize `temp` and repeating as many times as `len(mail_list)` (the numbers of emails in `mail_list`).

#### 2FA Code

This was much easier than making a full password. We generated a number between 100000 and 999999, converted that to a string, checked whether it was already in `tfa_list`, appended it to the list if it was unique and repeated as many times as `len(mail_list)`.

### Aftermath

We were now left with 3 lists of the same length:

- `mail_list` (Stored mail)
- `pwd_list` (Stored passwords)
- `tfa_list` (Stored 2FA codes)

We just outputted them each in a line by referring to them by index number. There we go - the program was complete! We converted this to a procedure and called it when needed.

## Checklist We Followed Through For This

- [x] Input IDs, validate and arrange input as ascending array
  - [x] Make constant for student count
  - [x] Take ID numbers as input
  - [x] Validate ID input (both `XXXXXXXXXX` and `XXXX-XX-XXXX` work)
  - [x] Disallow duplicate ID input
  - [x] Omit IDs matching format `XXXX-00-XXXX`
  - [x] Dump inputs to an array
  - [x] Sort array as ascending
- [x] Generate email
  - [x] Append `@scholastica.online` to each element of ID array
  - [x] Take input of email and verify it against generated data (for each email)
- [x] Generate password
  - [x] Make unique
  - [x] Ensure password meets at least these criteria:
    - [x] Alphanumeric
    - [x] 8 characters long
    - [x] 1 uppercase letter
    - [x] 3 lowercase letters
    - [x] 2 digits / numbers
- [x] Generate yet another password ("2FA Code")
  - [x] Ensure it's only a 6-digit number
- [x] Output them in a clean manner
- [x] Convert the entire process into a procedure (function with no `return` basically)

## Known Bugs

- None known as of writing 🥳
