import cv2

img_src = "company.jpeg"
img_dst = "company_result.jpeg"

img = cv2.imread(img_src, cv2.IMREAD_GRAYSCALE)

if img is not None:
    cv2.imshow("image", img)
    cv2.imwrite(img_dst, img)
else:
    print("이미지가 정상적으로 불러오지 않았습니다.")

cv2.waitKey()
cv2.destroyAllWindows()