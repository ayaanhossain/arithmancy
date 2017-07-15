from itertools import imap
from string    import ascii_uppercase as au

class arithmancy(object):

	aggrippan = {
		'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
		'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
		'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
	}

	chaldean = {
		'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 8, 'G': 3, 'H': 5, 'I': 1,
		'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 7, 'P': 8, 'Q': 1, 'R': 2,
		'S': 3, 'T': 4, 'U': 6, 'V': 6, 'W': 6, 'X': 5, 'Y': 1, 'Z': 7
	}

	def __init__(self, chart=aggrippan):
		self.chart=chart

	def get_character(self, name):
		name      = name.upper()
		char_set  = set(iter(au))
		print list((char, self.chart[char]) for char in name if char in char_set)
		character = sum(self.chart[char] for char in name if char in char_set)
		while character >= 10:
			character = sum(imap(int, iter(str(character))))
		return int(character)

def main():
	arithmancer = arithmancy(chart=arithmancy.aggrippan)
	print arithmancer.chart
	print arithmancer.get_character('Ayaan Hossain')

if __name__ == '__main__':
	main()