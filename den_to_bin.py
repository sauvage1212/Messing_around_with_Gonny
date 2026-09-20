def den_to_bin(numb):
    unknown = True
    bin_length = 1
    x = 2
    while unknown:
        if numb < (x):
            unknown = False
            length_of_output = bin_length
        x *= 2
        bin_length += 1
    # print("len of out: ", length_of_output)
    digits_in_output = []
    for i in range(length_of_output):
        collumn_digit = 2 ** ((length_of_output - 1) - i)
        # print("col", collumn_digit)
        if (numb - (collumn_digit)) >= 0:
            numb -= collumn_digit
            digits_in_output.append(1)
        else:
            digits_in_output.append(0)
    output = ""
    for digit in digits_in_output:
        output = output + str(digit)
    return output      
    # return "Bob this old: "
num = int(input("num:"))
print(den_to_bin(num))

# 1, 2, 4, 8, 16
# 2, 4, 8, 16, 32
# 2 ** length_of_output