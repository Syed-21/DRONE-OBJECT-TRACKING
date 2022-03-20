import time

from djitellopy import Tello
import cv2

width = 320
height =240
startcounter = 1  # 0 for flight 1 for just testing the drone and the algorithm

me = Tello()
me.connect()
me.for_back_velocity = 0
me.left_right_velocity = 0
me.yaw_velocity = 0
me.speed = 0

print(me.get_battery())
me.streamoff()
me.streamon()

while True:
    frame_read = me.get_frame_read()
    myFrame = frame_read.frame
    img = cv2.resize(myFrame,(width,height))

    if startcounter == 0:
        me.takeoff()
        time.sleep(8)
        me.rotate_clockwise(90)
        time.sleep(3)
        me.move_left(35)
        time.sleep(3)
        me.land()
        startcounter = 1

    if me.send_rc_control:
        me.send_rc_control(me.left_right_velocity,me.for_back_velocity,me.up_down_velocity,me.yaw_velocity)


    cv2.imshow('myresult',img)

    if cv2.waitKey(1)&0xFF == ord('q'):
        me.land()
        break