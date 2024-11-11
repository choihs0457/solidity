import time
import hashlib


t = int(time.time())
enc = bytes.fromhex("4d5708cd303cd23186a7e6f5ebf64b1ee970bb83c087f3dca020b2f9f960c053")

while True:
    h = hashlib.sha256(str(t).encode()).digest()
    msg = ''
    for i in range(32):
        if not 0x20 <= h[i] ^ enc[i] <= 0x7f:
            break
        msg += chr(h[i] ^ enc[i])
    
    else:
        print(msg)
        break
    t -= 1