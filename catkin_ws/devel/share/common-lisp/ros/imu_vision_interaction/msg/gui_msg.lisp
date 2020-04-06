; Auto-generated. Do not edit!


(cl:in-package imu_vision_interaction-msg)


;//! \htmlinclude gui_msg.msg.html

(cl:defclass <gui_msg> (roslisp-msg-protocol:ros-message)
  ((imu_stat
    :reader imu_stat
    :initarg :imu_stat
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 4 :element-type 'cl:fixnum :initial-element 0))
   (kin_stat
    :reader kin_stat
    :initarg :kin_stat
    :type cl:fixnum
    :initform 0)
   (state_est_final
    :reader state_est_final
    :initarg :state_est_final
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 2 :element-type 'cl:fixnum :initial-element 0))
   (state_est_im
    :reader state_est_im
    :initarg :state_est_im
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 2 :element-type 'cl:fixnum :initial-element 0))
   (state_est_imu
    :reader state_est_imu
    :initarg :state_est_imu
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 2 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass gui_msg (<gui_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <gui_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'gui_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name imu_vision_interaction-msg:<gui_msg> is deprecated: use imu_vision_interaction-msg:gui_msg instead.")))

(cl:ensure-generic-function 'imu_stat-val :lambda-list '(m))
(cl:defmethod imu_stat-val ((m <gui_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imu_vision_interaction-msg:imu_stat-val is deprecated.  Use imu_vision_interaction-msg:imu_stat instead.")
  (imu_stat m))

(cl:ensure-generic-function 'kin_stat-val :lambda-list '(m))
(cl:defmethod kin_stat-val ((m <gui_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imu_vision_interaction-msg:kin_stat-val is deprecated.  Use imu_vision_interaction-msg:kin_stat instead.")
  (kin_stat m))

(cl:ensure-generic-function 'state_est_final-val :lambda-list '(m))
(cl:defmethod state_est_final-val ((m <gui_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imu_vision_interaction-msg:state_est_final-val is deprecated.  Use imu_vision_interaction-msg:state_est_final instead.")
  (state_est_final m))

(cl:ensure-generic-function 'state_est_im-val :lambda-list '(m))
(cl:defmethod state_est_im-val ((m <gui_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imu_vision_interaction-msg:state_est_im-val is deprecated.  Use imu_vision_interaction-msg:state_est_im instead.")
  (state_est_im m))

(cl:ensure-generic-function 'state_est_imu-val :lambda-list '(m))
(cl:defmethod state_est_imu-val ((m <gui_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imu_vision_interaction-msg:state_est_imu-val is deprecated.  Use imu_vision_interaction-msg:state_est_imu instead.")
  (state_est_imu m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <gui_msg>) ostream)
  "Serializes a message object of type '<gui_msg>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'imu_stat))
  (cl:let* ((signed (cl:slot-value msg 'kin_stat)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'state_est_final))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'state_est_im))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'state_est_imu))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <gui_msg>) istream)
  "Deserializes a message object of type '<gui_msg>"
  (cl:setf (cl:slot-value msg 'imu_stat) (cl:make-array 4))
  (cl:let ((vals (cl:slot-value msg 'imu_stat)))
    (cl:dotimes (i 4)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'kin_stat) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  (cl:setf (cl:slot-value msg 'state_est_final) (cl:make-array 2))
  (cl:let ((vals (cl:slot-value msg 'state_est_final)))
    (cl:dotimes (i 2)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))))
  (cl:setf (cl:slot-value msg 'state_est_im) (cl:make-array 2))
  (cl:let ((vals (cl:slot-value msg 'state_est_im)))
    (cl:dotimes (i 2)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))))
  (cl:setf (cl:slot-value msg 'state_est_imu) (cl:make-array 2))
  (cl:let ((vals (cl:slot-value msg 'state_est_imu)))
    (cl:dotimes (i 2)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<gui_msg>)))
  "Returns string type for a message object of type '<gui_msg>"
  "imu_vision_interaction/gui_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'gui_msg)))
  "Returns string type for a message object of type 'gui_msg"
  "imu_vision_interaction/gui_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<gui_msg>)))
  "Returns md5sum for a message object of type '<gui_msg>"
  "34f592a2b757ac695ceb8d8637e5e187")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'gui_msg)))
  "Returns md5sum for a message object of type 'gui_msg"
  "34f592a2b757ac695ceb8d8637e5e187")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<gui_msg>)))
  "Returns full string definition for message of type '<gui_msg>"
  (cl:format cl:nil "int16[4] imu_stat~%int16 kin_stat~%int16[2] state_est_final~%int16[2] state_est_im~%int16[2] state_est_imu~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'gui_msg)))
  "Returns full string definition for message of type 'gui_msg"
  (cl:format cl:nil "int16[4] imu_stat~%int16 kin_stat~%int16[2] state_est_final~%int16[2] state_est_im~%int16[2] state_est_imu~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <gui_msg>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'imu_stat) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
     2
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'state_est_final) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'state_est_im) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'state_est_imu) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <gui_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'gui_msg
    (cl:cons ':imu_stat (imu_stat msg))
    (cl:cons ':kin_stat (kin_stat msg))
    (cl:cons ':state_est_final (state_est_final msg))
    (cl:cons ':state_est_im (state_est_im msg))
    (cl:cons ':state_est_imu (state_est_imu msg))
))
