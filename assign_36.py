'''
def remove_duplicates(l):
    return [e for e in {e for e in l}]
print(remove_duplicates([4,5,343,2,4,5,3,2,234,4,23,3]))
        
def count_frq(l):
    l.sort()
    d={}
    i=0
    while i<len(l):
        d[l[i]]=l.count(l[i])
        i+=l.count(l[i])
    return d 
print(count_frq([4,5,343,2,4,5,3,2,234,4,23,3]))
print()

def find_num(s):
    l=[]
    for e in s.split(' '):
        try:
                l.append(int(e))
        except:
            pass
    return l
print(find_num(("Enter a string "))
print()
'''
def find_large_seq(l):
    max=0
    start_index=0
    end_index=0
    le=0
    i=1
    while i<len(l):
        if l[i-1]<l[i]:
            le+=1
            if max<le:
                max=le
                start_index=i-le
                end_index=i
        else:
            le=0
        i+=1
    return l[start_index:end_index+1]
print(find_large_seq([5,7,1,3,4,2,7,8,10,11]))

def check_equal_list(l1,l2):
    return l1.sort()==l2.sort() and len(l1)==len(l2)
print(check_equal_list([2,3,5,6,2,4,6,3,2,4],[4,3,6,4]))

