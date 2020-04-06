;; Auto-generated. Do not edit!


(when (boundp 'imu_vision_interaction::gui_msg)
  (if (not (find-package "IMU_VISION_INTERACTION"))
    (make-package "IMU_VISION_INTERACTION"))
  (shadow 'gui_msg (find-package "IMU_VISION_INTERACTION")))
(unless (find-package "IMU_VISION_INTERACTION::GUI_MSG")
  (make-package "IMU_VISION_INTERACTION::GUI_MSG"))

(in-package "ROS")
;;//! \htmlinclude gui_msg.msg.html


(defclass imu_vision_interaction::gui_msg
  :super ros::object
  :slots (_imu_stat _kin_stat _state_est_final _state_est_im _state_est_imu ))

(defmethod imu_vision_interaction::gui_msg
  (:init
   (&key
    ((:imu_stat __imu_stat) (make-array 4 :initial-element 0 :element-type :integer))
    ((:kin_stat __kin_stat) 0)
    ((:state_est_final __state_est_final) (make-array 2 :initial-element 0 :element-type :integer))
    ((:state_est_im __state_est_im) (make-array 2 :initial-element 0 :element-type :integer))
    ((:state_est_imu __state_est_imu) (make-array 2 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _imu_stat __imu_stat)
   (setq _kin_stat (round __kin_stat))
   (setq _state_est_final __state_est_final)
   (setq _state_est_im __state_est_im)
   (setq _state_est_imu __state_est_imu)
   self)
  (:imu_stat
   (&optional __imu_stat)
   (if __imu_stat (setq _imu_stat __imu_stat)) _imu_stat)
  (:kin_stat
   (&optional __kin_stat)
   (if __kin_stat (setq _kin_stat __kin_stat)) _kin_stat)
  (:state_est_final
   (&optional __state_est_final)
   (if __state_est_final (setq _state_est_final __state_est_final)) _state_est_final)
  (:state_est_im
   (&optional __state_est_im)
   (if __state_est_im (setq _state_est_im __state_est_im)) _state_est_im)
  (:state_est_imu
   (&optional __state_est_imu)
   (if __state_est_imu (setq _state_est_imu __state_est_imu)) _state_est_imu)
  (:serialization-length
   ()
   (+
    ;; int16[4] _imu_stat
    (* 2    4)
    ;; int16 _kin_stat
    2
    ;; int16[2] _state_est_final
    (* 2    2)
    ;; int16[2] _state_est_im
    (* 2    2)
    ;; int16[2] _state_est_imu
    (* 2    2)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16[4] _imu_stat
     (dotimes (i 4)
       (write-word (elt _imu_stat i) s)
       )
     ;; int16 _kin_stat
       (write-word _kin_stat s)
     ;; int16[2] _state_est_final
     (dotimes (i 2)
       (write-word (elt _state_est_final i) s)
       )
     ;; int16[2] _state_est_im
     (dotimes (i 2)
       (write-word (elt _state_est_im i) s)
       )
     ;; int16[2] _state_est_imu
     (dotimes (i 2)
       (write-word (elt _state_est_imu i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16[4] _imu_stat
   (dotimes (i (length _imu_stat))
     (setf (elt _imu_stat i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     )
   ;; int16 _kin_stat
     (setq _kin_stat (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16[2] _state_est_final
   (dotimes (i (length _state_est_final))
     (setf (elt _state_est_final i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     )
   ;; int16[2] _state_est_im
   (dotimes (i (length _state_est_im))
     (setf (elt _state_est_im i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     )
   ;; int16[2] _state_est_imu
   (dotimes (i (length _state_est_imu))
     (setf (elt _state_est_imu i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     )
   ;;
   self)
  )

(setf (get imu_vision_interaction::gui_msg :md5sum-) "34f592a2b757ac695ceb8d8637e5e187")
(setf (get imu_vision_interaction::gui_msg :datatype-) "imu_vision_interaction/gui_msg")
(setf (get imu_vision_interaction::gui_msg :definition-)
      "int16[4] imu_stat
int16 kin_stat
int16[2] state_est_final
int16[2] state_est_im
int16[2] state_est_imu
")



(provide :imu_vision_interaction/gui_msg "34f592a2b757ac695ceb8d8637e5e187")


