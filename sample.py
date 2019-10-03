import sys
import os
import csv

def main(path):
    try:
        data = []
        with open(path, 'rb') as csvfile:
            for l in csv.reader(csvfile, quotechar='"', delimiter=',',
                quoting = csv.QUOTE_ALL, skipinitialspace=True):
                    data.append(l)
        head, tail = os.path.split(path)
        if tail == "government-procurement-via-gebiz.csv":
            return govproc(head, data)
        elif tail == "listing-of-registered-contractors.csv":
            return regcont(head, data)
    except IOError:
        print "File not found"

def govproc(directory, data):
    awards = {}
    regs = {}
    
    for line in data[1:]:
        agency = line[1]
        award = float(line[6])
        supplier = line[5]

        # Function 2
        with open(directory + '\\data\\' + agency + '.txt', 'a+') as f:
            f.write(','.join(line)+'\\n')

        # Function 3
        if agency not in awards:
            awards[agency] = 0
        awards[agency] += award

        # Function 4 and 5
        if supplier not in regs:
            regs[supplier] = 0
        regs[supplier] += award
                        
    # Function 3
    for i in sorted(awards, key=awards.get, reverse=True):
        print i, awards[i]

    print '_______________________________________'

    # Function 5
    for i in regs:
        total = 0
        if i == 'na':
            print 'Non-registered: ' + str(regs[i])
        else:
            total += regs[i]
    print 'Registered: ' + str(total)

    count = 0
    for i in sorted(regs, key=awards.get, reverse=True):
        if i != 'na':
            print i, regs[i]
            count += 1
        if count == 5:
            break

'''
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "app.py <path of csv file>"
    else:
        print main(sys.argv[1])
'''

main('sample datasets\Project Datasets\government-procurement\government-procurement-via-gebiz.csv')
