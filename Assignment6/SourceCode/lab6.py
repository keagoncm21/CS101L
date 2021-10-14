'''
CS 101 Lab
Program #6
Name: Keagon Madison
Email: kcmc2f@umkc.edu

PROBLEM:
A Caeser Cipher encrypter/decrypter must be made using multiple functions. The user must be able
to enter the amount of places the letters will shift and which letters/strings they want shifted.

ALGORITHM:
There is a main program loop that aks the user if they want to encode/decode a string or quit.
If the user chooses anything other than 1, 2, or Q, they get an error and it tries again.
If they want to encrypt a word or sentence, the program asks for the phrase and then asks for the number to shift by. 
Once the whole string is encrypted, it is outputted to the user.
If they want to decrypt a word or sentence, the program asks for the string and the number to shift by. 
Then, once the whole string is decrypted, it is ouputted to the user.
The program goes back to the main menu until the user selects quit(Q).

ERROR HANDLING:
For the selection phase, I added a while loop to check the user input to make sure it is valid.

OTHER COMMENTS:
There could probably be an added addition of encrypting/decrypting numbers and symbols as well later on.

'''

import string 

def Encrypt(string_text, int_key): 
    '''Caesar-encrypts string using specified key.'''
    new_string = ''
    alphabet = string.ascii_uppercase
    for i in string_text:
      if i in alphabet:
        if (string.ascii_lowercase.index(i.lower()) + 1 + int_key) > 25:
          alphcount = string.ascii_lowercase.index(i.lower()) + int_key - 26
          i = alphabet[alphcount]
        else:
          i = alphabet[string.ascii_lowercase.index(i.lower()) + int_key]
        new_string += i
      else:
        new_string += i
    return new_string




def Decrypt(string_text, int_key): 
  ''' Decrypts Caesar-encrypted string with specified key. ''' 
  new_string = ''
  alphabet = string.ascii_uppercase
  for i in string_text:
    if i in alphabet:
      if (string.ascii_lowercase.index(i.lower()) + 1 - int_key) > 25:
        alphcount = string.ascii_lowercase.index(i.lower()) - int_key - 26
        i = alphabet[alphcount]
      else:
        i = alphabet[string.ascii_lowercase.index(i.lower()) - int_key]
      new_string += i
    else:
      new_string += i
  return new_string
 
def Get_input(): 
  '''Interacts with user. Returns one of: '1', '2', '3', '4'.'''
  usr_input = input('Enter your selection: ')
  while usr_input not in ('Q', '1', '2'):
    print('Wrong selection. Try again.')
    usr_input = input('Enter your selection: ')
  return usr_input
 
1
def Print_menu():
  '''Prints menu. No user interaction. '''
  print('MAIN MENU:\n1) Encode a string\n2) Decode a string\nQ) Quit')
  
  
def main(): 
  Print_menu()
  Again = True 
  while Again: 
    print()
    Choice = Get_input() 
    if Choice == '1': 
      Plaintext = input("Enter (brief) text to encrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Ciphertext = Encrypt(Plaintext, Key)
      print("Encrypted:", Ciphertext) 
    elif Choice == '2': 
      Ciphertext = input("Enter (brief) text to decrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Plaintext = Decrypt(Ciphertext, Key)
      print("Decrypted:", Plaintext) 
   
    else: 
      print("Have an ordinary day.") 
      Again = False 
      
      
# our entire program:
if __name__ == '__main__':
  main() 
