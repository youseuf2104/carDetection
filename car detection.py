import time

import cv2

# Original github code from https://github.com/SarahZarei/Car-Detection
cap = cv2.VideoCapture('video.avi')

car_cascade = cv2.CascadeClassifier('cars.xml')

average = 0
entries = 0

# Run while detecting the video capture images
while (cap.isOpened()):
    start = time.time()
    # Read each frame where ret is a return boolean value(True or False)
    ret, frame = cap.read()
    # if return is true continue because if it isn't then frame is of NoneType in that case you cant work on that frame
    if ret:

        # Any preprocessing you want to make on the frame goes here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # See if preprocessing is working on the frame it should

        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow('frame', frame)

        # finally write your preprocessed frame into your output video
        # out_video.write(gray) # write the modifies frame into output video
        # to forcefully stop the running loop and break out, if it doesnt work use ctlr+c
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # Display the timm needed for the current frame capture
        elapsed = time.time() - start
        print('Time for Frame: {:.3f} ms'.format(elapsed * 1000.0))
        average += elapsed * 1000.0
        entries = entries + 1
    # break out if frame has return NoneType this means that once script encounters such frame it breaks out
    # You will get the error otherwise
    else:
        break

# Added to display the average frame rate time
print('Average for Frames: {:.3f} ms'.format(average / entries))
cv2.destroyAllWindows()
