import sys
import os
import json
from typing import Sized
import main 
from fsplit.filesplit import Filesplit

def split_cb(f, s):
    print("file: {0}, size: {1}".format(f, s))
  
def put(obj,input_file):
    #obj.blocksize
    #obj.num_datanodes
    #using hashing algorithm split input file based on blocksize and store each split inside hased datanode
    # f = open(input_file,"r")
    # data = f.read()
    # print(data)
    fs = Filesplit()
    input_file_size = os.path.getsize(input_file)
    inputfile_no_of_blocks= input_file_size//obj.block_size
    print(input_file_size)
    print('entered fnc')
    while input_file_size>obj.block_size: 
        print('enterd while') 
        print(obj.datanodename_list) 
        print(obj.datanode_dict)
        for node in obj.datanodename_list:
            print('enterd for')
            print(node,obj.datanode_dict[node])
    
            if obj.datanode_dict[node]>= obj.block_size:
                print('enterd if')
                print(node)
                # fs.split(file=input_file,split_size=obj.block_size,output_dir=node,callback=split_cb)
                note = "split -b 64 %s %s."
                os.system(note)
                print('spkit done')
                print(node)
                obj.datanode_dict[node]-=obj.block_size
                input_file_size-= obj.block_size
    print('we out')
    # hashed_datanode = input_file_size % 2
    # for i in range(1,obj.num_datanodes+1):
    #    d=str(i)
    #    hashed_datanode_dir = obj.path_to_datanodes+"datanode"+d

    # fs.split(file=input_file,split_size=obj.block_size,output_dir=hashed_datanode_dir,callback=split_cb)


def ls(curr_dir):
    curr_dir = os.listdir(curr_dir)
    for i in curr_dir:
        print(i)


def mkdir(curr_dir,input_file):
     os.mkdir(curr_dir+"/"+input_file)

def rmdir(input_file):
    os.rmdir(input_file)


def rm(input_file):
    os.remove(input_file)

