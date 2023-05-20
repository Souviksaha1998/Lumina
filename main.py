from Lumina.lumina import Lumina
import numpy as np
import cv2
from Lumina.colors import color_palette


color = color_palette()
lumina = Lumina()

if __name__ == '__main__':
    im = np.ones((512,512,4))
    bbox = [20,100,400,300]
    im = cv2.imread('crop_.jpg')
    c = (60,50)
    print(color)
    lumina.circle(im,c,radius=15,thickness=-1,colors=color,)
    im  = lumina.fillPolygon_create(im,[(523,337),(1240,321),(1277,590),(383,632)],transparency=0.7)
    # mask = lumina.create_mask(im,[[10,20],[50,80],[90,44],[55,11]])
    # print(detection)
    cv2.imshow('c',im)
    cv2.imwrite('5.jpg',im)
    # cv2.imshow('d',mask)
    cv2.waitKey(0)