import cv2
import dropbox
import time
import random
startTime=time.time()
def TakeSnapshot():
    number=random.randint(0,100)
    VideoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=VideoCaptureObject.read()
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        startTime=time.time()
        result=False
    return imageName
    print("Snapshot Taken")
    VideoCaptureObject.release()
    cv2.destroyAllWindows()
def upload_file(imageName):
    access_token = 'MtX788qTicYAAAAAAAAAAeufxWUkR0BaaRTUSz4QbJnK9NKlp6bviQNxR3p6tnZS'
    file=imageName
    fileFrom=file
    fileTo="/testFolder/"+(imageName)
    dbx = dropbox.Dropbox(access_token)
    with open(fileFrom,"rb")as f:
        dbx.files_upload(f.read(),fileTo,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
def main():
    while(True):
        if((time.time()-startTime)>=5):
            name=TakeSnapshot()
            upload_file(name)
main()



