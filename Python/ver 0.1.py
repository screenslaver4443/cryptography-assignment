#Cryptopgraphy assignment
#Ver 0.1
#By Nikolai

dic1 = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26
}
dic2 = {
    1:'a',
    2:'b',
    3:'c',
    4:'d',
    5:'e',
    6:'f',
    7:'g',
    8:'h',
    9:'i',
    10:'j',
    11:'k',
    12:'l',
    13:'m',
    14:'n',
    15:'o',
    16:'p',
    17:'q',
    18:'r',
    19:'s',
    20:'t',
    21:'u',
    22:'v',
    23:'w',
    24:'x',
    25:'y',
    26:'z'
}

def encryptshift(text, key):
    rtext = ''
    for i in text:
        i = i.lower()
        if i == ' ' :
        	rtext += ' '
        else:
	        textn = dic1[i]
	        int(textn)
	        textn += key
	        while textn < 1:
	        	textn += 26
	        while textn > 26:
	        	textn -= 26
	        texttc = dic2[textn]
	        rtext += texttc
    return rtext

def decryptshift(text, key):
    rtext = ''
    for i in text:
        i = i.lower()
        if i == ' ' :
        	rtext += ' '
        else:
	        textn = dic1[i]
	        int(textn)
	        textn -= key
	        while textn < 1:
	        	textn += 26
	        while textn > 26:
	        	textn -= 26
	        texttc = dic2[textn]
	        rtext += texttc
    return rtext

def enswap(text):
	placeholder

while True:
	print('Encrypter/decrypter')
	shiftorswap = input('Are you using shift or swap for encryption or decryption? (shift/swap) ')
	encryptordecrypt = input('Are you encrypting or decrypting? (e/d) ')
	if encryptordecrypt == 'e' and shiftorswap == 'shift':
		inputmess = input('enter the message you want to encrypt: ')
		try:
			inputkey = int(input('Enter the encryption key (whole numbers only and no more than 26 and no negatives.)'))
		except: 
			print('Welp from the top.')
			continue
		print('your encrypted message is',encryptshift(inputmess, inputkey))
