
(cl:in-package :asdf)

(defsystem "imu_vision_interaction-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "IMU_msg" :depends-on ("_package_IMU_msg"))
    (:file "_package_IMU_msg" :depends-on ("_package"))
    (:file "kinect_msg" :depends-on ("_package_kinect_msg"))
    (:file "_package_kinect_msg" :depends-on ("_package"))
  ))