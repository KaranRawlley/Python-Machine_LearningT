import cv2,time
import numpy as np
from asyncio.locks import Event

# x = True
# 
# video = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# out = cv2.VideoWriter('outpur.avi',fourcc,5.0,(640,480))
# def record():
#     video = cv2.VideoCapture(0)
#     fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#     out = cv2.VideoWriter('outpur.avi',fourcc,5.0,(640,480))
#     global x
#     while x:
#         check,frame =  video.read()
# #     print(check)
#     #print(frame)
#     
#         out.write(frame)
#         cv2.imshow('Capturing',frame)
# 
#         if x==False:
#             break
#     out.release()    
#     video.release()
#     cv2.destroyAllWindows()


        
    
    
    
def record():
    
    video = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('outpur.avi',fourcc,5.0,(640,480))
    
    
    while True:
        check,frame =  video.read()
#     print(check)
    #print(frame)
    
        out.write(frame)
        cv2.imshow('Capturing',frame)
    

        k = cv2.waitKey(1)
        if(k==ord('q')):
            break
        
            

        
    out.release()    
    video.release()
    cv2.destroyAllWindows()
        
        
record()

def play():
    cap = cv2.VideoCapture('outpur.avi')

    while True:

        ret, frame = cap.read()

        if ret == True:

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            cv2.imshow('frame',gray)


        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

        else:
            break

    cap.release()
    cv2.destroyAllWindows()
        
    
    