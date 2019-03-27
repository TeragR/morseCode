'''
Morse Code decoder.
Completely untested.
'''

from morseCode import CODE

# Printed when a char cannot be decoded.
UNKNOWN_CHAR = '?'
	
def main():
	print('Enter the code to decode below. Use full stops for dots, hyphens for dashes, spaces to separate letters, and \'/\' to separate words.')
	encoded = input('==> ')
	words = encoded.split('/')
	for word in words:
		letters = word.split(' ')
		for letter in letters:
			try:
				print(CODE[letter], end='')
			except # Dictionary error because key doesn't fit:
				print(UNKNOWN_CHAR, end='')

if __name__ == '__main__':
	main()