# open the file file2.txt in read mode    
fileptr = open("copy.txt","r")    
  
#initially the filepointer is at 0     
print("The filepointer is at byte :",fileptr.tell())    
    
#reading the content of the file    
content = fileptr.read();    
    
#after the read operation file pointer modifies. tell() returns the location of the fileptr.     
    
print("After reading, the filepointer is at:",fileptr.tell())    
