import os,sys
import random as rd

N = input("Choississez un nombre compris enre 1 et 20: ")

rp,wp = os.pipe()
ri,wi = os.pipe()
rsp,wsp = os.pipe()
rsi,wsi = os.pipe()

pid = os.fork()
if pid != 0:
    for i in range(int(N)):
        x = rd.random()*1000
        b = x.hex().encode() # Convertion en bytes du nombre x
        length = len(b) #conversion de la taille en octet: 4 octet, little endian (architecture x86) peut être dans certain cas big endian
        lb = length.to_bytes(4,byteorder="little",signed = True) # signed=True si la valeur peut être négative
        
        if x%2 == 0:
            s = 0
            s = s + x
            s_b_p = s.hex().encode()
            length1 = len(s_b_p)
            ls_b_p = length1.to_bytes(4,byteorder="little",signed = True)
            
            os.close(rp)
            os.close(rsp)
            os.write(wp,b)
            os.close(wp)
            os.write(wsp,s_b_p)
            os.close(wsp)
            
        else:
            s = 0
            s = s + x
            s_b_i = s.hex().encode()
            length2 = len(s_b_i)
            ls_b_i = length2.to_bytes(4,byteorder="little",signed = True)
            
            os.close(ri)
            os.close(rsi)
            os.write(wi,b)
            os.close(wi)
            os.write(wsi,s_b_i)
            os.close(wsi)
               
    os.close(rp)
    os.close(ri)
    os.write(wi,-1)
    os.write(wp,-1)
    
else:
    None
