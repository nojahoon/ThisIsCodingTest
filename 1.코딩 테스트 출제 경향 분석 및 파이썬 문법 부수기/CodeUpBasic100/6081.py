hex_number = int(input(),16)
for i in range(1,16):
    print('%X*'%(hex_number),'%X' % i,'=%X' % (hex_number*i) , sep='')
    #print("%X*%X=%X" % (hex_number, i, hex_number * i))