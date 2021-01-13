import os
import shutil
from pip._vendor.colorama import Fore, Style, init
import subprocess
import time

init()
src_dir = os.getcwd()
servicesList = ['<ServiceName>', '<ServiceName>', '<ServiceName>', '<ServiceName>', '<ServiceName>']


def copyloop(appdir, target):
    cp_source_dir = appdir
    cp_target_dir = target

    file_names = os.listdir(cp_source_dir)

    for file_name in file_names:
        shutil.copy2(os.path.join(cp_source_dir, file_name), cp_target_dir)


def stopServices(svcname):
    args = ['sc', 'stop', svcname]
    result = subprocess.run(args)


def startServices(svcname):
    args = ['sc', 'start', svcname]
    result = subprocess.run(args)

def colourText(textHere, colour):
    print(getattr(Fore, colour) + textHere + Style.RESET_ALL)

colourText("\n \t \t Welcome to Auto Patcher v.3", "RED")
colourText("\n \t ....Shutting down all Related Services....", "GREEN")


for svc in servicesList:
    stopServices(svcname=svc)

colourText("\n ....Waiting 5 Seconds....", "YELLOW")
time.sleep(5)

colourText("\n \t ....Patching the Supervisor Client Time Zone Files....", "BLUE")
copyloop(appdir=src_dir + '\\TT2018\\', target="C:\\test\\")
colourText("\n ....Supervisor Client Patched", "BLUE")

colourText("\n \t ....Patching DBSyncServer to 2018.40....", "BLUE")
copyloop(appdir=src_dir + '\\DBSyncServer\\', target="C:\\Testing\\DBSyncServer\\")
colourText("\n ....DBSyncServer Patched", "BLUE")

colourText("\n \t ....Patching DBSyncServerAdmin to 2018.40....", "BLUE")
copyloop(appdir=src_dir + '\\DBSyncAdmin\\', target="C:\\Testing\\DBSyncServerAdmin\\")
colourText("\n ....DBSyncServerAdmin Patched", "BLUE")

colourText("\n \t ....Patching AppService to 2018.40....", "BLUE")
copyloop(appdir=src_dir + '\\AppService\\', target="C:\\Testing\\AppService\\")
colourText("\n ....AppService Patched", "BLUE")

colourText("\n \t ....Patching the Web Portal....", "BLUE")

wp_source_dir = src_dir + "\\WebPortal\\"
wp_target_dir = 'C:\\Test\\WebPortal\\'

for source_dir, dirs, file_names in os.walk(wp_source_dir):
    target_dir = source_dir.replace(wp_source_dir, wp_target_dir, 1)

    for file_name in file_names:
        source_file = os.path.join(source_dir, file_name)
        target_file = os.path.join(target_dir, file_name)
        if os.path.exists(target_file):
            # in case of the source and target are the same file
            if os.path.samefile(source_file, target_file):
                continue
            os.remove(target_file)
        shutil.copy2(source_file, target_dir)

colourText("\n ....Web Portal Patched", "BLUE")

colourText("\n ....Waiting 5 Seconds....", "YELLOW")
time.sleep(5)

colourText("\n \t ....Starting all Related Services....", "GREEN")
for svc in servicesList:
    startServices(svcname=svc)

colourText("\n \t \t The v.3 Auto Patcher is Complete \n", "RED")

print("\n Made with ", Fore.RED + "<3", Style.RESET_ALL, "by Chuck Coggins \n")
input('Press ENTER to exit')
