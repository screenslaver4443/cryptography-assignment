# Cryptopgraphy assignment
# Ver 1.1
# By Nikolai

#Defining dictionaries.
dic1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}
dic2 = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z'
}
swapdic = {
    'a': 'd',
    'b': 'f',
    'c': 'z',
    'd':'a',
    'e': 'y',
    'f':'b',
    'g': 'h',
    'h':'g',
    'i': 'p',
    'j': 'k',
    'k':'j', 
    'l': 'x',
    'm': 'n',
    'n':'m',
    'o': 's',
    'p': 'q',
    'q':'p',
    'r': 't',
    's': 'u',
    't':'r',
    'u':'s',
    'v': 'w',
    'w':'v',
    'x':'l',
    'y':'e',
    'z':'c'
}

def messtolist(text):
	listie1 = []
	for i in text:
		listie1.append(i)
	return(listie1)


def encryptshift(text, key):
    rtext = '' # defining the variable so that python doesn't get angry and throw a hissy fit.
    for i in text:
        i = i.lower() #Setting all the characters to lower case so that the dictionary can handle it.
        if i == ' ': 
            rtext += ' ' 
            #If the character is a space DON'T try to encrypt it.
        else:
            textn = dic1[i] #Converts the letter to a number using the first dictionary.
            int(textn) #Converts the outputted string to a integer.
            textn += key #Adds the key to the converted character thus shifting it.
            while textn < 1: 
                textn += 26
            while textn > 26:
                textn -= 26
            #^^^ the above while loops make sure the numbers dont go beyond the alphabet.
            texttc = dic2[textn] #converts the shifted number back into a letter via the second dictionary.
            rtext += texttc #Appends the encrypted character to the final message.
    return rtext 


def decryptshift(text, key):
    rtext = ''  # defining the variable so that python doesn't get angry and throw a hissy fit.
    for i in text:
        i = i.lower() #Setting all the characters to lower case so that the dictionary can handle it.
        if i == ' ':
            rtext += ' '
            #If the character is a space DON'T try to encrypt it.
        else:
            textn = dic1[i] #Converts the letter to a number using the first dictionary.
            int(textn) #Converts the outputted string to a integer.
            textn -= key #Subtracts the key to the converted character thus shifting it.
            while textn < 1:
                textn += 26
            while textn > 26:
                textn -= 26
            #^^^ the above while loops make sure the numbers dont go beyond the alphabet.
            texttc = dic2[textn] #converts the shifted number back into a letter via the second dictionary.
            rtext += texttc #Appends the decrypted character to the final message.
    return rtext


def swap(text):
    rtext = '' # defining the variable so that python doesn't get angry and throw a hissy fit.
    for i in text:
        i = i.lower() #Setting all the characters to lower case so that the dictionary can handle it.
        if i == ' ':
            rtext += ' '
            #If the character is a space DON'T try to encrypt it.
        else:
            i = swapdic[i] # Swaps the letter with another one in the alphabet via the swap dic
            rtext += i #appends the swaped letter to the output string.
    return rtext
quit = 0
while quit == 0:
        inputmess = ('')
    #try:
        print('NOTE: no symbols or numbers in your message.') #Warning
        shiftorswap = input(
            'Would you like to use shift or swap algorithim for encryption or decryption? or quit? (shift/swap/q for quit) ')
        if shiftorswap == 'q':
            quit = 1
            continue
        if shiftorswap == 'swap':
            inputmess = input('enter the message you want to encrypt/decrypt: ') #Inputs message
            print('Your encrypted/decrypted message is', swap(inputmess)) #runs the swap function.
            continue
        encryptordecrypt = input('Are you encrypting or decrypting? (e/d) ')  #Asks user if they are encrypting or decrypting
        if encryptordecrypt == 'e' and shiftorswap == 'shift':
          printlist = []
          inputmess = input('enter the message you want to encrypt: ') #User enters message
          inputkey = 1 #sets key to 0
          for i in inputmess: # gets individual characters from the message to encrypt individually
               printlist.append(encryptshift(i, inputkey)) #appends encrypted character to a list
               if inputkey >2:
                 inputkey = 1 #resets input key if its 3 or greater
               else:
                 inputkey += 1 #increases key
          ptext = ('')
          for i in printlist:
             ptext += i
          print('Your encrypted message is',ptext+'.') 
        if encryptordecrypt == 'd' and shiftorswap == 'shift':
          printlist=[]
          inputmess = input('enter the message you want to decrypt: ') #User enters message
          inputkey = 1 #sets key to 0
          for i in inputmess: # gets individual characters from the message to encrypt individually
               printlist.append(decryptshift(i, inputkey)) #appends encrypted character to a list
               if inputkey >2:
                 inputkey = 1 #resets input key if its 3 or greater
               else:
                 inputkey += 1 #increases input key
          ptext = ('') #defines variable
          for i in printlist:
             ptext += i #turns above list into variable
          print('Your decrypted message is',ptext+'.')
    #except:
        print('An error has occured, please try again from the top. Remember No symbols or numbers in the message.') #Error handling
