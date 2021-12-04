import sys
import os
import json

# Setup class
# Read input file path of congiuration file
# Setup HDFS and creat dfs_setup_config file
class Setup():
    def __init__(self, file_path):
        self.file_path = file_path
 
    def read_config(self):
        with open(self.file_path, "r") as jsonfile:
            data = json.load(jsonfile)
        f = open('dfs_setup_config',"w")
        for key in data:
            f.write(key+" : "+str(data[key])+"\n")
        print('Setup Complete')
        f.close
 
if __name__ == '__main__':
    # In CLI pass config file path as argument
    # If config file not passed, select as default file
    if len(sys.argv)==1 :
        file_input = "config_default.json"
        print("Setting up using default Configuration File")
    else:
        file_input = sys.argv[1]
        print("Setting up using "+ file_input +" Configuration File")
    setup_obj = Setup(file_input)
    setup_obj.read_config()

