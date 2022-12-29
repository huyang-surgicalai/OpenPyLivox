import struct
import os
if __name__ == '__main__':
    filepath=r'D:\code\livox_together\OpenPyLivox\3GGDJ150010298.bin'
    binfile = open(filepath, 'rb') #打开二进制文件
    size = os.path.getsize(filepath) #获得文件大小
    print(size)
    # for i in range(size):
    # data = binfile.read() #每次输出一个字节
    # print(data)
    binfile.close()
