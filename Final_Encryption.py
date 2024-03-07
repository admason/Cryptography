# import date module from Class datetime:
from datetime import date

# User defined input according to the their birthday:
day, mon, year = int(input("Enter day: ")),int(input("Enter month: ")),int(input("Enter year: ")) 

# Assign user inputs to bday method:
bday = date(year, mon, day)                               

# Assign month number to 'shift' variable:
shift =  bday.month   

# Assign user's input message due for encryption (plaintext)
plaintext  = input("Enter plaintext message: ")         

# Optional text file input method, can be used with accompanying message.txt file
# To read from text from the message.txt file, direct src to location and remove hashtags
# src = open('C:/Users/.../message.txt','r')
# plaintext = src.read()

class Cipher:                                                           # Create the class Cipher:
    def __init__(self):                                                 # initiate the class
        def caesar_cipher(self,x):                                      # define the caesar_cipher function
            self.x = x
            self.shift = shift
######################################
            cipher = ''
            for char in self.x:
                if char.isdigit():
                    cipher += str(chr((ord(char) + shift-48) % 10 + 48))
                elif char == " ":
                    cipher += " "
                elif (char.isupper()):  
                    cipher += (chr((ord(char)+ shift - 65)%26  + 65))
                else:
                    cipher += chr((ord(char) + shift - 97)%26 +97)
            return cipher
            print('ciper',cipher)                                       # returns a list of enciphered elements
        ciph = list(map(lambda x: caesar_cipher(self,x), plaintext))    # call the ceasar cipher via a list comprehension generator
        ciphertext = ''                                                 # create empty string ready for population by the values produced by the for loop iteration
        for i in ciph:                                                  # for each element generated and stored in 'ciph'...
            ciphertext += str((i))                                      # append to the string known as 'ciphertext'
        print('ciphertext: ', ciphertext)                               # Print the ciphertext string
        
        def caesar_decipher(self, ciph):
            self.ciph = ciph
            self.shift = shift
            decipher = ''
            for char in self.ciph:
                if char.isdigit():
                    decipher+=  (chr((ord(char) - shift-48) % 10 + 48))
                elif char == " ":
                    decipher += " "
                elif char.isupper():
                    decipher +=chr((ord(char) - shift - 65) %26 +97)
                else:
                    decipher += chr((ord(char) - shift - 97)%26 + 97)
            return decipher

            
        deciph = list(map(lambda ciph: caesar_decipher(self, ciph), ciphertext))
        deciphertext = ''
        for k in deciph:
            deciphertext += str(k)
        print('deciphered: ', deciphertext)

Cipher()   
