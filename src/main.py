import sys
import os

class Setup():
    def __init__(self, file_path):
        self.file_path = file_path
 
    def read_data(self):
        print('inside func')
        file = open(self.file_path,'r')
        self.data = file.read()
        print(self.data)
        file.close()
 
 
if __name__ == '__main__':
    # Now from outside give path and filename
    #file_path = 'config_sample.json'
    file_input = sys.argv[1]
    setup_obj = Setup(file_input)
    setup_obj.read_data()
    print(file_input)
    #print(setup_obj.data)