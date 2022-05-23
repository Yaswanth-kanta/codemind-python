n=input()
count=0
for i in n:
    if i.isdigit()==True:
        count=count+1
if count>0:
    print('Contains {} digit'.format(count))
else:
    print("Doesn't contain digit")