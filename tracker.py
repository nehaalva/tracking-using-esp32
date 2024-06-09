import cv2

cap = cv2.VideoCapture("http://172.16.27.57:81/stream")
x, frame = cap.read()

tracker = cv2.legacy.TrackerMOSSE_create()

bbox = cv2.selectROI('tracking', frame, False)

tracker.init(frame, bbox)


def draw(img, bbox):
    x, y, h, w = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x+h), (y+w)), (0, 0, 0), 2, 1)

while True:
    timer = cv2.getTickCount()

    x2, frame = cap.read()

    x1, bbox = tracker.update(frame)
    draw(frame, bbox)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(frame, str(int(fps)), (50, 50), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 0, 0), 1)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
