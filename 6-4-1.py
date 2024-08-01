def reverse(data):
    ret = []
    for index in range(len(data)-1,-1,-1):
        ret.append(data[index])
    return ret

for char in reverse("golf"):
    print(char,end=" ")
print('')
