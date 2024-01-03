marks=[4,78,56,93,32,67,81,97,45,8,35,71,34,86,89,48,70,27,84,59]
low=[]
mid=[]
high=[]
for num in marks:
    if num<=30:
        low.append(num)
    if num>=31 and num<=61:
        mid.append(num)
    if num >=70:
        high.append(num)
print(low)
print(mid)
print(high)