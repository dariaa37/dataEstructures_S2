from array import array


arrays = [[], [], []]

for i in range(6):
    arrays[0].append(int(input(f"Value {i+1} for ARRAY 1: ")))
    arrays[1].append(int(input(f"Value {i+1} for ARRAY 2: ")))
    arrays[2].append(arrays[0][i] + arrays[1][i])

print("TERCER ARRAY")
for i in range(6):
    print(f"{i+1}. {arrays[2][i]}")