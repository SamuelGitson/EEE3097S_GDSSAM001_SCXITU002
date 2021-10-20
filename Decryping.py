from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import gzip
import shutil
import encryption_testing
import time
starttime = time.time()
def decomp2():
    Fenc = open('outputfile.txt', 'wb')
    with gzip.open('outputfile.txt.gz','rb') as Fdec:
        bindata = Fdec.read()
    Fenc.write(bindata)
    Fenc.close()
decomp2()




print("decompression time: ")
print("--- %s seconds ---" % (time.time()-starttime))
def decryp():
    input_file = 'D:\\encrypted.txt'  # the input file
    input2 = 'outputfile.txt.gz'
    input3 = 'outputfile.txt'
    key = encryption_testing.key

    # read the data from the file
    file_in = open(input3, 'rb')
    iv = file_in.read(16)  # read the iv out, and note that it is 16 bytes long
    ciphered_data = file_in.read()  #read the rest of the data
    file_in.close()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)  # setup the cipher
    original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)

    ##print(original_data)
    input_filewrite = open(input3, "wb")
    input_filewrite.write(original_data)


decryp()

print("decryption time: ")
print("--- %s seconds ---" % (time.time()-starttime))