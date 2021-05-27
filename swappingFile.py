from os import close

def swapFileData(file_a,file_b):
    a = open(file_a)
    data_a = a.read()
    a.close()

    b = open(file_b)
    data_b = b.read()
    b.close()

    file1 = open(file_a,'w')
    file1.write(data_b)
    file1.close()

    file1 = open(file_b,'w')
    file1.write(data_a)
    file1.close()

input_a = input('Enter name of file 1')
input_b = input('Enter name of file 2')

swapFileData(input_a,input_b)