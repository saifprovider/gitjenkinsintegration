print("Hello Saif")
for x in range(1,101):
    for y in range(2,x):
        if(x%y ==0):break
        else:
            print(x,sep='', end='')

