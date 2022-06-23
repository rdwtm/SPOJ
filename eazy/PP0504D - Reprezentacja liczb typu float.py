import struct

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])
n = int(input())


for z in range(n):
    x=float_to_hex(float(input()))
    x=str(x)
    h=""
    for c in range(2, len(x), 2):
        if x[c:c+2]=="00":
            ar="0"
        else:
            ar=x[c:c+2]
        if c <8:
            h=h+ar+" "
        else:
            h=h+ar

    print(h)

