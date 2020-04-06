// Auto-generated. Do not edit!

// (in-package imu_vision_interaction.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class IMU_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.imu_msg = null;
      this.imu_stat = null;
    }
    else {
      if (initObj.hasOwnProperty('imu_msg')) {
        this.imu_msg = initObj.imu_msg
      }
      else {
        this.imu_msg = new Array(5).fill(0);
      }
      if (initObj.hasOwnProperty('imu_stat')) {
        this.imu_stat = initObj.imu_stat
      }
      else {
        this.imu_stat = new Array(4).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type IMU_msg
    // Check that the constant length array field [imu_msg] has the right length
    if (obj.imu_msg.length !== 5) {
      throw new Error('Unable to serialize array field imu_msg - length must be 5')
    }
    // Serialize message field [imu_msg]
    bufferOffset = _arraySerializer.float64(obj.imu_msg, buffer, bufferOffset, 5);
    // Check that the constant length array field [imu_stat] has the right length
    if (obj.imu_stat.length !== 4) {
      throw new Error('Unable to serialize array field imu_stat - length must be 4')
    }
    // Serialize message field [imu_stat]
    bufferOffset = _arraySerializer.int8(obj.imu_stat, buffer, bufferOffset, 4);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type IMU_msg
    let len;
    let data = new IMU_msg(null);
    // Deserialize message field [imu_msg]
    data.imu_msg = _arrayDeserializer.float64(buffer, bufferOffset, 5)
    // Deserialize message field [imu_stat]
    data.imu_stat = _arrayDeserializer.int8(buffer, bufferOffset, 4)
    return data;
  }

  static getMessageSize(object) {
    return 44;
  }

  static datatype() {
    // Returns string type for a message object
    return 'imu_vision_interaction/IMU_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'affaccaeab02b87844ca1675a87c3358';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[5] imu_msg
    int8[4] imu_stat
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new IMU_msg(null);
    if (msg.imu_msg !== undefined) {
      resolved.imu_msg = msg.imu_msg;
    }
    else {
      resolved.imu_msg = new Array(5).fill(0)
    }

    if (msg.imu_stat !== undefined) {
      resolved.imu_stat = msg.imu_stat;
    }
    else {
      resolved.imu_stat = new Array(4).fill(0)
    }

    return resolved;
    }
};

module.exports = IMU_msg;
