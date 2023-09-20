import cv2

img_src = "company.jpeg"
img = cv2.imread(img_src,cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(img_src, cv2.IMREAD_UNCHANGED)
img3 = cv2.imread(img_src,cv2.IMREAD_COLOR )

# cv2.IMREAD_GRAYSCALE
# cv2.IMREAD_UNCHANGED
# cv2.IMREAD_COLOR

cv2.imshow("company image", img)
cv2.imshow("company image2", img2)
cv2.imshow("company image3", img3)

cv2.waitKey()
cv2.destroyAllWindow()
