n=int(input())
for i in range (0,n):
    s=str(input())
    l=len(s)
    if l>10:
        print(s[0], end="")
        print(l-2, end="")
        print(s[l-1])
    else:
        print(s)
