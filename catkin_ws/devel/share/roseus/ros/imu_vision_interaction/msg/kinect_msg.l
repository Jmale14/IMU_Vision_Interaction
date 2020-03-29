;; Auto-generated. Do not edit!


(when (boundp 'imu_vision_interaction::kinect_msg)
  (if (not (find-package "IMU_VISION_INTERACTION"))
    (make-package "IMU_VISION_INTERACTION"))
  (shadow 'kinect_msg (find-package "IMU_VISION_INTERACTION")))
(unless (find-package "IMU_VISION_INTERACTION::KINECT_MSG")
  (make-package "IMU_VISION_INTERACTION::KINECT_MSG"))

(in-package "ROS")
;;//! \htmlinclude kinect_msg.msg.html


(defclass imu_vision_interaction::kinect_msg
  :super ros::object
  :slots (_im_screw_probs_1 _im_screw_probs_2 _im_screw_probs_3 _im_screw_probs_4 _tally _safe_move ))

(defmethod imu_vision_interaction::kinect_msg
  (:init
   (&key
    ((:im_screw_probs_1 __im_screw_probs_1) (make-array 5 :initial-element 0.0 :element-type :float))
    ((:im_screw_probs_2 __im_screw_probs_2) (make-array 5 :initial-element 0.0 :element-type :float))
    ((:im_screw_probs_3 __im_screw_probs_3) (make-array 5 :initial-element 0.0 :element-type :float))
    ((:im_screw_probs_4 __im_screw_probs_4) (make-array 5 :initial-element 0.0 :element-type :float))
    ((:tally __tally) (make-array 5 :initial-element 0.0 :element-type :float))
    ((:safe_move __safe_move) nil)
    )
   (send-super :init)
   (setq _im_screw_probs_1 __im_screw_probs_1)
   (setq _im_screw_probs_2 __im_screw_probs_2)
   (setq _im_screw_probs_3 __im_screw_probs_3)
   (setq _im_screw_probs_4 __im_screw_probs_4)
   (setq _tally __tally)
   (setq _safe_move __safe_move)
   self)
  (:im_screw_probs_1
   (&optional __im_screw_probs_1)
   (if __im_screw_probs_1 (setq _im_screw_probs_1 __im_screw_probs_1)) _im_screw_probs_1)
  (:im_screw_probs_2
   (&optional __im_screw_probs_2)
   (if __im_screw_probs_2 (setq _im_screw_probs_2 __im_screw_probs_2)) _im_screw_probs_2)
  (:im_screw_probs_3
   (&optional __im_screw_probs_3)
   (if __im_screw_probs_3 (setq _im_screw_probs_3 __im_screw_probs_3)) _im_screw_probs_3)
  (:im_screw_probs_4
   (&optional __im_screw_probs_4)
   (if __im_screw_probs_4 (setq _im_screw_probs_4 __im_screw_probs_4)) _im_screw_probs_4)
  (:tally
   (&optional __tally)
   (if __tally (setq _tally __tally)) _tally)
  (:safe_move
   (&optional __safe_move)
   (if __safe_move (setq _safe_move __safe_move)) _safe_move)
  (:serialization-length
   ()
   (+
    ;; float64[5] _im_screw_probs_1
    (* 8    5)
    ;; float64[5] _im_screw_probs_2
    (* 8    5)
    ;; float64[5] _im_screw_probs_3
    (* 8    5)
    ;; float64[5] _im_screw_probs_4
    (* 8    5)
    ;; float64[5] _tally
    (* 8    5)
    ;; bool _safe_move
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[5] _im_screw_probs_1
     (dotimes (i 5)
       (sys::poke (elt _im_screw_probs_1 i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[5] _im_screw_probs_2
     (dotimes (i 5)
       (sys::poke (elt _im_screw_probs_2 i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[5] _im_screw_probs_3
     (dotimes (i 5)
       (sys::poke (elt _im_screw_probs_3 i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[5] _im_screw_probs_4
     (dotimes (i 5)
       (sys::poke (elt _im_screw_probs_4 i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[5] _tally
     (dotimes (i 5)
       (sys::poke (elt _tally i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; bool _safe_move
       (if _safe_move (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[5] _im_screw_probs_1
   (dotimes (i (length _im_screw_probs_1))
     (setf (elt _im_screw_probs_1 i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;; float64[5] _im_screw_probs_2
   (dotimes (i (length _im_screw_probs_2))
     (setf (elt _im_screw_probs_2 i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;; float64[5] _im_screw_probs_3
   (dotimes (i (length _im_screw_probs_3))
     (setf (elt _im_screw_probs_3 i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;; float64[5] _im_screw_probs_4
   (dotimes (i (length _im_screw_probs_4))
     (setf (elt _im_screw_probs_4 i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;; float64[5] _tally
   (dotimes (i (length _tally))
     (setf (elt _tally i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;; bool _safe_move
     (setq _safe_move (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get imu_vision_interaction::kinect_msg :md5sum-) "7d063af4b46c588d600951ce9d186617")
(setf (get imu_vision_interaction::kinect_msg :datatype-) "imu_vision_interaction/kinect_msg")
(setf (get imu_vision_interaction::kinect_msg :definition-)
      "float64[5] im_screw_probs_1
float64[5] im_screw_probs_2
float64[5] im_screw_probs_3
float64[5] im_screw_probs_4
float64[5] tally
bool safe_move
")



(provide :imu_vision_interaction/kinect_msg "7d063af4b46c588d600951ce9d186617")


