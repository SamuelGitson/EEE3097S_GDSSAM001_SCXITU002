from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import gzip
import shutil
import encryption_testing
import time
starttime = time.time()
def decomp2():
    with gzip.open("outputfile.txt.gz", "rb") as f_in:
        with open("outputfile.txt", "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)


def decomp():
    with gzip.open('D:\\encrypted.txt.gz', "rb") as f_in:
        with open("D:\\encrypted.txt", "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
decomp()
print("decompression time: ")
print("--- %s seconds ---" % (time.time()-starttime))
def decryp():
    input_file = 'D:\\encrypted.txt'  # the input file
    input2 = 'outputfile.txt.gz'
    input3 = 'outputfile.txt'
    key = encryption_testing.key

    # read the data from the file
    file_in = open(input_file, 'rb')
    iv = file_in.read(16)  # read the iv out, and note that it is 16 bytes long
    ciphered_data = file_in.read()  #read the rest of the data
    file_in.close()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)  # setup the cipher
    original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)

    ##print(original_data)
    input_filewrite = open(input_file, "wb")
    input_filewrite.write(original_data)

decryp()

print("decryption time: ")
print("--- %s seconds ---" % (time.time()-starttime))