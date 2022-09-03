n=int(input("how many entery you want to add"))
d=dict(input("enter the key and data").split(",") for _ in range(n))
for k,t in d:
    print(k,t)
