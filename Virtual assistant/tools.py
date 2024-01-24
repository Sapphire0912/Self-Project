import cv2
import numpy as np

path = "E:\\Self-Project\\Virtual assistant\\pic_icon\\kokomi_shortkey_window.png"
img = cv2.imread(path)
img = cv2.resize(img, (50, 50), cv2.INTER_AREA)
cv2.imwrite("E:\\Self-Project\\Virtual assistant\\pic_icon\\kokomi_shortkey_window_re.png", img)

# img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

# # 檢查圖片是否有透明度通道
# if img.shape[2] == 4:
#     # 提取透明度通道
#     alpha = img[:, :, 3]
#
#     # 將透明度通道乘以0.5（降低透明度）
#     new_alpha = alpha * 0.7
#
#     # 將新的透明度通道設定回圖片
#     img[:, :, 3] = new_alpha
#
#     # 保存調整透明度後的圖片
#     cv2.imwrite("E:\\Self-Project\\Virtual assistant\\background\\v1_0_kokomi2_re.png", img)
#
# else:
#     print("圖片沒有透明度通道！")
