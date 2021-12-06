import sys
import os
import json
import main 
from fsplit.filesplit import Filesplit

def split_cb(f, s):
    print("file: {0}, size: {1}".format(f, s))
    
def cat(obj,input_file):
    #obj.blocksize
    #obj.num_datanodes
    #using hashing algorithm split input file based on blocksize and store each split inside hased datanode
    # f = open(input_file,"r")
    # data = f.read()
    # print(data)
    fs = Filesplit()
    input_file_size = os.path.getsize(input_file)
    hashed_datanode = input_file_size % 2
    for i in range(1,obj.num_datanodes+1):
       d=str(i)
       hashed_datanode_dir = obj.path_to_datanodes+"datanode"+d

    fs.split(file=input_file,split_size=obj.block_size,output_dir=hashed_datanode_dir,callback=split_cb)