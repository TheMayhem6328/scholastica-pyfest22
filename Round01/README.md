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

## Bonus Question (Quoted From [Official](README-Official.md))

Another masking algorithm is used to convert all numeric values to "#"s, alphabets to "%", and special characters to "¥" in the school ID.

What can you deduce about the format of the ID? Hence, how will this be beneficial for the school?

> We forgot to answer this on time :)

## Methodology

### Preamble

For this, we were given approximately 2.5 days (assignment was posted at 5pm GMT+6 on 26th September - deadline was on 28th September, 11:59pm GMT+6).

We spent the first day planning the code out - Zahir (TheMayhem6328) read the official instructions, made an objective summary out of it and outlined the checklist as seen in the below section. Zahir essentially directed the trajectory of this code, while Shabab primarily helped with testing and optimization.

### Idea

We took a more objective-oriented approach to this problem - we mostly followed the checklist we compiled (with slight deviation and addition every now and then).

### Validation

#### ID numbers

For validating `ID number` inputs, we used a set of various checks. All of these conditions had to pass:

- (Format check) Input matches format either `XXXX-XX-XXXX` or `XXXXXXXXXX` format.
- (Length check) Input had to be of exact length as format
- (Range Check) The first 4 digits of the input had to be within 2000 and 2022 - boundary inclusive

For checking format, we matched input with regex with the help of a built-in python library (`re`).

[Regular Expression](https://www.wikiwand.com/en/Regular_expression) (aka. `Regex` or `Regexp`) is a specialized statement which defines a precise search query. The python library `re` offers functions to match a string with regex and take actions based on it.  
We particularly used `re.search()` to return boolean `True` if the input conformed to the regex.  
A slight problem - this function would just _partially_ check the string - if the input was erroneous but had even one portion where it would match the regex, the function would return `True`  
(so string like `My name is XXXX-XX-XXXX`, `yyXXXXXXXXXXy` would be valid too)

This is where the length check comes in. If we additionally ensured that the length was exactly the length of the format, the user would have no way of typing in extra content.

We also had to make certain that the first 4 characters were between `2000` and `2022`. For that, we just took the first 4 characters (through string index range notation - something like `input[0:4]`) and did a normal number range check.

If all of this was valid, the ID number was dumped into a list. Otherwise, we just informed the user of the error and kept repeated input until user stopped giving us an erroneous input (without incrementing counter)

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
