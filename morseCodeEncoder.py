'''
Morse Code encoder.
'''

from morseCode import CODE

def main():
	print('Enter the text to convert. If you use characters that cannot be converted, they will usually remain as-is. The one exception is full stops, which are removed, because they look like dots.')
	text = input('==> ')
	words = text.split()
	for word in words:
		for c in word:
			try:
				print(CODE.getKey(c.upper()), end='')
			except # Dictionary error because value does not exist:
				print(c, end='')

if __name__ == '__main__':
	main()