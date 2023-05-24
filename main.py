from Lumina.lumina import Lumina
import numpy as np
import cv2
from Lumina.colors import color_palette


color = color_palette()
lumina = Lumina()

if __name__ == '__main__':
    im = np.ones((512,512,3))
    bbox = [20,100,400,300]
    lumina.circle(im,color,radius=15,thickness=-1,colors=color,)
    lumina.cornerRect(im,bbox,color)
    cv2.imshow('im',im)
    cv2.imwrite('im.jpg',im)
    cv2.waitKey(0)
