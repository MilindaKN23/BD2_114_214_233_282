import sys
import os
import json
import commands
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
    try:
        setup_obj.create_direc()
    except FileExistsError:
        print("User already exits")
        os.chdir(setup_obj.fs_path.split("/")[1]+"/"+setup_obj.fs_path.split("/")[2])

    print("Entering command line interface: ")

    while(True):
        current_path = os.getcwd()
        initial_input = input(current_path+" $$$ ")
        command_input = initial_input.split(" ")[0]
        if(command_input == 'cat'):
            #cat function
            #arg should be input file
            print("In cat block")
            input_file = initial_input.split(" ")[1]
            commands.cat(setup_obj,input_file)
            print("outside cat")
        elif(command_input == 'ls'):
            curr_dir = os.getcwd()
            commands.ls(curr_dir)
        elif(command_input == 'put'):
            commands.put(setup_obj,initial_input.split(" ")[1])
            print("In put block")
        elif(command_input == 'mkdir'):
            curr_dir = os.getcwd()
            input_file = initial_input.split(" ")[1]
            commands.mkdir(curr_dir,input_file)
            print("In mkdir block")
        elif(command_input == 'rm'):
            curr_dir = os.getcwd()
            input_file = initial_input.split(" ")[1]
            commands.rm(input_file)
            print("In rm ")
        elif(command_input == 'rmdir'):
            curr_dir = os.getcwd()
            input_file = initial_input.split(" ")[1]
            commands.rmdir(input_file)
            #ls function
            print("In rmdir block")
        elif(command_input == 'exit'):
            exit()
        else:
            print("command not found.")
        