# camCali: Precision Lens Calibration & Distortion Correction

A robust computer vision tool designed to estimate intrinsic camera parameters and rectify lens distortion artifacts using OpenCV. This project implements Zhang's calibration method to achieve high-accuracy results for wide-angle and standard lenses.

## ✨ Key Features
* **Interactive Frame Selection**: Capture high-quality calibration frames from video streams in real-time.
* **Sub-pixel Corner Refinement**: Enhances corner detection precision using `cornerSubPix` for minimized re-projection errors.
* **Seamless Rectification**: Instant lens distortion correction based on computed camera matrices ($K$) and distortion coefficients ($D$).

## 📊 Calibration Performance

The calibration was conducted using a $9 \times 6$ chessboard pattern with a $20\text{mm}$ cell size. 

### 1. Accuracy Metric
* **Root Mean Square Error (RMSE)**: `0.99435`
> **Analysis**: An RMSE below $1.0$ confirms that the estimated parameters accurately represent the physical camera geometry with minimal pixel-level error.

### 2. Intrinsic Camera Matrix ($K$)
The intrinsic matrix encapsulates the focal length and optical center (principal point) of the lens:

$$K = \begin{bmatrix} 1922.61898 & 0 & 1091.79010 \\ 0 & 1926.59005 & 1908.48807 \\ 0 & 0 & 1 \end{bmatrix}$$

* **Focal Length ($f_x, f_y$)**: `1922.62`, `1926.59`
* **Principal Point ($c_x, c_y$)**: `1091.79`, `1908.49`

### 3. Distortion Coefficients ($D$)
Derived coefficients to compensate for radial and tangential lens artifacts:
* **Radial ($k_1, k_2, k_3$)**: `0.02343`, `-0.09022`, `0.08888`
* **Tangential ($p_1, p_2$)**: `0.00025`, `0.00084`

---

## 🖼️ Rectification Results (Demo)

The following demonstration highlights the transition from a distorted wide-angle perspective to a rectified linear perspective. 

| Original (Distorted) | Rectified (Undistorted) |
| ![Result](./result.png)|

> **Note**: As seen in the comparison, the "barrel distortion" common in wide-angle lenses is successfully eliminated, restoring the straight lines of the chessboard.
