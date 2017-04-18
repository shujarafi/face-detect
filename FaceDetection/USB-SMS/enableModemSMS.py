import subprocess



print "Please Run This Script as Root. eg: root@shuja-linux"

ModemID = raw_input("Enter Your USB Modem ID ")

print subprocess.check_output(["sudo", "mmcli", "-m", ModemID, "-e"])

