def addItem(l,a):
    pos=int(input('Enter the position in which the element needs to be inserted : '))
    l.insert(pos,a)
    return l
def deleteItem(a):
    l.remove(a)
    return l
l=list()
n=int(input('Enter the N value : '))
print('Enter the values : ')
for i in range(n):
    c=int(input())
    l.append(c)
print('Your list : ',l)
a=int(input('Enter the element to be inserted : '))
l=addItem(l,a)
print('List after insertion : ',l)
a=int(input('Enter the element to be deleted : '))
l=deleteItem(a)
print('List after deletion : ',l)
minimum=min(l)
maximum=max(l)
print('Minimum element is : ',minimum)
print('Maximum element is : ',maximum)
t1=(1,2,3,4,5)
print('Created Tuple is : ',t1)
print('Reversed Tuple is : ',t1[::-1])
t2=(16,17,18,19,20)
print('Created Tuple is : ',t2)
t3=list(t2)
print('After conversion of tuple to list : ',t3)

