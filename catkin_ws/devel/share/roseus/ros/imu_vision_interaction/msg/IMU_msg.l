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
  :slots (_imu_msg ))

(defmethod imu_vision_interaction::IMU_msg
  (:init
   (&key
    ((:imu_msg __imu_msg) (make-array 5 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _imu_msg __imu_msg)
   self)
  (:imu_msg
   (&optional __imu_msg)
   (if __imu_msg (setq _imu_msg __imu_msg)) _imu_msg)
  (:serialization-length
   ()
   (+
    ;; float64[5] _imu_msg
    (* 8    5)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[5] _imu_msg
     (dotimes (i 5)
       (sys::poke (elt _imu_msg i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[5] _imu_msg
   (dotimes (i (length _imu_msg))
     (setf (elt _imu_msg i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;;
   self)
  )

(setf (get imu_vision_interaction::IMU_msg :md5sum-) "f487f171bce2552e381aa73a58773243")
(setf (get imu_vision_interaction::IMU_msg :datatype-) "imu_vision_interaction/IMU_msg")
(setf (get imu_vision_interaction::IMU_msg :definition-)
      "float64[5] imu_msg

")



(provide :imu_vision_interaction/IMU_msg "f487f171bce2552e381aa73a58773243")


