#coding=utf-8
 
import os, sys, platform
 
os.system('xdg-open https://chat.whatsapp.com/')
 
try:
 
    if sys.argv[1]=='update':
 
        os.system('rm -rf BLACK.cpython-311.so BLACK.cpython-311.so')
 
except:
 
    pass
 
os.system('rm -rf BLACK.cpython-311.so BLACK.cpython-311.so')
 
os.system('git pull')
 
bit = platform.architecture()[0]
 
if bit == '64bit':
 
    if not os.path.isfile('BLACK.cpython-311.so'):
 
        os.system('curl https://github.com/SokAlike/BLACK/blob/main/BLACK.cpython-311.so > BLACK.cpython-311.so') 
 
        os.system("chmod 777 BLACK64*")
 
        import BLACK64
 
    else:
 
        import BLACK64
 
elif bit == '32bit':
 
    if not os.path.isfile('BLACK.cpython-311.so'):
 
        os.system('curl https://github.com/SokAlike/BLACK/blob/main/BLACK.cpython-311.so > BLACK.cpython-311.so')
 
        os.system("chmod 777 BLACK32*")
 
        import BLACK
 
    else:
 
        import BLACK
 