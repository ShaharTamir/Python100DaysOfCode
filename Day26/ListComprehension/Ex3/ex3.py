with open("file1.txt", "r") as f1:
    file1 = f1.readlines()

with open("file2.txt", "r") as f2:
    file2 = f2.readlines()

result = [int(num) for num in file1 if num in file2]
print(result)
