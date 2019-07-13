#入力されたピタゴラス数がピタゴラス群を生成するか確認するためのプログラム
#和と差について群を成すらしい
#精製したピタゴラス数は原始解も表示する
#原始解は入力したピタゴラス数の因数になるらしい

N=input("ピタゴラス群に分解しよう！>>>　")
n=int(N)

import math

#入力を原始ピタゴラス数に揃えるためにできるだけ4で割り、4で割ったあまりが1であるか判定する
k=0
while(n%2==0):
    n=n/2
    k+=1

p=[] #ピタゴラス数の組を入れておくリストのリスト。これ自体の要素はリスト
#4で割ったあまりが1の場合の処理。ピタゴラス数に分解できる可能性がある
if(n%4==1 and n!=1):
    a=1 #aの初期化
    i=-1 #リストpのインデックス用のカウンタ変数。c*c-a*aが平方数の時に働く
    while(a<n/math.sqrt(2)): #それぞれのaに対してbbが平方数であるかを確認する
        c=n #毎回初期化する
        bb=c*c-a*a
        a+=1
        if(math.sqrt(bb)%1==0): #bbが平方数のときに以下の処理をする
            i+=1
            a-=1
            b=math.sqrt(bb)
            p.append([])
            a=a*(2**k)
            b=b*(2**k)
            a=int(a)
            b=int(b)
            p[i].append(a)
            p[i].append(b)
            a=a/(2**k)
            a+=1
pp,plus,minus=[],[],[]
for r in p:
    if(math.gcd(r[0],r[1])==1):
        if r[0]%2==1:
            pp.append([r[0],r[1]])
        else:
            pp.append([r[1],r[0]])
lengthpp=len(pp)
for i in range(1,lengthpp):
    for j in range(i):
        plus.append([pp[i][0]+pp[j][0],pp[i][1]+pp[j][1]])
        minus.append([abs(pp[i][0]-pp[j][0]),abs(pp[i][1]-pp[j][1])])
for i in range(int(lengthpp*(lengthpp-1)/2)):
    a=math.sqrt(plus[i][0]**2+plus[i][1]**2)
    b=math.sqrt(minus[i][0]**2+minus[i][1]**2)
    if a%1==0:
        a=int(a)
        gcdplus=math.gcd(plus[i][0],plus[i][1])
    if b%1==0:
        b=int(b)
        gcdminus=math.gcd(minus[i][0],minus[i][1])
    print(plus[i][0],plus[i][1],a,int(plus[i][0]/gcdplus),int(plus[i][1]/gcdplus),int(a/gcdplus))
    print(minus[i][0],minus[i][1],b,int(minus[i][0]/gcdminus),int(minus[i][1]/gcdminus),int(b/gcdminus))
