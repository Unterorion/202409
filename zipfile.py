import zipfile

with zipfile.zipfile('mytext.zip', 'w') as myzip:
    myzip.write('finally.txt')
    myzip.write('newfile.txt')
    myzip.write('readtxt.txt')
    myzip.write('test.txt')
