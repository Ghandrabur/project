num = 0
sum = 0
num_line = 0
print("Introduceti cate un numar positiv")
while num >= 0:
    num = int(float(input("Valoare: ")))
    if num >= 0:
            sum += num
            num_line = num_line + 1
print("Suma numerelor introduse este: ", sum)
print("Au fost introduese : ", num_line)
print("Suma medie  : ", int(sum / num_line) )