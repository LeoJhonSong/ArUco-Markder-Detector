import cv2


# read calibration file
calibration = cv2.FileStorage("./charuco_camera_calibration.yaml", cv2.FILE_STORAGE_READ)
camera_matrix = calibration.getNode("camera_matrix").mat()
dist_matrix = calibration.getNode("distortion_coefficients").mat()
calibration.release()
# print("camera_matrix : ", camera_matrix.tolist())
# print("dist_matrix : ", dist_matrix.tolist())

# read video stream and detect

if __name__ == '__main__':
    cap = cv2.VideoCapture('./test.mkv')
    marker = {}

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ((cv2.waitKey(1) & 0xFF == 27) or ret is False):  # 按ESC退出
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # set for ArUco
        aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
        param = cv2.aruco.DetectorParameters_create()
        param.adaptiveThreshConstant = 10

        # 四个角为由左上起顺时针排序
        corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=param)

        if (ids is not None):
            rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners, 0.05, camera_matrix, dist_matrix)
            for i in range(ids.size):
                cv2.aruco.drawAxis(frame, camera_matrix, dist_matrix, rvec[i], tvec[i], 0.1)
                moment = cv2.moments(corners[i])
                cx = moment['m10'] / moment['m00'] / frame.shape[1]
                cy = moment['m01'] / moment['m00'] / frame.shape[0]
                print('rotate vector: ', rvec[i], ' | translation vector', tvec[i], ' | position: ', cx, ', ', cy)

            cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        cv2.imshow('detector', frame)

    cap.release()
    cv2.destroyAllWindows()
