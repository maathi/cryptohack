hex_string = input("enter your hex string: \n")
str = ""

for i in range(0, len(hex_string), 2):
	hex = hex_string[i:i+2]	
	dec = int(hex, 16)
	char = chr(dec)
	str += char

print(str)
