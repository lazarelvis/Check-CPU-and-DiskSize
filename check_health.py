# Checking CPU usage and disk space available on PC
import shutil
import psutil

#check the free space of the disk usage and there is 20% more of the disk usage is return a True
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

#check how much of the CPU is used and return a True statement if is less than 75%
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

# if both functions returns are True it will return "Everything is OK!" 
if not check_disk_usage("/") or not check_cpu_usage():
    print("Error!")
else:
    print("Everything is OK!")
