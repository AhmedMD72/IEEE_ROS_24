import rospy
from geometry_msgs.msg import Pose2D
from std_msgs.msg import String
from frist_tutorial.msg import V2V

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    car_pub=rospy.Publisher('car_channel', V2V, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    passat_car=V2V()
    passat_car.name ="passat"
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


def callback(data):
   rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
def listener():
# In ROS, nodes are uniquely named. If two nodes with the same
# name are launched, the previous one is kicked off. The
# anonymous=True flag means that rospy will choose a unique
# name for our 'listener' node so that multiple listeners can
# run simultaneously.
  rospy. init_node( 'listener', anonymous=True) 
  #rospy.Subscriber("chatter", String, callback)
  car_pub=rospy.Publisher("car_channel",V2V,queue_size=10)
  passat_car_info =V2V()
  passat_car_info.name ="passat"
  passat_car_info.V2V
  rate = rospy.Rate(1)
  while not rospy.is_shutdown():
      car_pub.publish(passat_car_info)
      rate.sleep()
      
# spin() simply keeps python from exiting until this node is stopped
      rospy.spin()
if __name__ == '__main__':
     try:
        listener()
     except rospy.ROSInterruptException:
        pass
  