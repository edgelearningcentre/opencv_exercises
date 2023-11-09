import cv2
import matplotlib.pyplot as plt
cb_img = cv2.imread("checkerboard_color.png")
coke_img = cv2.imread("coca-cola-logo.png")



# using matplot lib imshow function
# plt.imshow(cb_img)
# plt.title("matplotlib imshow")
# plt.show()

# use opencv imshow display for 8 seconds
# window1 = cv2.namedWindow("w1")
# cv2.imshow(window1,cb_img)
# cv2.waitKey(8000)
# cv2.destroyWindow(window1)


window4  = cv2.namedWindow("w4")
Alive = True
while Alive:
    cv2.imshow(window4,coke_img)
    keypress = cv2.waitKey(1)
    if keypress == ord('q'):
        Alive = False
cv2.destroyWindow(window4)
stop =1