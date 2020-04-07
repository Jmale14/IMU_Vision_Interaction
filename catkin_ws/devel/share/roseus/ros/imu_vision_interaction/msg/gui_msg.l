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
  :slots (_imu_stat _kin_stat _state_est_final _state_est_im _state_est_imu _imu_pred _im_pred ))

(defmethod imu_vision_interaction::gui_msg
  (:init
   (&key
    ((:imu_stat __imu_stat) (make-array 4 :initial-element 0 :element-type :integer))
    ((:kin_stat __kin_stat) 0)
    ((:state_est_final __state_est_final) (make-array 2 :initial-element 0 :element-type :integer))
    ((:state_est_im __state_est_im) (make-array 2 :initial-element 0 :element-type :integer))
    ((:state_est_imu __state_est_imu) (make-array 2 :initial-element 0 :element-type :integer))
    ((:imu_pred __imu_pred) (make-array 5 :initial-element 0.0 :element-type :float))
    ((:im_pred __im_pred) (make-array 2 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _imu_stat __imu_stat)
   (setq _kin_stat (round __kin_stat))
   (setq _state_est_final __state_est_final)
   (setq _state_est_im __state_est_im)
   (setq _state_est_imu __state_est_imu)
   (setq _imu_pred __imu_pred)
   (setq _im_pred __im_pred)
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
  (:imu_pred
   (&optional __imu_pred)
   (if __imu_pred (setq _imu_pred __imu_pred)) _imu_pred)
  (:im_pred
   (&optional __im_pred)
   (if __im_pred (setq _im_pred __im_pred)) _im_pred)
  (:serialization-length
   ()
   (+
    ;; int8[4] _imu_stat
    (* 1    4)
    ;; int8 _kin_stat
    1
    ;; int8[2] _state_est_final
    (* 1    2)
    ;; int8[2] _state_est_im
    (* 1    2)
    ;; int8[2] _state_est_imu
    (* 1    2)
    ;; float64[5] _imu_pred
    (* 8    5)
    ;; float64[2] _im_pred
    (* 8    2)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8[4] _imu_stat
     (dotimes (i 4)
       (write-byte (elt _imu_stat i) s)
       )
     ;; int8 _kin_stat
       (write-byte _kin_stat s)
     ;; int8[2] _state_est_final
     (dotimes (i 2)
       (write-byte (elt _state_est_final i) s)
       )
     ;; int8[2] _state_est_im
     (dotimes (i 2)
       (write-byte (elt _state_est_im i) s)
       )
     ;; int8[2] _state_est_imu
     (dotimes (i 2)
       (write-byte (elt _state_est_imu i) s)
       )
     ;; float64[5] _imu_pred
     (dotimes (i 5)
       (sys::poke (elt _imu_pred i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[2] _im_pred
     (dotimes (i 2)
       (sys::poke (elt _im_pred i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8[4] _imu_stat
   (dotimes (i (length _imu_stat))
     (setf (elt _imu_stat i) (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> (elt _imu_stat i) 127) (setf (elt _imu_stat i) (- (elt _imu_stat i) 256)))
     )
   ;; int8 _kin_stat
     (setq _kin_stat (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _kin_stat 127) (setq _kin_stat (- _kin_stat 256)))
   ;; int8[2] _state_est_final
   (dotimes (i (length _state_est_final))
     (setf (elt _state_est_final i) (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> (elt _state_est_final i) 127) (setf (elt _state_est_final i) (- (elt _state_est_final i) 256)))
     )
   ;; int8[2] _state_est_im
   (dotimes (i (length _state_est_im))
     (setf (elt _state_est_im i) (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> (elt _state_est_im i) 127) (setf (elt _state_est_im i) (- (elt _state_est_im i) 256)))
     )
   ;; int8[2] _state_est_imu
   (dotimes (i (length _state_est_imu))
     (setf (elt _state_est_imu i) (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> (elt _state_est_imu i) 127) (setf (elt _state_est_imu i) (- (elt _state_est_imu i) 256)))
     )
   ;; float64[5] _imu_pred
   (dotimes (i (length _imu_pred))
     (setf (elt _imu_pred i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;; float64[2] _im_pred
   (dotimes (i (length _im_pred))
     (setf (elt _im_pred i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;;
   self)
  )

(setf (get imu_vision_interaction::gui_msg :md5sum-) "bf8981175370443a047e2d3397a3cff7")
(setf (get imu_vision_interaction::gui_msg :datatype-) "imu_vision_interaction/gui_msg")
(setf (get imu_vision_interaction::gui_msg :definition-)
      "int8[4] imu_stat
int8 kin_stat
int8[2] state_est_final
int8[2] state_est_im
int8[2] state_est_imu
float64[5] imu_pred
float64[2] im_pred
")



(provide :imu_vision_interaction/gui_msg "bf8981175370443a047e2d3397a3cff7")


