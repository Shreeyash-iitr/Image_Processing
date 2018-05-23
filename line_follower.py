import cv2
import picamera
import picamera.array
import numpy
import RPi.GPIO as gpio

ml1 = 17
ml2 = 18
mr1 = 19
mr2 = 20
kpx = 0.5
kpa = 0.25
kdx = 0.4
kda = 0.2
motor_s = 250
corr =0
max_rpm = int(0.01*((kpx*150) + (kpa*90) + (kdx*10) + (kda*1) + 250))


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(ml1, gpio.OUT)
    gpio.setup(ml2, gpio.OUT)
    gpio.setup(mr1, gpio.OUT)
    gpio.setup(mr2, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(12, gpio.OUT)


def forward():
    gpio.output(ml1,True)
    gpio.output(ml2, False)
    gpio.output(mr1, True)
    gpio.output(mr2, False)


mr_pwm = gpio.PWM(11,100)
ml_pwm = gpio.PWM(12,100)




with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution = (300,400)
        pre_err_a = 0
        pre_err_x = 0
        mr_pwm.start(100)
        ml_pwm.start(100)
        while True:
            camera.capture(stream, 'bgr', use_video_port=True)
            frame = stream.array
            thresh = cv2.inRange(frame, (0,0,0), (70,70,70))
            kernel = numpy.ones((3,3),numpy.uint8)
            thresh = cv2.erode(thresh, kernel, 5)
            thresh = cv2.dilate(thresh, kernel, 9 )
            ret, contour, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
            cnt = contour[0]

            #making tilted rectangle to measure angle error
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = numpy.int0(box)
            cv2.drawContours(frame, [box], 0, (255,0,0), 2)
            if rect[1][0] < rect[1][1]:
                err_a = (rect[2])
                print('ANGLE : ' + str(err_a))
            else :
                err_a = (90+rect[2])
                print('ANGLE : ' + str(err_a))



            #making simple rectangle to find distance error
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255),2)
            cv2.line(thresh, (x + (w // 2), y), (x + (w // 2), y + h), (255, 0, 0), 2)
            err_x = (x+(w//2)-150)
            print('DISTANCE : ' + str(err_x))

            # calculating error and code for PID
            d_err_x = err_x - pre_err_x
            d_err_a = err_a - pre_err_a
            corr = (kpx*err_x) + (kpa*err_a) + (kdx*d_err_x) + (kda*d_err_a)
            pre_err_x = err_x
            pre_err_a = err_a
            lms_p = (motor_s + corr)//max_rpm
            rms_p = (motor_s - corr)//max_rpm
            forward()
            mr_pwm.ChangeDutyCycle(rms_p)
            ml_pwm.ChangeDutyCycle(lms_p)

            cv2.imshow('stream', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            stream.seek(0)
            stream.truncate()

        cv2.destroyAllWindows()









