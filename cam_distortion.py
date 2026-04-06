import cv2
import numpy as np

def apply_undistort(image_path, K, dist):
    # 1. 이미지 로드
    img = cv2.imread(image_path)
    if img is None:
        print("이미지 경로를 확인해주세요.")
        return
    
    h, w = img.shape[:2]

    # 2. 최적의 카메라 행렬 계산 (보정 후 검은 여백을 조절하려면 1을 0으로 바꿔보세요)
    # 1: 모든 픽셀 보존(검은 영역 포함 가능), 0: 유효 픽셀 위주로 크롭
    new_K, roi = cv2.getOptimalNewCameraMatrix(K, dist, (w, h), 1, (w, h))

    # 3. 실제 왜곡 보정 수행 (미션 필수 함수 [cite: 17])
    undistorted = cv2.undistort(img, K, dist, None, new_K)

    # 4. (선택) 결과물 비교를 위해 두 이미지를 가로로 붙이기
    # 크기가 같아야 하므로 hstack을 사용합니다.
    comparison = np.hstack((img, undistorted))
    
    # 5. 결과 저장 및 출력
    cv2.imwrite('result.png', comparison)
    cv2.imshow('Before (Left) vs After (Right)', comparison)
    print("왜곡 보정 완료")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # ==========================================
    # 민규님이 성공적으로 구한 캘리브레이션 결과값 입력
    # ==========================================
    K = np.array([[1.92261898e+03, 0.00000000e+00, 1.09179010e+03],
                  [0.00000000e+00, 1.92659005e+03, 1.90848807e+03],
                  [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
    
    D = np.array([0.02342582, -0.09022107, 0.00024543, 0.00084367, 0.08888041])

    # 보정하고 싶은 원본 이미지 파일명 입력
    TARGET_IMAGE = "data.jpeg" 
    
    apply_undistort(TARGET_IMAGE, K, D)