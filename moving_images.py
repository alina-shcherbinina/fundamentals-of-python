import numpy as np

def read_file(name):
    array=[]
    text_file = open(name) #file
    #print("Opening file: ", text_file)
    lines = text_file.readlines()
    text_file.close()
    for i in range(2, len(lines)):
        first = lines[i].split()
        array.append(first) #if extend its out of range :(
    
    pic = np.array(array, dtype='int32') 
    return pic

def coordinates(pic):
    for y in range(pic.shape[0]):
        for x in range(pic.shape[1]):
            if pic[y, x] == 1:
                return y, x

first = read_file('img1.txt')
second = read_file('img2.txt')

y1, x1 = coordinates(first)
y2, x2 = coordinates(second)
 
final_x = x2-x1
final_y = y2-y1

print('moved by y:', final_y, ', moved by x:', final_x)