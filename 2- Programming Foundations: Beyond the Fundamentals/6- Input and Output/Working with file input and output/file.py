input_file = open("input.in", "r")
output_file = open("output.txt", "w")
print("Start reading file")
sum = 0
items = 0
for i in input_file:
    items += 1
    sum += int(i)

print("Sum =", sum, file=output_file)
print("Average =", sum/items, file=output_file)
output_file.close()
print("End")