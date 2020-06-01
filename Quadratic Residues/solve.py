p = 29
ints = [14, 6, 11]

for i in range(2, 29):
    a = i**2%29
    if(a in ints):
        print(i,"**2 = ", a, "[29]")

