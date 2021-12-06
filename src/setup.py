import sys
import os
import json
import main
import commands

class Setup():
        def __init__(self, config_dict):
            #Extraction of configuration details 
            self.block_size = config_dict["block_size"]
            self.path_to_datanodes = config_dict["path_to_datanodes"]
            self.path_to_namenodes = config_dict["path_to_namenodes"]
            self.replication_factor = config_dict["replication_factor"]
            self.num_datanodes = config_dict["num_datanodes"]
            self.datanode_size = config_dict["datanode_size"]
            self.sync_period = config_dict["sync_period"]
            self.datanode_log_path = config_dict["datanode_log_path"]
            self.namenode_log_path = config_dict["namenode_log_path"]
            self.namenode_checkpoints = config_dict["namenode_checkpoints"]
            self.fs_path = config_dict["fs_path"]
            self.dfs_setup_config = config_dict["dfs_setup_config"]
            self.datanode_dict = {}
            self.datanodename_list=[]

        def create_direc(self):
            #Creating a directory for each user
            user = self.fs_path.split("/")[2]
            home_dir = self.fs_path.split("/")[1]
            os.mkdir(home_dir+"/"+user)
            print("created directory for"+user)

            #Creating datanode dir
            datanode_dir = self.path_to_datanodes.split("/")[3]
            os.mkdir(home_dir+"/"+user+"/"+datanode_dir)

            #creating namenode dir
            namenode_dir = self.path_to_namenodes.split("/")[3]
            os.mkdir(home_dir+"/"+user+"/"+namenode_dir)

            #creating datanodes within the datanode directory
            create_datanodes(self,self.num_datanodes,self.datanode_size,user,datanode_dir,home_dir,self.datanode_dict,self.datanodename_list)
            print("Succesfully Created Datanodes")

            #creating namenode within the namenode directory
            create_namenode(namenode_dir)
            print("Succesfully Created Namenode")

            #Success
            print('Setup Complete')
        
        def setdatanode(self,d,l):
            self.datanode_dict=d
            self.datanodename_list=l

def create_datanodes(self,num_datanodes, datanode_size, user,datanode_dir,home_dir,datanode_dict,datanodename_list):
    os.chdir(home_dir+"/"+user+"/"+datanode_dir)
    for i in range(1,num_datanodes+1):
        s = str(i)
        os.mkdir("datanode"+s)
        datanode_dict["datanode"+s]=datanode_size
        datanodename_list.append("datanode"+s)
    print(datanodename_list)
    print(datanode_dict)
    self.setdatanode(datanode_dict,datanodename_list)
    
    

def create_namenode(namenode_dir):
    os.chdir("../"+namenode_dir)
    namenode_dict = {
        "key":"value"
    }
    json_object = json.dumps(namenode_dict)
    with open("namenode.json", "w") as outfile:
        outfile.write(json_object)
    os.chdir("../")

def setup_cat():
    print("In setup_cat")