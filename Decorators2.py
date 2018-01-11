import os



def exists(oldfunc):
    def val(fname):
        if(os.path.exists(fname)):
            oldfunc(fname)
        else:
            print 'File does not exist'
    return val

@exists
def outputLine(inFile):
    with open(inFile) as f:
        print(f.readlines())

outputLine('Employee.py')
outputLine('Employ.py')
