from telepot import Bot
from scripts import TOKEN_API
from scripts.motor import Motor

	
class ChatGpt(Bot):
	def __init__(self):	
		self.tele = Bot(TOKEN_API)
		self.tele.message_loop({'chat': self.callback_recv, 'callback_query': self.callback_send})
		self.dr = Motor()

	def callback_send(self, msg): 
		print(msg)

	def callback_recv(self, msg): 
		print(msg)
		self.dr.write_text(msg['text'])
		response = self.dr.await_response()
		self.tele.sendMessage(msg['from']['id'], response)

  	
ChatGpt()
while True: 
	...