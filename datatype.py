#Day2 in training

# 1. Print function displays the contents
# 2. type function display data type of the variable

no = 10
print(no)
print(type(no))


no = 4.5
print(no)
print(type(no))


result = True
print(result)
print(type(result))


name = 'navanee'
print(name)
print(type(name))
print(id(name))



no = 2
print(no)
print(id(no))

no2 = 4
print(no2)
print(id(no2))

#len function takes length of the variable and print function displays the length of the variable.

name = 'thasha'
print(len(name))

no = 888.894555

#Round function takes whole number.
print(round(no))
#Round[round(no,2)] function gives 2numbers after decimalpoints
print(round(no,2))
#Round[round(no,3)] function gives 2numbers after decimalpoints
print(round(no,3))

#Follow practice shows us the way to display numbers in
# 1. Binary form
# 2. Octal form
# 3. Hexa decimal form

#binary form

no = 0B0101
print(no)

no = 0b0101
print(no)

#Octal form

no = 0o776
print(no)

no = 0O776
print(no)

#Hexa form

no = 0X123
print(no)

no = 0x123
print(no)

no = 0Xabc
print(no)

no = 0xCAB
print(no)


#Using functions for binary/octal/hexa

no = bin(20)
print(no)

no = oct(20)
print(no)

no = hex(20)
print(no)

