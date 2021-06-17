dict1={1:'one',2:'two',3:'three'}
dict2={4:'four',5:'five'}
print('Dict1 = ',dict1)
print('Dict2 = ',dict2)
dict1.update(dict2)
print('Dict1 = ',dict1)
dict1.pop(3)
print('Dict1 after removing key 3 = ',dict1)
list1=[16,17,18,19,20]
list2=['sixteen','seventeen','eighteen','nineteen','twenty']
dict3=dict()
print('list1 : ',list1)
print('list2 : ',list2)
for i in range(len(list1)):
    dict3[list1[i]]=list2[i]
print('After converting two list to dictionary : ',dict3)
set1={1,2,3,4,5}
set2={3,4}
print('set1 : ',set1)
print('set2 : ',set2)
print('length of set1 : ',len(set1))
set3=set1.difference(set2)
print('After removing the intersection of a 2nd set from the 1st set',set3)
