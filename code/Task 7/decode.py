with open('test.bin', 'rb') as file_bin, open('test_info.dat', 'r') as file_info, open('test_decode.txt', 'w') as file_decode:
    bit_string = ""
    byte = file_bin.read(1)
    while(len(byte) > 0):
        byte = ord(byte)
        bits = bin(byte)[2:].rjust(8, '0')
        bit_string += bits
        byte = file_bin.read(1)
    

    info = file_info.read().split(';')
    n = int(info[0])
    dic = {}
    for i in range(1, len(info)-1):
        key = info[i].split(':')
        dic[key[1]] = key[0]
    
    count=0;
    text=''
    c=''
    for ch in bit_string:
        c+=ch
        if c in dic and count < n:
            text += dic[c]
            c=''
            count +=1

    file_decode.write(text)
    print("decode!")

    
