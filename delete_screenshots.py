import os

os.chdir('/Users/arthurdamato/Desktop')
cwd = os.getcwd()

for file in os.listdir(cwd):
    if file.startswith('Screen Shot'):
        os.remove(file)