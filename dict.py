pairs=input("enter key-value pairs seprated by spaces:").split()
t=[(pairs[i],pairs[i+1]) for i in range(0,len(pairs),2)]
d=dict(t)
print("dictnary:",d)
