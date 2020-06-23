from ftplib import FTP
import os

# Change these
VIDEO_TO_PROCESS = "videoName"
FTP_SERVER_ADDRESS = "mywebserver.ddns.net"
INTERPOLATION_TIME_STEP = 0.125

# Don't change these
LOCAL_INPUT_DIR = "/content/MVIMP/Data/Input"
LOCAL_OUTPUT_DIR = "/content/MVIMP/Data/Output"

# FTP login details - MAKE SURE TO SET: the FTP server's connection timeout to infinity
ftp = None
def connectFtp():
    global ftp
    ftp = FTP(FTP_SERVER_ADDRESS)
    ftp.login(user="collab",passwd='collab')


connectFtp()
# Go into input dir
files = ftp.nlst()
for file in files:
    if VIDEO_TO_PROCESS == file:
        ftp.cwd(file)

print(ftp.pwd())
ftp.cwd("in")
print(ftp.pwd())

def changeDirWithRetry(dirpath):
    global ftp
    success = False
    while success == False:
        try:
            ftp.cwd(dirpath)
            success = True
        except:
            try:
                prevWorkingDir = ftp.pwd()
                ftp.close()
                connectFtp()
                ftp.cwd(prevWorkingDir)
            except:
                pass


# For each input file in the input folder
for inputfile in ftp.nlst():
    print(inputfile)
    # Download input file from FTP server
    fileObject = open(LOCAL_INPUT_DIR + "/" + inputfile, 'wb')
    print(ftp.pwd() + "/" + inputfile)
    ftp.retrbinary('RETR %s' % ftp.pwd() + "/" + inputfile, fileObject.write)
    fileObject.close()
    # Run interpolation
    os.system('python3 inference_dain.py --input_video "' + inputfile + '" --time_step ' + INTERPOLATION_TIME_STEP)
    # Grab output
    changeDirWithRetry("..")
    changeDirWithRetry("out")
    for (dirpath, dirnames, filenames) in os.walk(LOCAL_OUTPUT_DIR):
        outputFilePath = dirpath + "/" + filenames[0]
        outputFile = open(outputFilePath, 'rb')
        ftp.storbinary('STOR ' + filenames[0], outputFile)
        outputFile.close()
        os.remove(outputFilePath)
    changeDirWithRetry("..")
    changeDirWithRetry("in")
