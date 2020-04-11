#ord('c') ^ 0x73 = 16
#byte = 16

hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
flag = ""

for i in range(0, len(hex_string), 2):
	hex = hex_string[i:i+2]
	dec = int(hex, 16)
	dec = dec ^ 16
	c = chr(dec)
	flag += c 

print(flag)
