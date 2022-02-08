import cv2

done=False
while(True):
    vid=input("Enter path of Video with name : ")
    cap=cv2.VideoCapture(vid)
    ret, frame = cap.read()
    if (cap.isOpened()):
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        result = cv2.VideoWriter('Rotated_video.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, ( frame_height, frame_width),0)
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                image = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
                Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                result.write(Gray)
                if cv2.waitKey(1) & 0xFF == ord('s'):
                    break

            else:
                done=True
                cap.release()
                break

    if (done == True):
        print('Done')
        break
    else:
        print(done)
        print("Your path doesnot include any Video")








