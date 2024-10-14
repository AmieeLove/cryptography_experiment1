def xor(a:bytes, b: bytes)->bytes:
    return [x^y for x,y in zip(a,b)]

str1 = "1c0111001f010100061a024b53535009181c"
str2 = "686974207468652062756c6c277320657965"
bytes1 = bytes.fromhex(str1)
bytes2 = bytes.fromhex(str2)
x = xor(bytes1,bytes2)
x = [hex(i)[2:] for i in x]
x = ''.join(x)
print(x)
# 746865206b696420646f6e277420706c6179