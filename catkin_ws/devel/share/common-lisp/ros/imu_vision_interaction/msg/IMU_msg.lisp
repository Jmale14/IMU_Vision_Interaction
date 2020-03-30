; Auto-generated. Do not edit!


(cl:in-package imu_vision_interaction-msg)


;//! \htmlinclude IMU_msg.msg.html

(cl:defclass <IMU_msg> (roslisp-msg-protocol:ros-message)
  ((imu_msg
    :reader imu_msg
    :initarg :imu_msg
    :type (cl:vector cl:float)
   :initform (cl:make-array 5 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass IMU_msg (<IMU_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <IMU_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'IMU_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name imu_vision_interaction-msg:<IMU_msg> is deprecated: use imu_vision_interaction-msg:IMU_msg instead.")))

(cl:ensure-generic-function 'imu_msg-val :lambda-list '(m))
(cl:defmethod imu_msg-val ((m <IMU_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imu_vision_interaction-msg:imu_msg-val is deprecated.  Use imu_vision_interaction-msg:imu_msg instead.")
  (imu_msg m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <IMU_msg>) ostream)
  "Serializes a message object of type '<IMU_msg>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'imu_msg))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <IMU_msg>) istream)
  "Deserializes a message object of type '<IMU_msg>"
  (cl:setf (cl:slot-value msg 'imu_msg) (cl:make-array 5))
  (cl:let ((vals (cl:slot-value msg 'imu_msg)))
    (cl:dotimes (i 5)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<IMU_msg>)))
  "Returns string type for a message object of type '<IMU_msg>"
  "imu_vision_interaction/IMU_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'IMU_msg)))
  "Returns string type for a message object of type 'IMU_msg"
  "imu_vision_interaction/IMU_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<IMU_msg>)))
  "Returns md5sum for a message object of type '<IMU_msg>"
  "f487f171bce2552e381aa73a58773243")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'IMU_msg)))
  "Returns md5sum for a message object of type 'IMU_msg"
  "f487f171bce2552e381aa73a58773243")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<IMU_msg>)))
  "Returns full string definition for message of type '<IMU_msg>"
  (cl:format cl:nil "float64[5] imu_msg~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'IMU_msg)))
  "Returns full string definition for message of type 'IMU_msg"
  (cl:format cl:nil "float64[5] imu_msg~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <IMU_msg>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'imu_msg) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <IMU_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'IMU_msg
    (cl:cons ':imu_msg (imu_msg msg))
))
