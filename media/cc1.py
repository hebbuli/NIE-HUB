n=input()
l=list(map(int,n[2:].split()))
m=[]

for i in l:
	m.append("1")
	m.append(str(2*i))
print(" ".join(m))
