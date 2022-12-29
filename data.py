import numpy as np
data_from_text_file=np.genfromtxt('textfile_1.txt',delimiter=',')
print(data_from_text_file)

data_from_text_file=data_from_text_file.astype('int32')
print(data_from_text_file)

print(data_from_text_file>10)
print(data_from_text_file[data_from_text_file>0])

#numpy_function
def numpy_function(x,y):
    return 10 * x + y
b = np.fromfunction(numpy_function, (2, 3), dtype=int )
print(b)
