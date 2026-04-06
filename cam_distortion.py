import cv2
import numpy as np

def apply_undistort(image_path, K, dist):
    img = cv2.imread(image_path)
    if img is None:
        print("이미지 경로를 확인해주세요.")
        return
    
    h, w = img.shape[:2]
    new_K, roi = cv2.getOptimalNewCameraMatrix(K, dist, (w, h), 1, (w, h))
    undistorted = cv2.undistort(img, K, dist, None, new_K)
    comparison = np.hstack((img, undistorted))
    
    # 5. 결과 저장 및 출력
    cv2.imwrite('result.png', comparison)
    cv2.imshow('Before (Left) vs After (Right)', comparison)
    print("왜곡 보정 완료")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    K = np.array([[1.92261898e+03, 0.00000000e+00, 1.09179010e+03],
                  [0.00000000e+00, 1.92659005e+03, 1.90848807e+03],
                  [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
    
    D = np.array([0.02342582, -0.09022107, 0.00024543, 0.00084367, 0.08888041])

    TARGET_IMAGE = "data.jpeg" 
    
    apply_undistort(TARGET_IMAGE, K, D)