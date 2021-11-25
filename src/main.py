import sys

#reading the config file to setup
print(sys.argv[1])
with open('config\config_sample.json', 'r') as f:
    contents = f.read()
print (contents)

file = open(sys.argv[1], 'r')
try:
    config_content = file.read()
    print (config_content)
finally:
    file.close()