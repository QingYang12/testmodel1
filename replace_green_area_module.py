import cv2
import numpy as np

# ...
image_path = os.path.join(script_dir, image_name)
image="t12.png";
# 转换颜色空间 BGR -> HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# 设定绿色的范围
lower_green = np.array([35, 50, 50])
upper_green = np.array([90, 255, 255])
# 对图像进行阈值分割，得到掩膜
mask = cv2.inRange(hsv, lower_green, upper_green)
# 将原图像中绿色区域替换为白色
result = image.copy()
result[mask > 0] = (255, 255, 255)