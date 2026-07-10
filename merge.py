item1=input("enter key-vale pairs for first dictinory:").split()
item2=input("enter key-vale pairs for second  dictinory:").split()

dict1={item1[i]:item1[i+1]for i in range(0,len(item1),2)}
dict2={item2[i]:item2[i+1]for i in range(0,len(item2),2)}

merged=dict1.copy()
merged.update(dict2)

print("merged dict:",merged)
