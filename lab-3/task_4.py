
n = int(input("введите натуральное число: "))


for i in range(1,n+1):
    #spaces in the beggining
    for j in range(n-i,0,-1):
        print(" ",end="")
        
    for k in range(1,i+1):
        print(k,end='')

    #обратный
    for t in range(i-1,0,-1):
        print(t,end='')
    #go to the next line 
    print()
        