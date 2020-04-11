import socket
import json
import base64
import codecs

s = socket.socket()
s.connect(("socket.cryptohack.org", 13377))



while True:
    msg = s.recv(1234)
    dic = json.loads(msg)
    print(dic)
    print("******************************")
    decoded = ""

    if dic["type"] == "base64":
        decoded = base64.b64decode(dic["encoded"]).decode()
        jo = "{\"decoded\":\"" + decoded + "\"}"
        
        s.send(jo.encode())
        
    elif dic["type"] == "hex":
       
        for i in range(0, len(dic["encoded"]), 2):
            hex = dic["encoded"][i:i+2]	
            dec = int(hex, 16)
            char = chr(dec)
            decoded += char

        jo = "{\"decoded\":\"" + decoded + "\"}"
        s.send(jo.encode())
    elif dic["type"] == "rot13":
        decoded = codecs.encode(dic["encoded"], 'rot_13')
        jo = "{\"decoded\":\"" + decoded + "\"}"

        s.send(jo.encode())
    elif dic["type"] == "bigint":
        for i in range (2, len(dic["encoded"]), 2):
            hex = dic["encoded"][i:i+2]
            decoded += chr(int(hex, 16))

        jo = "{\"decoded\":\"" + decoded + "\"}"
        s.send(jo.encode())
    elif dic["type"] == "utf-8":
        for i in dic["encoded"]:
            decoded += chr(int(i))
        
        jo = "{\"decoded\":\"" + decoded + "\"}"
        s.send(jo.encode())
    else:
        break


