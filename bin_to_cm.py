array = []

text_file = open('figure6.txt') #file
print("Opening file: ", text_file)

max_mm = float(text_file.readline()) # maximum mm first line 
lines = text_file.readlines()

for i in range(1, len(lines)):
    first = lines[i].split()
    # print(first)
    array.extend(first)

pixel = [s for s in array if "1" in s]

if (len(pixel)) == 0:
    print("Object is not found")
else:
    
    Resolution = max_mm/len(pixel) 
    print('Resolution: ', Resolution)