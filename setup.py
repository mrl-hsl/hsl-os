import os

# cmd = 'mkdir ./SheardMemory/PyShm/Build'
# os.system(cmd)

cmd = 'cd ./SheardMemory/PyShm/Build;\
     cmake ..;\
     make;\
    mv pyShm.cpython-36m-x86_64-linux-gnu.so ../pyShm.so'
os.system(cmd)
