file = open("data.dat", "r")

cout = 0

for line in file:    
    cout_0 = 0
    cout_1 = 0
    for i in line:
        if i == "0":
            cout_0 += 1
        elif i == "1":
            cout_1 += 1
    if cout_0 % 3 == 0 or cout_1 % 2 == 0:
        cout += 1

print(cout)
