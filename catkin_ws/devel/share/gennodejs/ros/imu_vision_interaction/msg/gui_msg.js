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

class gui_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.imu_stat = null;
      this.kin_stat = null;
      this.state_est_final = null;
      this.state_est_im = null;
      this.state_est_imu = null;
    }
    else {
      if (initObj.hasOwnProperty('imu_stat')) {
        this.imu_stat = initObj.imu_stat
      }
      else {
        this.imu_stat = new Array(4).fill(0);
      }
      if (initObj.hasOwnProperty('kin_stat')) {
        this.kin_stat = initObj.kin_stat
      }
      else {
        this.kin_stat = 0;
      }
      if (initObj.hasOwnProperty('state_est_final')) {
        this.state_est_final = initObj.state_est_final
      }
      else {
        this.state_est_final = new Array(2).fill(0);
      }
      if (initObj.hasOwnProperty('state_est_im')) {
        this.state_est_im = initObj.state_est_im
      }
      else {
        this.state_est_im = new Array(2).fill(0);
      }
      if (initObj.hasOwnProperty('state_est_imu')) {
        this.state_est_imu = initObj.state_est_imu
      }
      else {
        this.state_est_imu = new Array(2).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type gui_msg
    // Check that the constant length array field [imu_stat] has the right length
    if (obj.imu_stat.length !== 4) {
      throw new Error('Unable to serialize array field imu_stat - length must be 4')
    }
    // Serialize message field [imu_stat]
    bufferOffset = _arraySerializer.int16(obj.imu_stat, buffer, bufferOffset, 4);
    // Serialize message field [kin_stat]
    bufferOffset = _serializer.int16(obj.kin_stat, buffer, bufferOffset);
    // Check that the constant length array field [state_est_final] has the right length
    if (obj.state_est_final.length !== 2) {
      throw new Error('Unable to serialize array field state_est_final - length must be 2')
    }
    // Serialize message field [state_est_final]
    bufferOffset = _arraySerializer.int16(obj.state_est_final, buffer, bufferOffset, 2);
    // Check that the constant length array field [state_est_im] has the right length
    if (obj.state_est_im.length !== 2) {
      throw new Error('Unable to serialize array field state_est_im - length must be 2')
    }
    // Serialize message field [state_est_im]
    bufferOffset = _arraySerializer.int16(obj.state_est_im, buffer, bufferOffset, 2);
    // Check that the constant length array field [state_est_imu] has the right length
    if (obj.state_est_imu.length !== 2) {
      throw new Error('Unable to serialize array field state_est_imu - length must be 2')
    }
    // Serialize message field [state_est_imu]
    bufferOffset = _arraySerializer.int16(obj.state_est_imu, buffer, bufferOffset, 2);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type gui_msg
    let len;
    let data = new gui_msg(null);
    // Deserialize message field [imu_stat]
    data.imu_stat = _arrayDeserializer.int16(buffer, bufferOffset, 4)
    // Deserialize message field [kin_stat]
    data.kin_stat = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [state_est_final]
    data.state_est_final = _arrayDeserializer.int16(buffer, bufferOffset, 2)
    // Deserialize message field [state_est_im]
    data.state_est_im = _arrayDeserializer.int16(buffer, bufferOffset, 2)
    // Deserialize message field [state_est_imu]
    data.state_est_imu = _arrayDeserializer.int16(buffer, bufferOffset, 2)
    return data;
  }

  static getMessageSize(object) {
    return 22;
  }

  static datatype() {
    // Returns string type for a message object
    return 'imu_vision_interaction/gui_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '34f592a2b757ac695ceb8d8637e5e187';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16[4] imu_stat
    int16 kin_stat
    int16[2] state_est_final
    int16[2] state_est_im
    int16[2] state_est_imu
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new gui_msg(null);
    if (msg.imu_stat !== undefined) {
      resolved.imu_stat = msg.imu_stat;
    }
    else {
      resolved.imu_stat = new Array(4).fill(0)
    }

    if (msg.kin_stat !== undefined) {
      resolved.kin_stat = msg.kin_stat;
    }
    else {
      resolved.kin_stat = 0
    }

    if (msg.state_est_final !== undefined) {
      resolved.state_est_final = msg.state_est_final;
    }
    else {
      resolved.state_est_final = new Array(2).fill(0)
    }

    if (msg.state_est_im !== undefined) {
      resolved.state_est_im = msg.state_est_im;
    }
    else {
      resolved.state_est_im = new Array(2).fill(0)
    }

    if (msg.state_est_imu !== undefined) {
      resolved.state_est_imu = msg.state_est_imu;
    }
    else {
      resolved.state_est_imu = new Array(2).fill(0)
    }

    return resolved;
    }
};

module.exports = gui_msg;
