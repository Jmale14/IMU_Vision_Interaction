; Auto-generated. Do not edit!


(cl:in-package imu_vision_interaction-msg)


;//! \htmlinclude kinect_msg.msg.html

(cl:defclass <kinect_msg> (roslisp-msg-protocol:ros-message)
  ((im_screw_probs_1
    :reader im_screw_probs_1
    :initarg :im_screw_probs_1
    :type (cl:vector cl:float)
   :initform (cl:make-array 5 :element-type 'cl:float :initial-element 0.0))
   (im_screw_probs_2
    :reader im_screw_probs_2
    :initarg :im_screw_probs_2
    :type (cl:vector cl:float)
   :initform (cl:make-array 5 :element-type 'cl:float :initial-element 0.0))
   (im_screw_probs_3
    :reader im_screw_probs_3
    :initarg :im_screw_probs_3
    :type (cl:vector cl:float)
   :initform (cl:make-array 5 :element-type 'cl:float :initial-element 0.0))
   (im_screw_probs_4
    :reader im_screw_probs_4
    :initarg :im_screw_probs_4
    :type (cl:vector cl:float)
   :initform (cl:make-array 5 :element-type 'cl:float :initial-element 0.0))
   (safe_move
    :reader safe_move
    :initarg :safe_move
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass kinect_msg (<kinect_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <kinect_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'kinect_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name imu_vision_interaction-msg:<kinect_msg> is deprecated: use imu_vision_interaction-msg:kinect_msg instead.")))

(cl:ensure-generic-function 'im_screw_probs_1-val :lambda-list '(m))
(cl:defmethod im_screw_probs_1-val ((m <kinect_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imu_vision_interaction-msg:im_screw_probs_1-val is deprecated.  Use imu_vision_interaction-msg:im_screw_probs_1 instead.")
  (im_screw_probs_1 m))

(cl:ensure-generic-function 'im_screw_probs_2-val :lambda-list '(m))
(cl:defmethod im_screw_probs_2-val ((m <kinect_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imu_vision_interaction-msg:im_screw_probs_2-val is deprecated.  Use imu_vision_interaction-msg:im_screw_probs_2 instead.")
  (im_screw_probs_2 m))

(cl:ensure-generic-function 'im_screw_probs_3-val :lambda-list '(m))
(cl:defmethod im_screw_probs_3-val ((m <kinect_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imu_vision_interaction-msg:im_screw_probs_3-val is deprecated.  Use imu_vision_interaction-msg:im_screw_probs_3 instead.")
  (im_screw_probs_3 m))

(cl:ensure-generic-function 'im_screw_probs_4-val :lambda-list '(m))
(cl:defmethod im_screw_probs_4-val ((m <kinect_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imu_vision_interaction-msg:im_screw_probs_4-val is deprecated.  Use imu_vision_interaction-msg:im_screw_probs_4 instead.")
  (im_screw_probs_4 m))

(cl:ensure-generic-function 'safe_move-val :lambda-list '(m))
(cl:defmethod safe_move-val ((m <kinect_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imu_vision_interaction-msg:safe_move-val is deprecated.  Use imu_vision_interaction-msg:safe_move instead.")
  (safe_move m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <kinect_msg>) ostream)
  "Serializes a message object of type '<kinect_msg>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'im_screw_probs_1))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'im_screw_probs_2))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'im_screw_probs_3))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'im_screw_probs_4))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'safe_move) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <kinect_msg>) istream)
  "Deserializes a message object of type '<kinect_msg>"
  (cl:setf (cl:slot-value msg 'im_screw_probs_1) (cl:make-array 5))
  (cl:let ((vals (cl:slot-value msg 'im_screw_probs_1)))
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
  (cl:setf (cl:slot-value msg 'im_screw_probs_2) (cl:make-array 5))
  (cl:let ((vals (cl:slot-value msg 'im_screw_probs_2)))
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
  (cl:setf (cl:slot-value msg 'im_screw_probs_3) (cl:make-array 5))
  (cl:let ((vals (cl:slot-value msg 'im_screw_probs_3)))
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
  (cl:setf (cl:slot-value msg 'im_screw_probs_4) (cl:make-array 5))
  (cl:let ((vals (cl:slot-value msg 'im_screw_probs_4)))
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
    (cl:setf (cl:slot-value msg 'safe_move) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<kinect_msg>)))
  "Returns string type for a message object of type '<kinect_msg>"
  "imu_vision_interaction/kinect_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'kinect_msg)))
  "Returns string type for a message object of type 'kinect_msg"
  "imu_vision_interaction/kinect_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<kinect_msg>)))
  "Returns md5sum for a message object of type '<kinect_msg>"
  "a2edb252d0d37f6b395cd5f25d43ffd5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'kinect_msg)))
  "Returns md5sum for a message object of type 'kinect_msg"
  "a2edb252d0d37f6b395cd5f25d43ffd5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<kinect_msg>)))
  "Returns full string definition for message of type '<kinect_msg>"
  (cl:format cl:nil "float64[5] im_screw_probs_1~%float64[5] im_screw_probs_2~%float64[5] im_screw_probs_3~%float64[5] im_screw_probs_4~%bool safe_move~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'kinect_msg)))
  "Returns full string definition for message of type 'kinect_msg"
  (cl:format cl:nil "float64[5] im_screw_probs_1~%float64[5] im_screw_probs_2~%float64[5] im_screw_probs_3~%float64[5] im_screw_probs_4~%bool safe_move~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <kinect_msg>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'im_screw_probs_1) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'im_screw_probs_2) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'im_screw_probs_3) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'im_screw_probs_4) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <kinect_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'kinect_msg
    (cl:cons ':im_screw_probs_1 (im_screw_probs_1 msg))
    (cl:cons ':im_screw_probs_2 (im_screw_probs_2 msg))
    (cl:cons ':im_screw_probs_3 (im_screw_probs_3 msg))
    (cl:cons ':im_screw_probs_4 (im_screw_probs_4 msg))
    (cl:cons ':safe_move (safe_move msg))
))
