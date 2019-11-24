from HardwareManager.HardwareManager import HardwareManager
import cv2
hardwareManager =  HardwareManager()

while(True):
    hardwareManager.update()
    cv2.waitKey(100)