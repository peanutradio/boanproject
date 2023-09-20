import cv2

# 웹캠 열기
vfile = cv2.VideoCapture(0)

# 웹캠 열기가 성공했는지 확인
if vfile.isOpened():
    while True:
        # 프레임 읽어오기
        vret, img = vfile.read()
        if vret:
            # 읽어온 프레임을 화면에 표시
            cv2.imshow('webcam', img)
            key = cv2.waitKey(1)
            
            # 'q' 키를 누르면 종료
            if key == ord('q'):
                break
            
            # 's' 키를 누르면 이미지 저장
            if key == ord('s'):
                cv2.imwrite('webcam_snap.jpg', img)
                print("이미지 저장 완료")
        else:
            print("프레임 정상적이지 않음")
            break
else:
    print("오류 발생")

# 리소스 해제
vfile.release() # 비디오 값 반환.
cv2.destroyAllWindows()
