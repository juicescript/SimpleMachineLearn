from chatterbot import ChatBot

chatbot = ChatBot('Ron Obvious', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

while True:
	req = raw_input("Voce: ")
	print("Robo: " + str(chatbot.get_response(req)))
