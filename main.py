#! /usr/bin/python2
import cv2
import time
from single_buoy_lib import Buoy


def run(name='test.avi'):
    buoy_obj = Buoy()
    buoy_obj.openSource(Buoy.SOURCE_TYPE['FILE'], name)
    start = time.time()
    fc = 0
    while buoy_obj.read():
        fc += 1
        buoy_obj.preprocess()
        res = buoy_obj.process()
        print("FPS: %.4f" % (fc/(time.time()-start)))
        if res.result_img is not None:
            cv2.imshow('res', res.result_img)
            cv2.waitKey(1)


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        run()
