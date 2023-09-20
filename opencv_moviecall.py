import cv2
# print(cv2.__version__)

movie_file = "220314_새벽설교.mp4"
vfile = cv2.VideoCapture(movie_file)

if vfile.isOpened():
    while True:
        vret, img = vfile.read()
        if vret:
            cv2.imshow(movie_file, img)
            cv2.waitKey(25)
        else:
            break
else:
    print("파일을 열수 없습니다.")

vfile.release()
cv2.destroyAllWindows()

