from collections import Counter
li=[('romance', 23), ('drama', 22), ('action', 13)]
for i in li:
    print(i[0])

strin="sssss,sssss"
if(',' in strin):
    print("yes")
li=[strin]
print(Counter(li))