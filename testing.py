str = 'ab'
if len(str) <= 1:
    print(str)
else:
    mid = str[1:len(str)-1]
    print(str[len(str)-1] + mid + str[0])

print(str[len(str)-1])
print(mid)
print(str[0])
