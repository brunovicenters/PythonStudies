# Saving files path
filename = 'rocky-speech.txt'

# Opening file in read mode
file = open(filename, mode='r')

# Reading file's content and saving it
text = file.read()

# Closing file
file.close()

# Printing file's content
print(text)

# ****************************************************************************************

print("\n************* Using With ************* \n")

# You can avoid closing the connection by using a with statement, creating a context
with open('rocky-speech.txt', mode='r') as file:
     print(file.read())

# ****************************************************************************************

print("\n************* Printing lines ************* \n")
with open('rocky-speech.txt', mode='r') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())