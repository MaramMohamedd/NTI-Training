import cv2

#reading the image 
image = cv2.imread(r"C:\Users\moham\OneDrive\Pictures\Saved Pictures\d40f78919dc20a8536bf1d9bd805e8b1.jpg")
image = cv2.resize(image , (500 ,500))
cv2.imshow("Dog" ,image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#converting its color
cvt_img = cv2.cvtColor(image , cv2.COLOR_RGB2GRAY )
cv2.imshow("converted to gray" ,cvt_img )
cv2.waitKey(0)
cv2.destroyAllWindows()

#saving
cv2.imwrite('nti.jpg' , cvt_img)

#drawing rec 
cv2.rectangle(image ,(100 ,100) , (200,200) , (100 ,100) )
cv2.putText(image ,'REXI' , (10 ,200), cv2.FONT_HERSHEY_TRIPLEX , 1 , (255 ,255 ,255) , 1)
cv2.imshow('rec' , image)
cv2.waitKey(0)
cv2.destroyAllWindows()
