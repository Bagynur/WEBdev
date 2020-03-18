n = int(input())
b = input().split()
cnt = int(0)

a = []

for i in range(0,n):
    a.append(int(b[i]))

for i in range(1,n-1):
    if(a[i-1]<a[i] and a[i+1]<a[i]):
        cnt =cnt+1
        
print(cnt)