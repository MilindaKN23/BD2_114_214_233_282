import sys
import os
import json
import main

def Setup(config_dict):
        #Extraction of configuration details 
        block_size = config_dict["block_size"]
        path_to_datanodes = config_dict["path_to_datanodes"].split("/")
        path_to_namenodes = config_dict["path_to_namenodes"].split("/")
        replication_factor = config_dict["replication_factor"]
        num_datanodes = config_dict["num_datanodes"]
        datanode_size = config_dict["datanode_size"]
        sync_period = config_dict["sync_period"]
        datanode_log_path = config_dict["datanode_log_path"]
        namenode_log_path = config_dict["namenode_log_path"]
        namenode_checkpoints = config_dict["namenode_checkpoints"]
        fs_path = config_dict["fs_path"].split("/")
        dfs_setup_config = config_dict["dfs_setup_config"]

        #Creating a directory for each user
        user = fs_path[2]
        home_dir = fs_path[1]
        os.mkdir(home_dir+"/"+user)
        print("created directory for"+user)

        #Creating datanode dir
        datanode_dir = path_to_datanodes[3]
        os.mkdir(home_dir+"/"+user+"/"+datanode_dir)

        #creating namenode dir
        namenode_dir = path_to_namenodes[3]
        os.mkdir(home_dir+"/"+user+"/"+namenode_dir)

        #creating datanodes within the datanode directory
        create_datanodes(num_datanodes,datanode_size,user,datanode_dir,home_dir)
        print("Succesfully Created Datanodes")

        #creating namenode within the namenode directory
        create_namenode(namenode_dir)
        print("Succesfully Created Namenode")

        #Success
        print('Setup Complete')

def create_datanodes(num_datanodes, datanode_size, user,datanode_dir,home_dir):
    os.chdir(home_dir+"/"+user+"/"+datanode_dir)
    for i in range(1,num_datanodes+1):
        s = str(i)
        f = open("datanode"+s,"w")
        f.write("hello")
    

def create_namenode(namenode_dir):
    os.chdir("../"+namenode_dir)
    namenode_dict = {
        "key":"value"
    }
    json_object = json.dumps(namenode_dict)
    with open("namenode.json", "w") as outfile:
        outfile.write(json_object)