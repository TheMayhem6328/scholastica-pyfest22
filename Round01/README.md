# Round 1 - CRISIS

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

## Checklist

- [x] Input IDs, validate and arrange input as ascending array
  - [x] Make constant for student count
  - [x] Take ID numbers as input
  - [x] Validate ID input (both `XXXXXXXXXX` and `XXXX-XX-XXXX` work)
  - [x] Disallow duplicate ID input
  - [x] Omit IDs matching format `XXXX-00-XXXX`
  - [x] Dump inputs to an array
  - [x] Sort array as ascending
- [ ] Generate email
  - [ ] Append `@scholastica.online` to each element of ID array
- [ ] Generate password
  - [ ] Make unique
  - [ ] Ensure password meets at least these criteria:
    - [ ] Alphanumeric
    - [ ] 8 characters long
    - [ ] 1 uppercase letter
    - [ ] 3 lowercase letters
    - [ ] 2 digits / numbers
- [ ] Generate yet another password ("2FA Code")
  - [ ] Ensure it's only a 6-digit number
- [ ] Output them in a clean manner
  - [ ] (TBA)
- [ ] Convert the entire process into a procedure (function with no `return` basically)
- [ ] (Complete checklist)