from socket import *
import sys
import os

serverName = 'DESKTOP-FUGEQON'
serverPort = int('8888')
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print("Connected. Type !help for command list:\n")
path = ("./")
files = [f for f in os.listdir('.') if os.path.isfile(f)]

while 1:
  sentence = input('>')
  _check = sentence.split(" ", 1)
  if(sentence=="!help"):
    print ("Available commands:\n"+
           "!help         : list available commands\n"+
           "ls-local      : list local files\n"+
           "ls-remote     : list remote files\n"+
           "get 'filename': download remote file to local\n"+
           "put 'filename': upload local file to remote\n"+
           "exit          : terminates program")
  elif(sentence=="ls-local"):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print("local files:")
    for f in files:
      fileSize = os.path.getsize(f)
      print("-> "+f+"\t%d bytes" % fileSize)
  elif(sentence=="exit"):
    break

  elif(sentence=="ls-remote"):
    clientSocket.sendto(sentence.encode('utf-8'),(serverName, serverPort))
    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode('utf-8'))

  elif(len(_check)==2):
    if(_check[0].lower()=="get" or _check[0].lower()=="put"):
      '''
       send file
       (wait) receive ACK signaling that server caught the file
       upload complete
      '''
      if(_check[0]=='put'):
        _found = 'False'
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
          if(f == _check[1]):
            _found = 'True'
            print("File found, sending request to server...")
            clientSocket.sendto(sentence.encode('utf-8'),(serverName, serverPort))
            modifiedSentence = clientSocket.recv(1024)
            print("ACK: "+  modifiedSentence.decode('utf-8'))
            fileSize = os.path.getsize(f)
            clientSocket.sendto(str(fileSize).encode('utf-8'),(serverName, serverPort))
            modifiedSentence = clientSocket.recv(1024)
            print("ACK2 :"+ str(modifiedSentence.decode('utf-8')))
            f = open((path+f), "rb")
            buffRead = 0
            bytesRemaining = int(fileSize)
            while bytesRemaining != 0:
              if(bytesRemaining >= 1024):
                buffRead = f.read(1024)
                sizeofSlabRead = len(buffRead)
                print('remaining: %d' % bytesRemaining)
                print('read: %d'%sizeofSlabRead)
                clientSocket.sendto(buffRead,(serverName, serverPort))
                bytesRemaining = bytesRemaining - int(sizeofSlabRead)
              else:
                buffRead = f.read(bytesRemaining)
                sizeofSlabRead = len(buffRead)
                print('remaining: %d'%bytesRemaining)
                print('read: %d'%sizeofSlabRead)
                clientSocket.sendto(buffRead,(serverName, serverPort))
                bytesRemaining = bytesRemaining - int(sizeofSlabRead)
            print("Read file completely")
        if(_found == 'False'):
          print('File requested not available in dir.')
      elif(_check[0]=='get'):
        clientSocket.sendto(sentence.encode(),(serverName, serverPort))
        modifiedSentence = clientSocket.recv(1024)
        if(modifiedSentence.decode('utf-8') == 'True'):
          print('File found, preparing download...')
          reqFileSize = clientSocket.recv(1024)
          print("file size: "+ str(reqFileSize.decode('utf-8')))
          fSizeACK = str(reqFileSize)
          clientSocket.sendto(fSizeACK.encode('utf-8'),(serverName, serverPort))
          f = open((path+_check[1]), "wb")
          buffWrote = 0
          bytesRemaining = int(reqFileSize)

          while bytesRemaining != 0:
            if(bytesRemaining >= 1024):
              slab = clientSocket.recv(1024)
              f.write(slab)
              sizeofSlabReceived = len(slab)
              print("wrote %d bytes" % len(slab))

              bytesRemaining = bytesRemaining - int(sizeofSlabReceived)
            else:
              slab = clientSocket.recv(bytesRemaining)
              f.write(slab)
              sizeofSlabReceived = len(slab)
              print("wrote %d bytes" % len(slab))
              bytesRemaining = bytesRemaining - int(sizeofSlabReceived)

        elif(modifiedSentence == 'False'):
          print(modifiedSentence.decode('utf-8'))
          print('File requested not available in remote dir.')
    else:
      print("[invalid command]")
  else:
    print("[invalid command]")
clientSocket.close()

