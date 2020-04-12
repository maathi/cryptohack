hex_string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

flag = ""
# for i in range(0, len(hex_string), 2):
# 	hex = hex_string[i:i+2]
for i in range(32, 126):
	dec = int("0e", 16)
	key = dec ^ i

	for j in range(0, len(hex_string), 2):
		hex = hex_string[j:j+2]
		dec = int(hex, 16)
		dec = dec ^ key
		c = chr(dec)
		flag += c
	print(flag)	
	flag=""
	print("################################")

