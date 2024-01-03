import os
import time

print("THIS IS THE MAGIC SHOWER")
n = input("ENTER ANY NUMBER TO SEE THE MAGIC: ")


def stop():
    return os.system("shutdown -a")
def shutdown():
    return os.system("shutdown -h now")
def restart():
    return os.system("shutdown -h now")
if n:
    shutdown()
    exit()
