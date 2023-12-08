a,b,c = map(int,input().split())
sr = min(max(a,b),max(b,c),max(a,c))
print(sr)