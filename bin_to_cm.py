array = []

text_file = open('figure6.txt') #file
print("Opening file: ", text_file)

max_mm = float(text_file.readline()) # maximum mm first line 
lines = text_file.readlines()

for i in range(1, len(lines)):
    first = lines[i].split('\n')
    array.extend(first)

line = array[0] # width of an image in px
line = line.split() # split the other lines 
pixel = len(line) # length
 
Resolution = max_mm/pixel 
print('Resolution: ', Resolution)