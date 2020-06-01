KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2xKEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2xKEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAGxKEY1xKEY3xKEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"



def xor(hex_string_1, hex_string_2):
    hexed = ""
    for i in range(0, len(hex_string_1), 2):
        xored = int(hex_string_1[i:i+2], 16) ^ int(hex_string_2[i:i+2], 16)
        hexed += hex(xored)[2:4].zfill(2) #ex : 0x4 --> 04
         
    return hexed

def hex_to_str(hex_string):
    string = ""
    for i in range(0, len(hex_string), 2):
        hex = hex_string[i:i+2]
        dec = int(hex, 16)
        string += chr(dec)
    
    return string

a = xor(FLAGxKEY1xKEY3xKEY2, KEY2xKEY3)
flag = xor(a, KEY1)
print(hex_to_str(flag))