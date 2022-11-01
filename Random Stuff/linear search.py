array = ["aaron", "sam", "ben", "dan", "ryan"]
toFind = input("name to find?")
found = False
for i in range(len(array)):
    if array[i] == toFind:
        print(toFind, "is found at index:", i)
        found = True
if not found:
    print("not found")
