'''
def writing(filename,text):
    f=open(filename,'a')
    f.write(text)
    f.close()

fn="mushahid.txt"
t="hey This is me How are you doing right now"
writing(fn,t)

def display(filename):
    f=open(filename,'r')
    text=f.read()
    print(text)
    f.close()
#display("mushahid.txt")

def copy(fromfile,tofile):
    ffrom=open(fromfile,'r')
    fto=open(tofile,"a")
    text=ffrom.read()
    fto.write(text)
    ffrom.close()
    fto.close()

writing("md.txt",'hi ')
#display('md.txt')
copy("mushahid.txt","md.txt")
display("md.txt")


def extractNumbers(filename):
    try:
        l=[]
        f=open(filename,'r')
        for e in f.read().split(' '):
            if e.isdigit():
                l.append(int(e))
        f.close()
    except FileNotFoundError as e:
        print(e)
    return l
print(extractNumbers("india.txt"))

'''

def extractdata(filename):
    d={}
    f=open(filename,'r')
    for line in f.readlines():
        data=line.split(',')
        d[data[0]]=data[1]
    f.close()
    return d

print(extractdata('india.txt'))