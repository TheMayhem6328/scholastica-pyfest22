# Round 1 - CRISIS

## Objective (`Primary` & `Extended` Combined )

> Make sure to do validation wherever possible

Make a program that takes `n` amount of ID numbers (`n` being number of students in school [estimate] ) as input.  
ID numbers have to be sorted in ascending order. They can't be repeated - repetitive inputs should be discarded. They have to match the format `XXXX-XX-XXXX`.

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

ID numbers matching the format `XXXX-00-XXXX` have to be omitted - i.e. the email, password and OTP for those emails will have to be deleted (AFTER input is done; suppose user inputted 40 SRM IDs within 1500 - only 1460 of them will stay, after SRM ones have been deleted).

Later on, print them (the set of email-password-OTP triplets) out

Lastly, make it a procedure (not a function - no need to assign `return` values) so that it can be recalled at any time.

## Bonus Question (Quoted From [Official](README-Official.md))

Another masking algorithm is used to convert all numeric values to "#"s, alphabets to "%", and special characters to "¥" in the school ID.

What can you deduce about the format of the ID? Hence, how will this be beneficial for the school?