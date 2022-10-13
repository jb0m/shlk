print("Введите n и m")
n,m=map(str, input().split())
if len(n)>len(m):
    print("n больше m")
elif len(n)<len(m):
    print("n меньше m")
else:
    print("кто я?")
    print("n=m")