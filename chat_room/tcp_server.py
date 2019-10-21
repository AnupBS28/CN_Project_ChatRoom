from socket import *
import threading 
#serverName="10.14.140.17"
serverPort=12005

serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)



connectionSocket, addr = serverSocket.accept()


while 1:
 sentence = connectionSocket.recv(1024)
 print(sentence)
 connectionSocket.send(sentence + "anup")
 sentence1 = raw_input("Input lowercase sentence:")
 connectionSocket.send(sentence1 + "anvu")
connectionSocket.close()
'''
def recieve():
	 global serverPort
	 serverSocket=socket(AF_INET,SOCK_STREAM)
	 serverSocket.bind(("",serverPort))
	 serverSocket.listen(1)
	 
	 
	 
	 connectionSocket, addr = serverSocket.accept()
	 
	 capitalizedSentence = sentence.upper()
	 while 1:
		 sentence = connectionSocket.recv(1024)
		 print(sentence)
		 connectionSocket.send(capitalizedSentence)
		 
	connectionSocket.close()
	
	
def sender():
	while 1:
		global serverPort,serverName
		clientSocket = socket(AF_INET, SOCK_STREAM)
		clientSocket.connect((serverName,serverPort))
		sentence = raw_input("Input lowercase sentence:")
		clientSocket.send(sentence)
		#modifiedSentence = clientSocket.recv(1024)
		#print "From Server:", modifiedSentence
	clientSocket.close()


if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=recieve, args=()) 
    t2 = threading.Thread(target=sender, args=()) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!") '''
