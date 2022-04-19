n = [[8, 3, 4],
[1, 5, 9],
[6, 7, 2]]    
i=0
row1=0
row2=0
row3=0
column1=0
column2=0
column3=0
diagonal1=0
diagonal2=0

while i<len(n):
    j=0
    while j<len(n[i]):
        if i==0:
            row1+=n[i][j]
        elif i==1:
            row2+=n[i][j]
        elif i==2:
            row3+=n[i][j]
        j+=1
    i+=1
print(row1)
print(row2)
print(row3)
a=0
while a<len(n):
    k=0
    while k<len(n[a]):
        if k==0:
            column1+=n[a][k]
        elif k==1:
            column2+=n[a][k]
        elif k==2:
            column3+=n[a][k]
        k+=1
    a+=1
print(column1)
print(column2)
print(column3)
i=0
while i<len(n):
    diagonal1+=n[i][i]
    i+=1
print(diagonal1)
i=0
j=2
while i<len(n):
    diagonal2+=n[i][j]
    i+=1
    j-=1
print(diagonal2)
if row1==row2==row3==column1==column2==column3==diagonal1==diagonal2:
        print("This is a magic square")
else:
        print("this is not a magic square")

