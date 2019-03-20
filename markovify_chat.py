import sys
from markov_chat_generator import MarkovChatGenerator


def argument_error():
	print('Not enough arguments')
	sys.exit(2)


def generate_chat(mcg, argvs):
	mcg.generate_chat(argvs[0], argvs[1], argvs[2])


def train_model(mcg):
	mcg.train_model()


if __name__ == "__main__":

	mcg = MarkovChatGenerator('inbox', 'chat_corpus')
	if len(sys.argv) == 1:
		argument_error()
	elif sys.argv[1] == 't':
		train_model(mcg)
	elif sys.argv[1] == 'g':
		if len(sys.argv) < 5:
			argument_error()
		else:
			generate_chat(mcg, sys.argv[2:])
	else:
		'Unknown arguments'