import gzip
import encryption_testing
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import shutil
import time
fatData = "C:\\Users\\samja\\Downloads\\2018-09-19_IMU\\2018-09-19-03_57_11_VN100.csv"

startTime = time.time()


original = r'C:\Users\samja\Documents\MATLAB\outputfile.txt'
target = r'C:\Users\samja\PycharmProjects\pythonProject\outputfile.txt'
shutil.copyfile(original, target)

#compressing the data.txt file
#with open('outputfile.txt', 'rb') as f_in, gzip.open('outputfile.txt.gz', 'wb') as f_out:
    #shutil.copyfileobj(f_in,f_out)

#compression attempt number 2
fp = open('outputfile.txt', 'rb')
readData = fp.read()
bindata = bytearray(readData)
with gzip.open('outputfile.txt.gz','wb') as f:
    f.write(bindata)
    f.close()

print("Compression time:")
print("--- %s seconds ---" % (time.time()-startTime))


# generating the key
key = get_random_bytes(32) #note that 1 byte = 8 bits
print(key)

# storing the key
key_location = "D:\\keyting.txt"

# save the key to a file
file_out = open(key_location, "wb")
file_out.write(key)
file_out.close()

# later on...assuming that we no longer have the key
file_in = open(key_location, "rb")
key_from_file = file_in.read()
file_in.close()

# verifying that these keys are indeed the same
assert key == key_from_file, 'keys dont match'

# Now that we have a file, we can start encrypting.
output_file = 'D:\\encrypted.txt'  # output file
output2 = 'outputfile.txt.gz'
output3 = 'outputfile.txt'

#The old method (works):
#with gzip.open("outputfile.txt.gz","r") as myfile:
    #d = myfile.readlines()
#d2 = str(d)  # change to a string
#d3 = d2.encode()  # encode it to change it to bytes

#secondary method:
with gzip.open('outputfile.txt.gz', 'rb') as myfile:
    bindata = myfile.read()



# using the big data file:

#with open(fatData, "r") as fatfile:
#    f = fatfile.readlines()
#f2 = str(f)
#f3 = f2.encode()

#data11 = "1234 hello world"  # string of data
#data11.encode()  # .encode() changes string object to a byte object
#stringdata = "1234 hello worlds"



# Create the cipher object and encrypt the data
cipher = AES.new(key, AES.MODE_CBC)  # Create an AES cipher object with the key using the mode CBC
ciphered_data = cipher.encrypt(pad(bindata, AES.block_size))


file_out = open(output3, "wb")  # Open file to write bytes
file_out.write(cipher.iv)  # Write the iv to the output file
file_out.write(ciphered_data)  # write the ciphertext to the file ( this is the encrypted data)
file_out.close()

FOutput3 = open("outputfile.txt","rb")
readData2 = FOutput3.read()
bindata2 = bytearray(readData2)
with gzip.open('outputfile.txt.gz','wb') as f2:
    f2.write(bindata2)
    f2.close()






#print("encryption time: ")
#print("--- %s seconds ---" % (time.time()-startTime))

#compressing the data.txt file
#with open('D:\\encrypted.txt', 'rb') as f_in, gzip.open('D:\\encrypted.txt.gz', 'wb') as f_out:
    #shutil.copyfileobj(f_in,f_out)

#attempting to compress the encryption.txt file properly
def encryptionCompress():

    fe = open('D:\\encrypted.txt', 'rb')
    read_en_data = fe.read()
    bin2data = bytearray(read_en_data)
    with gzip.open('D:\\encrypted.txt.gz', 'wb') as EnData:
        EnData.write(bin2data)
        EnData.close()
#encryptionCompress()

print("Total program completion ")
print("--- %s seconds ---" % (time.time()-startTime))