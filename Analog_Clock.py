import numpy as np
import cv2
import math
from time import sleep
from datetime import datetime

    
# variables 
center = (400,400)
center_point = 400 
radius = 270
window_size = (800,800,3)
font = cv2.FONT_HERSHEY_SIMPLEX
red = (0,0,255)
blue = (255,105,65)
white = (255,255,255)
crimson = (60,20,220)
firebrick = (34,34,178)

gray = (105,105,105)
start_point=[]
end_point= []


while (1):
    img = np.zeros(window_size, np.uint8)
    now = datetime.now()
    
    # put Date
    cv2.putText(img, 'Date: ', (3, 40), cv2.FONT_HERSHEY_TRIPLEX, 1.2, firebrick, 2, cv2.FILLED)
    date_string = now.strftime("%d/%m/%Y")
    cv2.putText(img, date_string , (130, 40), cv2.FONT_HERSHEY_TRIPLEX, 1.2, crimson, 2, cv2.FILLED)
    
    
    # put Time
    cv2.putText(img, 'Time: ', (3, 90), cv2.FONT_HERSHEY_TRIPLEX, 1.2, firebrick, 2, cv2.FILLED)
    time_string = now.strftime("%H:%M:%S")
    cv2.putText(img, time_string , (130, 90), cv2.FONT_HERSHEY_TRIPLEX, 1.2, crimson, 2, cv2.FILLED)
    
    
    # clock components
    cv2.circle(img, center, radius, white, 2)    # clock shape
    cv2.circle(img, center, 1, (255,105,65), 13)  # center point
    
    
    # hours points
    # make 12 , 3 , 6 , 9
    for i in range(0,360,90):
        x = int((400 + radius * math.cos(math.radians(i))))
        y = int((400 + radius * math.sin(math.radians(i))))
        cv2.circle(img, (x,y), 3, blue, 8)
        
    # make 1 , 2 , 4 , 5 , 7 , 8 , 10 , 11
    for i in range(0,360,30):
        x = int((400 + radius * math.cos(math.radians(i))))
        y = int((400 + radius * math.sin(math.radians(i))))
        cv2.circle(img, (x,y), 2, blue, 3)
        

    # minutes points
    i = 0 
    for i in range(0,360,6):
        x_start = int((400 + radius * math.cos(math.radians(i))))
        y_start = int((400 + radius * math.sin(math.radians(i))))
        start_point.append((x_start,y_start))
        
    for i in range(0,360,6):
        x_end = int((400 + (radius-15) * math.cos(math.radians(i))))
        y_end = int((400 + (radius-15) * math.sin(math.radians(i))))
        end_point.append((x_end,y_end))
        
    for i in range(len(start_point)):
        if i % 5 == 0:
            if i % 3 ==0:
                cv2.line(img, start_point[i], end_point[i], blue, 12)
            else:
                cv2.line(img, start_point[i], end_point[i], blue, 4)
        else:
            cv2.circle(img, start_point[i], 5, gray, -1)
        
        
    # draw the clock numbers 12,3,6,9
    cv2.putText(img, '12', (360, 210), font, 2, white, 5, cv2.FILLED)
    cv2.putText(img, '3', (600, 420), font, 2, white, 5, cv2.FILLED)
    cv2.putText(img, '6', (380, 630), font, 2, white, 5, cv2.FILLED)
    cv2.putText(img, '9', (160, 420), font, 2, white, 5, cv2.FILLED)

        
    # get the time
    now = datetime.now()
    hour = math.fmod(now.hour, 12)
    minute = now.minute
    second = now.second
    
    
    # get the angle of Clock’s hands
    hour_angle = math.fmod((hour*30) + (minute/2) + 270, 360)
    minute_angle = math.fmod(minute * 6 + 270, 360)
    second_angle = math.fmod(second * 6 + 270, 360)
    
    
    # draw Clock’s hands for hours
    hour_x = int(center_point + (radius-100) * math.cos(hour_angle * math.pi / 180))
    hour_y = int(center_point + (radius-100) * math.sin(hour_angle * math.pi / 180))
    cv2.line(img, center, (hour_x, hour_y), white, 7)
    
    # draw Clock’s hands for minutes
    minute_x = int(center_point + (radius-60) * math.cos(minute_angle * math.pi / 180))
    minute_y = int(center_point + (radius-60) * math.sin(minute_angle * math.pi / 180))
    cv2.line(img, center, (minute_x, minute_y), gray, 3)
    
    # draw Clock’s hands for seconds
    second_x = int(center_point + (radius-25) * math.cos(second_angle * math.pi / 180))
    second_y = int(center_point + (radius-25) * math.sin(second_angle * math.pi / 180))
    cv2.line(img, center, (second_x, second_y), red, 2)

    
    cv2.imshow('Clock', img)
    # to close the window prees 'q'
    if (cv2.waitKey(1) == ord('q')):
        break
    
    
cv2.destroyAllWindows()
