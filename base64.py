hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bin_string = ""

for i in range(0, len(hex_string), 2):
	hex = hex_string[i:i+2]
	dec = int(hex, 16)
	byte = bin(dec)[2:]
	bin_string = bin_string + byte 

print(bin_string)
