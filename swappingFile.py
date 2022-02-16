def swapFileData():
    file1ToSwap = input("Enter your file that to swap : ")
    file2ToSwap = input("Enter your file that to swap : ")
    data_a = open(file1ToSwap,"w")
    data_b = open(file2ToSwap,"w")
    with open(file1ToSwap,"r") as a:
        data_a = a.read()
    with open(file2ToSwap, 'r') as b:
        data_b = b.read()
    with open(file1ToSwap,"w") as a:
        a.write(data_b)
    with open(file2ToSwap, 'w') as b:
        b.write(data_a)