import os
import json
import markovify

class MarkovChatGenerator:

	def __init__(self, messages_dir, text_corpus_dir_name):
		# messages_json_dir = 'inbox'
		# text_corpus_dir = 'chat_corpus'
		self.messages_json_dir = messages_dir
		self.text_corpus_dir = text_corpus_dir_name

	def train_model(self):
		file_handles = {}
		for filename in os.listdir(os.getcwd() + '/' + self.messages_json_dir):
			if filename == '.DS_Store':
				continue
			try:
				with open(self.messages_json_dir + '/' + filename + '/message.json') as f:
					data = json.load(f)
				if not os.path.exists(self.text_corpus_dir):
					os.mkdir(self.text_corpus_dir)
				for participant in data['participants']:
					participant_name = participant['name'].replace(' ', '_').lower()
					file_handles[participant_name] = open(self.text_corpus_dir + '/' + participant_name + '.txt', 'a', encoding="utf-8")

				for message in data['messages']:
					if 'content' in message and message['type']=='Generic' and message['content'].find('http') == -1 and message['content'].find('sent a photo') == -1 and message['content'].find('set his own nickname') == -1 and message['content'].find('removed vote for') == -1 and message['content'].find('voted for') == -1 and message['content'].find('created a poll') == -1 and message['content'].find('set the nickname for') == -1:
						content = message['content'].lower()
						print(content)
						sender_name = message['sender_name'].replace(' ', '_').lower()
						file_handles[sender_name].write(content.replace('\u00f0\u009f\u0098\u009b', ':p') + '\n')	
			except Exception as e:
				pass


	def generate_chat(self, participant1, participant2, chat_length):

		try:
			with open(self.text_corpus_dir + "/" + participant1 +".txt", "r") as f:
				text = f.read()
			text_model_p1 = markovify.NewlineText(text)
		except Exception as e:
			raise e
		
		try:
			with open("chat_corpus/" + participant2 +".txt", "r") as f:
				text = f.read()
			text_model_p2 = markovify.NewlineText(text)
		except Exception as e:
			raise e
		
		p1_name = ' '.join([x.capitalize() for x in participant1.split('_')])
		p2_name = ' '.join([x.capitalize() for x in participant2.split('_')])

		max_tries = 10
		for i in range(int(chat_length)):
			
			current_tries = 0			
			p1_conv = text_model_p1.make_sentence();
			while p1_conv == None and current_tries < max_tries:
				p1_conv = text_model_p1.make_sentence();
				current_tries += 1

			current_tries = 0
			p2_conv = text_model_p2.make_sentence();
			while p2_conv == None and current_tries < max_tries:
				p2_conv = text_model_p2.make_sentence();
				current_tries += 1
			print(p1_name + ': ' + p1_conv)
			print(p2_name + ': ' + p2_conv)

