import cv2

path = "./config/kokomi.txt"
f = open(path, 'r')
t = list()
for line in f.readlines():
    line = line.rstrip()
    t.append(line.split('=')[-1])

imgPath = t[-1]
print(imgPath)
img = cv2.imread(imgPath)
cv2.imshow('img', img)
cv2.waitKey(0)
