N=input("Factoring! ")
#import time
#start = time.time()
n=int(N)
s=n
p=[]
exp=[]

two=0
while(n%2==0):
    two+=1
    n=n/2
if(two>0):
    p.append(2)
    exp.append(two)

three=0
while(n%3==0):
    three+=1
    n=n/3
if(three>0):
    p.append(3)
    exp.append(three)

i=1
while(n>1):
    ae=0
    be=0
    while(n%(6*i-1)==0):
        n=n/(6*i-1)
        ae=ae+1
    if(ae!=0):
        p.append(6*i-1)
        exp.append(ae)
#ここから以上と相同の処理
    while(n%(6*i+1)==0):
        n=n/(6*i+1)
        be=be+1
    if(be!=0):
        p.append(6*i+1)
        exp.append(be)
#ここまでで1つのiに対する処理が終わり、iを更新する
    i=i+1
    if(s>(6*i-1)*(6*i-1)):
        continue

exp_57=0
if(3 in p and 19 in p):
    exp_57=min(exp[p.index(3)],exp[p.index(19)])#57の指数を取得
    if(exp_57!=0):
        exp[p.index(3)]-=exp_57#3の指数を変更
        exp[p.index(19)]-=exp_57#19の指数を変更
        p.append(57)
        p.sort()
        p_57=p.index(57)
        exp_ant=exp[:p_57]
        exp_post=exp[p_57:]
        exp_ant.append(exp_57)
        exp=exp_ant+exp_post

ans=str(s)+" = "
for c in range(len(p)):
    if(exp[c]>1):
        ans=ans+str(p[c])+"^"+str(exp[c])+"*"
    elif(exp[c]==1):
        ans=ans+str(p[c])+"*"

if(s==1):
    print(str(s)+" = 1")
else:
    print(ans[:-1])
if(exp_57!=0):
    print("57は素数！")
