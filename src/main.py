import sys
import os
import json
import setup

# Setup class
# Read input file path of congiuration file
# Setup HDFS and creat dfs_setup_config file

class YAH():
    def __init__(self, file_path):
        self.file_path = file_path
    

    def read_config(self):
        path = "/Users/milindakn/BD2_114_214_233_282/src"
        with open(self.file_path, "r") as jsonfile:
            data = json.load(jsonfile)
        return data
        #str_1 = data["fs_path"]
        #path_1 = path+str_1
        #os.mkdir(str_1)
        #f = open('/dfs_setup_config',"w")
        #for key in data:
         #   f.write(key+" : "+str(data[key])+"\n")
        #print('Setup Complete')
        #f.close
 
if __name__ == '__main__':
    # In CLI pass config file path as argument
    # If config file not passed, select as default file
    if len(sys.argv)==1 :
        file_input = "config_default.json"
        print("Setting up using default Configuration File")
    else:
        file_input = sys.argv[1]
        print("Setting up using "+ file_input +" Configuration File")
    yah_obj = YAH(file_input)
    config_dict = yah_obj.read_config()

    #Initializing setup object and creating directory.
    setup_obj = setup.Setup(config_dict)
    setup_obj.create_direc()

    print("Entering command line interface: ")

    while(True):
        initial_input = input("$$$ ")
        if(initial_input == 'cat'):
            #cat function
            print("In cat block")
        elif(initial_input == 'ls'):
            #ls function
            print("In ls block")
        elif(initial_input == 'put'):
            #put function
            print("In put block")
        elif(initial_input == 'mkdir'):
            #ls function
            print("In mkdir block")
        elif(initial_input == 'rm'):
            #ls function
            print("In rm block")
        elif(initial_input == 'rmdir'):
            #ls function
            print("In rmdir block")
        elif(initial_input == 'exit'):
            break
        else:
            print("command not found.")
        