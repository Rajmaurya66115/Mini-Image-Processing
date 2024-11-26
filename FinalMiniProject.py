import pytesseract
import cv2
from gtts import gTTS
#import os
##import musicplayer
from playsound import playsound
#import ssl
#sl._create_default_https_context=ssl._create_unverified_context
import pyttsx3

cap=cv2.VideoCapture(0)

while(cap.isOpened()):
  status,frame=cap.read()                                          # Live Camera Text Detection 
  cv2.imshow('frame',frame)
  if cv2.waitKey(1)==ord('s'):                                                
   cv2.imwrite('Captain.png',frame)
   break
cap.release()
cv2.destroyAllWindows() 
img=cv2.imread(r'E:\Users\raj\Desktop\Python\Miniproject\Captain.png')

#img=cv2.imread(r'E:\Users\raj\Desktop\Python\Miniproject\Captain.png')

#cv2.imshow('Frame',img)
#cv2.waitKey(0)"""


#pytesseract.pytesseract_cmd="E:\\Program Files\\Tesseract-OCR\\tesseract.exe"
#cvtimg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#print(img)
#cv2.imshow('Frame',img)
#cv2.waitKey(2000)
#text=pytesseract.image_to_string(img)
#img_path=r"E:\Users\raj\Desktop\Python\Miniproject\test2.png"
mytext=pytesseract.image_to_string(img)
print(mytext)

boxes=pytesseract.image_to_boxes(img)
hIMG,wIMG,Channels=img.shape
for _,b in enumerate(boxes.splitlines()):
    b=b.split(' ')
    #print(b)
    x,y,h,w=int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,hIMG-y),(h,hIMG-w),(250,0,0),1)
    text=b[0]
    font=cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img,text,(x-20,hIMG-y-20),font,0.50,(0,187,255),1)
"""for t in enumerate(boxes.splitlines()):
 #t=t.split(' ')  
 print(t)
"""
cv2.imshow("frame",img)
cv2.waitKey(3000)
engine=pyttsx3.init()
rate=engine.getProperty("rate")
engine.setProperty("rate",150)
engine.say(mytext)
engine.runAndWait()
input()
#language='en'
#tts=gTTS(text=mytext,lang=language,slow=False)
#tts.save('Mini.mp3')
#playsound(gtts.gTTS(tts))

##os.system('start Mini.mp3')
#playsound('Mini.mp3')