from ftplib import FTP
import os
VIDEO_TO_PROCESS = "videoName"
LOCAL_INPUT_DIR = "/content/MVIMP/Data/Input"
LOCAL_OUTPUT_DIR = "/content/MVIMP/Data/Output"

def runAndPrintOutput(command):
    import subprocess
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True, shell=True)

    while True:
        output = process.stdout.readline()
        error = process.stderr.readline()
        print(output.strip())
        print(error.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output
            for output in process.stdout.readlines():
                print(output.strip())
            break

def changeDirWithRetry(ftpObj, dirpath):
    success = False
    while success == False:
        try:
            ftpObj.cwd(dirpath)
            success = True
        except:
            pass
# FTP login details - MAKE SURE TO SET: the FTP server's connection timeout to infinity
ftp = FTP('mywebserver.ddns.net')
ftp.login(user="collab",passwd='collab')

files = ftp.nlst()
for file in files:
    if VIDEO_TO_PROCESS == file:
        ftp.cwd(file)

print(ftp.pwd())

# Go into input dir
ftp.cwd("in")

print(ftp.pwd())

# For each input file in the input folder
for inputfile in ftp.nlst():
    print(inputfile)
    # Download input file from FTP server
    fileObject = open(LOCAL_INPUT_DIR + "/" + inputfile, 'wb')
    print(ftp.pwd() + "/" + inputfile)
    ftp.retrbinary('RETR %s' % ftp.pwd() + "/" + inputfile, fileObject.write)
    fileObject.close()
    # Run interpolation
    os.system('python3 inference_dain.py --input_video "' + inputfile + '" --time_step 0.125')
    # Grab output
    changeDirWithRetry(ftp,"..")
    changeDirWithRetry(ftp, "out")
    for (dirpath, dirnames, filenames) in os.walk(LOCAL_OUTPUT_DIR):
        outputFilePath = dirpath + "/" + filenames[0]
        ftp.storbinary('STOR ' + filenames[0], open(outputFilePath, 'rb'))
        os.remove(outputFilePath)
    changeDirWithRetry(ftp, "..")
    changeDirWithRetry(ftp, "in")



'''
files = []
ftp.dir(files.append)

for file in files:
    print(type(file))
    print(file)

'''