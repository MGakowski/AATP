import os

createfile = int(raw_input("Create separate file=1, Overwrite=2 "))
pyver = int(raw_input("Pyhton version 2 or 3? "))
filen = str()

# New File
if createfile == 1:
    filename = str(raw_input("File name of target ascii art? "))
    newfile = str(raw_input("New file name? "))
    write_file = open(newfile + '.txt', "w")
    read_file = open(filename + '.txt', "r")

    currentl = 0

    with open(filename + '.txt') as f:
        linecount = sum(1 for _ in f)

    for x in range(0, linecount):
        read_file = open(filename + '.txt', "r")
        read_it = read_file.read().splitlines()[currentl]
        if pyver == 2:
            write_file.write('print "' + read_it + '"\n')
        else:
            write_file.write('print("' + read_it + '")\n')
        currentl += 1
    write_file.close()

# Overwrite
if createfile == 2:
    filename = str(raw_input("File name of target ascii art? "))
    filen = filename
    newfile = str(filename + "_temp")
    write_file = open(newfile + '.txt', "w")
    read_file = open(filename + '.txt', "r")

    currentl = 0

    with open(filename + '.txt') as f:
        linecount = sum(1 for _ in f)

    for x in range(0, linecount):
        read_file = open(filename + '.txt', "r")
        read_it = read_file.read().splitlines()[currentl]
        if pyver == 2:
            write_file.write('print "' + read_it + '"\n')
        else:
            write_file.write('print("' + read_it + '")\n')
        currentl += 1
    read_file.close()
    write_file.close()
    os.remove(filename + ".txt")
    os.rename(filen + "_temp.txt", filen + ".txt")
