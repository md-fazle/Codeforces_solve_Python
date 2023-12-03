a=[]
for _ in range(5):
    arr=list(map(int,input().split()))
    a.append(arr)
for i in range(5):
    for j in range(5):
        if a[i][j]==1:
            row=i
            column=j
print(abs(row-2)+abs(column-2))