#python has functions for crud

# open a file
#this creates a file even if it doesnt exist
myFile =open('myfile.txt', 'w')

#get some info
print('Name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

#write to file
myFile.write('I love python')
myFile.write(' and javascript')
myFile.close()

#append to file
# use a to append if u use w it will overwrite it
myFile =open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

# read from file
myFile =open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)