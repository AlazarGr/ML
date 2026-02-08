a = input().split()
b = list(map(int, input().split()))
d = dict(zip(a, b))
print(d)


ans = sum(d.values())
f = open("file-1.txt", "w")
f.write(str(ans))
print(ans)
f.close()