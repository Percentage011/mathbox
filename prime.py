N=input("何番目の素数を知りたいですか？　")
n=int(N)

p=[2,3]
i=1

while(len(p)<n):
    c=0
    for k in p:
        if((6*i-1)%k==0):
            break
        else:
            c+=1

    if(c==len(p)):
        p.append(6*i-1)

    if(len(p)<n):
        d=0
        for k in p:
            if((6*i+1)%k==0):
                break
            else:
                d+=1

        if(d==len(p)):
            p.append(6*i+1)

    i+=1

if(n==1):
    print("1番目の素数は2です")
else:
    if(n==2):
        print("2番目の素数は3です")
    else:
        print("n番目の素数は"+str(p[-1])+"です")
