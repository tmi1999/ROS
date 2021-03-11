#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from math import radians

PI = 3.1415926535897
speed = 3
angular_speed = PI

def forward(vel_pub, vel_msg, distance):
    if distance > 0:    
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    distance = abs(distance)

    while(current_distance < distance):
        vel_pub.publish(vel_msg)
        t1=rospy.Time.now().to_sec()
        current_distance= speed*(t1-t0)
    #stop
    vel_msg.linear.x = 0
    vel_pub.publish(vel_msg)
    
def rotate(vel_pub, vel_msg, angle):
    if angle > 0:
        vel_msg.angular.z = abs(angular_speed)
    else:
        vel_msg.angular.z = -abs(angular_speed)
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0
    relative_angle = radians(abs(angle))

    while(current_angle < relative_angle):
        vel_pub.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)
    #stop
    vel_msg.angular.z = 0
    vel_pub.publish(vel_msg)
    
def curve(vel_pub, vel_msg, distance, clockwise):
    if distance > 0:    
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
        
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    distance = abs(distance)

    while(current_distance < distance):
        vel_pub.publish(vel_msg)
        t1=rospy.Time.now().to_sec()
        current_distance= speed*(t1-t0)
    #stop
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    vel_pub.publish(vel_msg)

def move():
    rospy.init_node('robot_cleaner', anonymous=True)
    vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    print("Let's move your robot")

    curve(vel_pub, vel_msg, 5, 1)
    rotate(vel_pub, vel_msg, 90)
    forward(vel_pub, vel_msg, 2)
    rotate(vel_pub, vel_msg, 80)
    forward(vel_pub, vel_msg, 1)
    curve(vel_pub, vel_msg, -4, 0)
    rotate(vel_pub, vel_msg, -130)
    forward(vel_pub, vel_msg, 6)
    rotate(vel_pub, vel_msg, -100)
    forward(vel_pub, vel_msg, 3)

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass