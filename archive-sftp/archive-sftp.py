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
def main():
    # Open sFTP Connection
    SFTPSRV = pysftp.Connection(host=SFTPHOST, username=SFTPUSERNAME, password=SFTPPASSWORD)
    # Build SRC file dictionary
    SRCFILES = glob.glob(SOURCE)

    # Process Docs
    for FILE in SRCFILES:
        FULLNAME = os.path.join(SOURCE, FILE)
        print(FULLNAME)
        if (os.path.isfile(FULLNAME)):
            # Copy all files to new destination
            shutil.copy(FULLNAME, DESTINATION)

            # FTP to server
            SFTPSRV.put(FULLNAME)

            # Check if file uploads and then remove
            if(SFTPSRV.exists(FILE):
                # cleanup files
                os.remove(FULLNAME)
                print("File Upload Completed")
                
    SFTPSRV.close()

if __name__ == '__main__':
    main()
