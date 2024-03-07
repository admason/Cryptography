# Cryptography
Cryptography based programming
# Cipher 1: Simple Ceasar Cipher

Running the code:
Upon running the code, the user will be prompted to enter their birthday in the form of day, month and year converted to integer data types.

day, mon, year = int(input("Enter day: ")),int(input("Enter month: ")),int(input("Enter year: "))  
The useful value here is the month.
The date module is used:
bday = date(year, mon, day)    
Which has the inbuilt protocol for checking that each part of the date is valid.
For example, if the use inputs a day greater than 31, the date Class will respond with a ValueError: day is out of range. Since no months have more than 31 days.
Even entering 30th February will result in: ValueError: day is out of range for month.
Likewise, entering month =13 or more will result in:
ValueError: month must be in 1..12
The range of inputs are already covered with the imported Class of date.


The date Class does not discriminate between value length, if the day is entered as dd or d, such as ‘01’ or ‘1’.
For month: mm or m, such as ‘02’ or ‘2’.
Which is important as the code use the month value as the shift key, or known as ‘shift’ in this code:
This means a user need not worry about their preferred input of date format, so long as the date exists in the Gregorian Calendar.


Once the date has cleared the user is prompted for their plaintext message:
Enter plaintext message:
Which may accept number, symbol and both uppercase and lowercase letters.


For simplicity, forcing the shift of one position in the ASCII table, by setting month =1
Day = 1
Month = 1
Year = 2010

The code only needs the month = 1 to produce an enciphered text by shifting each element by one position up the ASCII table.
Returns


Whereby ‘a’ will shift the ASCII value forward by one position to ‘b’
Whereby ‘b’will shift the ASCII value forward by one position to ‘c’


Whereby ‘b’ will shift the ASCII value backward by one position to ‘a’
Whereby ‘c’ will shift the ASCII value backward by one position to ‘b’

The deciphered offers a means of checking the ciphertext will return to the original plaintext.


TESTING:
This may be furthermore checked by directing the plaintext to read from the message.txt file,
by using the code 
# src = open('C:/Users/.../message.txt','r')     (Replacing \ for /)
# plaintext = src.read()

The deciphered text should be the inverse of the plain text and the python code returns. 
	 deciphered: 
	 0123456789
Uppercase alphabet
ABCDEFGHIJKLMNOPQRSTUVWXYZ
Lowercse alphabet
abcdefghijklmnopqrstuvwxyz

