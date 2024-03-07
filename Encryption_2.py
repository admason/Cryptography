# import date module from Class datetime
from datetime import date

# User defined input according to thier birthday:
day, mon, year = int(input("Enter day: ")),int(input("Enter month: ")),int(input("Enter year: ")) 

# Assign user inputs to bday method:                            
bday = date(year, mon, day)

# Assign month number to the 'shift' variable                                 
shift =  bday.month

# Assign user's input message due for encryption as 'plaintext'                                          
plaintext  = input("Enter plaintext message: ")

## Optional text file input method, can be used for testing the code,
## to active remove hashtag from the beginning of the next two lines
#src = open('C:/Users/.../message.txt','r')
#plaintext = src.read()                                                    

class Cipher:                                   # Create the class Cipher:

    def __init__(self):                         # initiate the class with self
        def caesar_cipher(self,x):              # define the caesar_cipher function
            self.x = x                          # Allocate 'x' to the Cipher class
            self.shift = shift                  # Allocate 'shift' variable to the Cipher class
            cipher = ''                         # create an empty string named 'cipher'
            for char in self.x:                 # for loop through the plaintext delivered via x variable in lambda within the generator
                if char.isdigit():              # if char (element of plaintext) is a digit, treat as next line:
                    cipher += str(chr((ord(char) + shift-ord('0')) % 10 + ord('0')))
                elif char == " ":               # if char is a space, treat as next line:
                    cipher += " "
                elif (char.isupper()):          # if char is a uppercase text, treat as next line:
                    cipher += (chr((ord(char)+ shift - ord('A'))%26  + ord('A')))
                elif char.islower():            # if char is a lowercase text, treat as next line:
                    cipher += chr((ord(char) + shift - ord('a'))%26 +ord('a'))
                else:                           
                    cipher += chr(ord(char) + shift)    # if char is a symbol !"£$%^&*(), treat as next line: 
            return cipher                       # returns a list of enciphered elements
            print('cipher',cipher)                                       
        ciph = list(map(lambda x: caesar_cipher(self,x), plaintext))    # call the ceasar cipher via a list comprehension generator and deliver to 'ciph'
        ciphertext = ''                                                 # create empty string ready for population by the values produced by the for loop iteration
        for i in ciph:                                                  # for each element generated and stored in 'ciph'...
            ciphertext += str((i))                                      # append to the string known as 'ciphertext'
        print('\n ciphertext: \n', ciphertext)                          # Print the ciphertext string

      # caesar_decipher is the inverse of ceasar_cipher.  
        def caesar_decipher(self, ciph):            # This time pass 'ciph' as an arguement
            self.ciph = ciph                        # Allocate 'ciph' to the Cipher class
            self.shift = shift                      # Allocate 'shift' to the Cipher class
            decipher = ''                           # create an empty string named 'decipher'
            for char in self.ciph:                  # for loop through the 'ciphetext' delivered via 'ciph' variable in lambda within the generator
                if char.isdigit():                  # if char (element of plaintext) is a digit, treat as next line, this time subtract the 'shift' value:
                    decipher+=  (chr((ord(char) - shift - ord('0')) % 10 + ord('0')))
                elif char == " ":
                    decipher += " "
                elif char.isupper():
                    decipher +=chr((ord(char) - shift - ord('A')) %26 +ord('A'))
                elif char.islower():
                    decipher += chr((ord(char) - shift - ord('a'))%26 + ord('a'))
                else:
                    decipher += chr(ord(char) - shift) 
            return decipher

        deciph = list(map(lambda ciph: caesar_decipher(self, ciph), ciphertext)) # call the ceasar_decipher via a list comprehension generator and deliver to 'decipher'
        deciphertext = ''                                           # create empty string ready for population by the values produced by the for loop iteration
        for k in deciph:                                            # for each element generated and stored in 'deciph'...
            deciphertext += str(k)                                  # append to the string known as 'deciphertext'
        print('\n\t deciphered: \n\t', deciphertext)                # Print the deciphertext string


Cipher()                                                            # Activate Class Cipher() with arguements to be input by user.
