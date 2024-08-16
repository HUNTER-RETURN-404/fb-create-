import os,platform
os.system('git pull')
os.system("clear")
print('\033[92;1m ❲\033[97;1m+\033[92;1m❳ Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/Hf6WUhpV822AmZlGM6RA8P')
Hunter=platform.architecture()[0]
if Hunter=="32bit":
    os.system("clear");exit("\033[91;1m 32Bit Device Not Supported")
elif Hunter=="64bit":
    __import__("p64")
