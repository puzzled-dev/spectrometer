import cv2
import matplotlib.pyplot as plt
import numpy as np

capture = cv2.VideoCapture(0)

roi_selected = False

while True:
    ret, frame = capture.read()

    k = cv2.waitKey(1)

    if k & 0xFF == ord('s'):
        shape = cropped.shape
        dist = []
        for i in range(shape[1]):
            dist.append(np.mean(cropped[:, i][:, 0]) + np.mean(cropped[:, i][:, 1]) + np.mean(cropped[:, i][:, 2]))
        plt.plot(dist)
        plt.show()

    elif k & 0xFF == ord('r'):
        r = cv2.selectROI(frame)
        roi_selected = True

    elif k & 0xFF == ord('q'):
        break

    else:
        if roi_selected:
            cropped = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
            cv2.imshow('roi', cropped)
        else:
            cv2.imshow('frame', frame)

capture.release()
cv2.destroyAllWindows()
