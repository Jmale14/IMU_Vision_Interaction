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
   :initform (cl:make-array 2 :element-type 'cl:fixnum :initial-element 0))
   (imu_pred
    :reader imu_pred
    :initarg :imu_pred
    :type (cl:vector cl:float)
   :initform (cl:make-array 5 :element-type 'cl:float :initial-element 0.0))
   (im_pred
    :reader im_pred
    :initarg :im_pred
    :type (cl:vector cl:float)
   :initform (cl:make-array 2 :element-type 'cl:float :initial-element 0.0)))
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

(cl:ensure-generic-function 'imu_pred-val :lambda-list '(m))
(cl:defmethod imu_pred-val ((m <gui_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imu_vision_interaction-msg:imu_pred-val is deprecated.  Use imu_vision_interaction-msg:imu_pred instead.")
  (imu_pred m))

(cl:ensure-generic-function 'im_pred-val :lambda-list '(m))
(cl:defmethod im_pred-val ((m <gui_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imu_vision_interaction-msg:im_pred-val is deprecated.  Use imu_vision_interaction-msg:im_pred instead.")
  (im_pred m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <gui_msg>) ostream)
  "Serializes a message object of type '<gui_msg>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    ))
   (cl:slot-value msg 'imu_stat))
  (cl:let* ((signed (cl:slot-value msg 'kin_stat)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    ))
   (cl:slot-value msg 'state_est_final))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    ))
   (cl:slot-value msg 'state_est_im))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    ))
   (cl:slot-value msg 'state_est_imu))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'imu_pred))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'im_pred))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <gui_msg>) istream)
  "Deserializes a message object of type '<gui_msg>"
  (cl:setf (cl:slot-value msg 'imu_stat) (cl:make-array 4))
  (cl:let ((vals (cl:slot-value msg 'imu_stat)))
    (cl:dotimes (i 4)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'kin_stat) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  (cl:setf (cl:slot-value msg 'state_est_final) (cl:make-array 2))
  (cl:let ((vals (cl:slot-value msg 'state_est_final)))
    (cl:dotimes (i 2)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))))
  (cl:setf (cl:slot-value msg 'state_est_im) (cl:make-array 2))
  (cl:let ((vals (cl:slot-value msg 'state_est_im)))
    (cl:dotimes (i 2)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))))
  (cl:setf (cl:slot-value msg 'state_est_imu) (cl:make-array 2))
  (cl:let ((vals (cl:slot-value msg 'state_est_imu)))
    (cl:dotimes (i 2)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))))
  (cl:setf (cl:slot-value msg 'imu_pred) (cl:make-array 5))
  (cl:let ((vals (cl:slot-value msg 'imu_pred)))
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
  (cl:setf (cl:slot-value msg 'im_pred) (cl:make-array 2))
  (cl:let ((vals (cl:slot-value msg 'im_pred)))
    (cl:dotimes (i 2)
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<gui_msg>)))
  "Returns string type for a message object of type '<gui_msg>"
  "imu_vision_interaction/gui_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'gui_msg)))
  "Returns string type for a message object of type 'gui_msg"
  "imu_vision_interaction/gui_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<gui_msg>)))
  "Returns md5sum for a message object of type '<gui_msg>"
  "bf8981175370443a047e2d3397a3cff7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'gui_msg)))
  "Returns md5sum for a message object of type 'gui_msg"
  "bf8981175370443a047e2d3397a3cff7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<gui_msg>)))
  "Returns full string definition for message of type '<gui_msg>"
  (cl:format cl:nil "int8[4] imu_stat~%int8 kin_stat~%int8[2] state_est_final~%int8[2] state_est_im~%int8[2] state_est_imu~%float64[5] imu_pred~%float64[2] im_pred~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'gui_msg)))
  "Returns full string definition for message of type 'gui_msg"
  (cl:format cl:nil "int8[4] imu_stat~%int8 kin_stat~%int8[2] state_est_final~%int8[2] state_est_im~%int8[2] state_est_imu~%float64[5] imu_pred~%float64[2] im_pred~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <gui_msg>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'imu_stat) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
     1
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'state_est_final) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'state_est_im) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'state_est_imu) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'imu_pred) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'im_pred) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <gui_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'gui_msg
    (cl:cons ':imu_stat (imu_stat msg))
    (cl:cons ':kin_stat (kin_stat msg))
    (cl:cons ':state_est_final (state_est_final msg))
    (cl:cons ':state_est_im (state_est_im msg))
    (cl:cons ':state_est_imu (state_est_imu msg))
    (cl:cons ':imu_pred (imu_pred msg))
    (cl:cons ':im_pred (im_pred msg))
))
