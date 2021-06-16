words = {}
def read_from_file():
	with open("words_base.txt") as f:
		for line in f:
			(key, val) = line.split()
			words[str(key)] = val