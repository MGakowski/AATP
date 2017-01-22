createfile = int(raw_input("Create separate file=1, Overwrite=2 "))
pyver = int(raw_input("Pyhton version 2 or 3?"))


if createfile == 1:
    # Gets filenames
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

if createfile == 2:
    # Gets filenames
    filename = str(raw_input("File name of target ascii art? "))
    read_file = open(filename + '.txt', "w+")

    currentl = 0

    with open(filename + '.txt') as f:
        linecount = sum(1 for _ in f)

    for x in range(0, linecount):
        #read_it = read_file.read().splitlines()[currentl]
        if pyver == 2:
            read_file.write('print "' + read_file.read().splitlines()[currentl] + '"')
            print "writing"
        else:
            read_file.write('print("' + read_file.read().splitlines()[currentl] + '")')
        currentl += 1
    read_file.close()
