;; Auto-generated. Do not edit!


(when (boundp 'imu_vision_interaction::IMU_msg)
  (if (not (find-package "IMU_VISION_INTERACTION"))
    (make-package "IMU_VISION_INTERACTION"))
  (shadow 'IMU_msg (find-package "IMU_VISION_INTERACTION")))
(unless (find-package "IMU_VISION_INTERACTION::IMU_MSG")
  (make-package "IMU_VISION_INTERACTION::IMU_MSG"))

(in-package "ROS")
;;//! \htmlinclude IMU_msg.msg.html


(defclass imu_vision_interaction::IMU_msg
  :super ros::object
  :slots (_imu_msg _imu_stat ))

(defmethod imu_vision_interaction::IMU_msg
  (:init
   (&key
    ((:imu_msg __imu_msg) (make-array 5 :initial-element 0.0 :element-type :float))
    ((:imu_stat __imu_stat) (make-array 4 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _imu_msg __imu_msg)
   (setq _imu_stat __imu_stat)
   self)
  (:imu_msg
   (&optional __imu_msg)
   (if __imu_msg (setq _imu_msg __imu_msg)) _imu_msg)
  (:imu_stat
   (&optional __imu_stat)
   (if __imu_stat (setq _imu_stat __imu_stat)) _imu_stat)
  (:serialization-length
   ()
   (+
    ;; float64[5] _imu_msg
    (* 8    5)
    ;; int8[4] _imu_stat
    (* 1    4)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[5] _imu_msg
     (dotimes (i 5)
       (sys::poke (elt _imu_msg i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; int8[4] _imu_stat
     (dotimes (i 4)
       (write-byte (elt _imu_stat i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[5] _imu_msg
   (dotimes (i (length _imu_msg))
     (setf (elt _imu_msg i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;; int8[4] _imu_stat
   (dotimes (i (length _imu_stat))
     (setf (elt _imu_stat i) (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> (elt _imu_stat i) 127) (setf (elt _imu_stat i) (- (elt _imu_stat i) 256)))
     )
   ;;
   self)
  )

(setf (get imu_vision_interaction::IMU_msg :md5sum-) "affaccaeab02b87844ca1675a87c3358")
(setf (get imu_vision_interaction::IMU_msg :datatype-) "imu_vision_interaction/IMU_msg")
(setf (get imu_vision_interaction::IMU_msg :definition-)
      "float64[5] imu_msg
int8[4] imu_stat
")



(provide :imu_vision_interaction/IMU_msg "affaccaeab02b87844ca1675a87c3358")


