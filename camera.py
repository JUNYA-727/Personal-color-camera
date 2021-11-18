import cv2
from tensorflow import keras
capture=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
model = keras.models.load_model('personal_color_model1.h5')
while True:
    ret,img=capture.read()
    
    color= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    face_rectangle=(255,255,255)
    
    faces=face_cascade.detectMultiScale(color,1.1,5)
    
    for a,(x,y,w,h) in enumerate(faces):
        #cv2.rectangleの第1引数は画像(今回はフレーム)になる｡第2引数は左上頂点の座標(x,y)､第3引数は右下の座標を指す｡第4引数は色､第5引数は線の太さ｡
        cv2.rectangle(img,(x+20,y+30),(x+w-20,y+h),face_rectangle,1)
        #img[top : bottom, left : right]
        predict_face=img[y+30:y+h,x+20:x+w-20]
        predict_image=cv2.resize(predict_face,dsize=(300,300))
        predict_image=predict_image/255.0
        predict_image=predict_image.reshape(1,300,300,3)
        cv2.putText(img,text=('face'+str(a+1)),org=(x+20,y+27),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(255,255,255),thickness=1,lineType=cv2.LINE_4)
        scores=model.predict(predict_image)[0]
        predict=[]
        best=0
        for j,i in enumerate(scores):
            score=100*i
            predict.append(round(score,2))
            if best<i:
                best=i
                season=j
            else:
                continue

        if season==0:
            cv2.putText(img,text=('best_season:autumn'),org=(x+40,y-40),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.7,color=(0,255,0),thickness=1,lineType=cv2.LINE_4)
        elif season==1:
            cv2.putText(img,text=('best_season:spring'),org=(x+40,y-40),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.7,color=(0,255,0),thickness=1,lineType=cv2.LINE_4)
        elif season==2:
            cv2.putText(img,text=('best_season:summer'),org=(x+40,y-40),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.7,color=(0,255,0),thickness=1,lineType=cv2.LINE_4)
        elif season==3:
            cv2.putText(img,text=('best_season:winter'),org=(x+40,y-40),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.7,color=(0,255,0),thickness=1,lineType=cv2.LINE_4)
            
        cv2.putText(img,text=('spring:'+str(predict[1])+'%'),org=(x+80,y-20),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0,255,0),thickness=1,lineType=cv2.LINE_4)
        cv2.putText(img,text=('summer:'+str(predict[2])+'%'),org=(x+80,y-5),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0,255,0),thickness=1,lineType=cv2.LINE_4)
        cv2.putText(img,text=('autumn:'+str(predict[0])+'%'),org=(x+80,y+10),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0,255,0),thickness=1,lineType=cv2.LINE_4)
        cv2.putText(img,text=('winter:'+str(predict[3])+'%'),org=(x+80,y+25),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0,255,0),thickness=1,lineType=cv2.LINE_4)
    cv2.imshow('img',img)
    #キーボードの'q'を押して終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
cv2.waitKey(1)