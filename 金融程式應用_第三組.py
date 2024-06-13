import yfinance as yf

df=yf.download("0050.TW",start="2022-12-01",end="2024-06-12")
df=df.drop("Adj Close",axis=1)
df=df.drop("Volume",axis=1)
df1=df["High"]
df2=df["Low"]
list1=df1.values.tolist()#high
list2=df2.values.tolist()#low

list00=[]
min1=max(list1)
max1=min(list2)

'''找到最低'''
for i in list2:
    list00.append(i)
    if i <= min1:
        min1=i
        if max1 == min1:
            break
listlen=[list2[i]-list00[i]for i in range (len(list00))]
len1=len(listlen)
del list2[0:len1]
del list1[0:len1]
list00=[]
list11=list1#刪過低價的high
list22=list2#刪過低價的low
'''找最高'''
for j in list11:
    list00.append(j)
    if j >= max1:
        max1=j
        n=list11.index(max1)
        a=list11[n+1]
        b=list11[n+2]
        c=list11[n+3]
        d=list11[n+4]
        e=list11[n+5]
        f=list11[n+6]
        g=list11[n+7]
        if max1>=a and max1>=b and max1>=c and max1>=d and max1>=e and max1>=f and max1>=g:
            break
listlen=[list11[i]-list00[i]for i in range (len(list00))]
len2=len(listlen)
del list11[0:len2]
del list22[0:len2]
list00=[]   
list111=list11#刪過高價的high
list222=list22#刪過高價的low
'''找買賣點'''
buy=(max1-min1)*0.618+min1
sold=(max1-min1)*1.382+min1
for k in list222:
    list00.append(k)
    if k <= buy:
        buy=k
        break
listlen=[list222[i]-list00[i]for i in range (len(list00))]
len3=len(listlen)
del list222[0:len3]
del list111[0:len3]
list00=[]
list1111=list111#刪過買價的high
list2222=list222#刪過買價的low
for m in list1111:
    list00.append(m)
    if m >= sold:
        sold=m
        break
listlen=[list1111[i]-list00[i]for i in range (len(list00))]
len4=len(listlen)
del list2222[0:len4]
del list1111[0:len4]
list00=[]
list1=list1111#新一輪的high
list2=list2222#新一輪的low
print("最低價=",min1)
print("最高價 =",max1)
print("買價=",buy)
print("賣價 =",sold)   
ytm=(sold-buy)/buy*100
print("報酬率 =",ytm,"%")