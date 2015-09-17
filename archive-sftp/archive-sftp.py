# -*- coding: utf-8 -*-
import pysftp
import os
import shutil
import glob

#-----------------  GLOBAL VARIABLES -----------------#
# Source Folder Path
DESTINATION = ""

# Destinatino Folder Path
SOURCE = ""

# sFTP Host
SFTPHOST = ""

# sFTP Username
SFTPUSERNAME = ""

# sFTP Password
SFTPPASSWORD = ""

#---------------  END GLOBAL VARIABLES ----------------#

# File Archive Function
def archive():
    # Build SRC file dictionary
    SRCFILES = glob.glob(SOURCE)
    print(SRCFILES)
    # Copy all files to new destination
    for FILE in SRCFILES:
        FULLNAME = os.path.join(SOURCE, FILE)
        print(FULLNAME)
        if (os.path.isfile(FULLNAME)):
            shutil.copy(FULLNAME, DESTINATION)

            print("File Archive Completed")

#  sFTP Function
def sftp():

    # Open sFTP Connection
    SFTPSRV = pysftp.Connection(host=SFTPHOST, username=SFTPUSERNAME, password=SFTPPASSWORD)

    #Build SRC file dictionary
    SRCFILES = glob.glob(SOURCE)

    # Copy all files to the sFTP server
    for FILE in SRCFILES:
        FULLNAME = os.path.join(SOURCE, FILE)
        if (os.path.isfile(FULLNAME)):
            SFTPSRV.put(FULLNAME)

            # cleanup files
            os.remove(FULLNAME)

    print("File Upload Completed")
    SFTPSRV.close()

if __name__ == '__main__':
    archive()
    sftp()
