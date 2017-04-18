import subprocess



def SendUSBSMS():

    ModemID = 4
    ModemID = str(ModemID)

    print subprocess.check_output(["sudo", "mmcli", "-m", ModemID, "--messaging-list-sms"])
    print subprocess.check_output(["sudo", "mmcli", "-m", ModemID, "--messaging-list-sms"])
    #del all SMS

    #subprocess.check_output(["sudo", "mmcli", "-m", ModemID, "--messaging-create-sms="text='Unknown Detected',number='+94789160106'""])



SendUSBSMS()
