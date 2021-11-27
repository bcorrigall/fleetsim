import itertools
list1 = [1, 2, 4, 6, 7,8]
list2 = ['n','','fasd',' das','gasg']

for x, y in itertools.zip_longest(list1,list2):
    if x:
        print(x)
    if y:
        print(y)