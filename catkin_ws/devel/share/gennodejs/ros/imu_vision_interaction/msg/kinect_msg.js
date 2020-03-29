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

class kinect_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.im_screw_probs_1 = null;
      this.im_screw_probs_2 = null;
      this.im_screw_probs_3 = null;
      this.im_screw_probs_4 = null;
      this.tally = null;
      this.safe_move = null;
    }
    else {
      if (initObj.hasOwnProperty('im_screw_probs_1')) {
        this.im_screw_probs_1 = initObj.im_screw_probs_1
      }
      else {
        this.im_screw_probs_1 = new Array(5).fill(0);
      }
      if (initObj.hasOwnProperty('im_screw_probs_2')) {
        this.im_screw_probs_2 = initObj.im_screw_probs_2
      }
      else {
        this.im_screw_probs_2 = new Array(5).fill(0);
      }
      if (initObj.hasOwnProperty('im_screw_probs_3')) {
        this.im_screw_probs_3 = initObj.im_screw_probs_3
      }
      else {
        this.im_screw_probs_3 = new Array(5).fill(0);
      }
      if (initObj.hasOwnProperty('im_screw_probs_4')) {
        this.im_screw_probs_4 = initObj.im_screw_probs_4
      }
      else {
        this.im_screw_probs_4 = new Array(5).fill(0);
      }
      if (initObj.hasOwnProperty('tally')) {
        this.tally = initObj.tally
      }
      else {
        this.tally = new Array(5).fill(0);
      }
      if (initObj.hasOwnProperty('safe_move')) {
        this.safe_move = initObj.safe_move
      }
      else {
        this.safe_move = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type kinect_msg
    // Check that the constant length array field [im_screw_probs_1] has the right length
    if (obj.im_screw_probs_1.length !== 5) {
      throw new Error('Unable to serialize array field im_screw_probs_1 - length must be 5')
    }
    // Serialize message field [im_screw_probs_1]
    bufferOffset = _arraySerializer.float64(obj.im_screw_probs_1, buffer, bufferOffset, 5);
    // Check that the constant length array field [im_screw_probs_2] has the right length
    if (obj.im_screw_probs_2.length !== 5) {
      throw new Error('Unable to serialize array field im_screw_probs_2 - length must be 5')
    }
    // Serialize message field [im_screw_probs_2]
    bufferOffset = _arraySerializer.float64(obj.im_screw_probs_2, buffer, bufferOffset, 5);
    // Check that the constant length array field [im_screw_probs_3] has the right length
    if (obj.im_screw_probs_3.length !== 5) {
      throw new Error('Unable to serialize array field im_screw_probs_3 - length must be 5')
    }
    // Serialize message field [im_screw_probs_3]
    bufferOffset = _arraySerializer.float64(obj.im_screw_probs_3, buffer, bufferOffset, 5);
    // Check that the constant length array field [im_screw_probs_4] has the right length
    if (obj.im_screw_probs_4.length !== 5) {
      throw new Error('Unable to serialize array field im_screw_probs_4 - length must be 5')
    }
    // Serialize message field [im_screw_probs_4]
    bufferOffset = _arraySerializer.float64(obj.im_screw_probs_4, buffer, bufferOffset, 5);
    // Check that the constant length array field [tally] has the right length
    if (obj.tally.length !== 5) {
      throw new Error('Unable to serialize array field tally - length must be 5')
    }
    // Serialize message field [tally]
    bufferOffset = _arraySerializer.float64(obj.tally, buffer, bufferOffset, 5);
    // Serialize message field [safe_move]
    bufferOffset = _serializer.bool(obj.safe_move, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type kinect_msg
    let len;
    let data = new kinect_msg(null);
    // Deserialize message field [im_screw_probs_1]
    data.im_screw_probs_1 = _arrayDeserializer.float64(buffer, bufferOffset, 5)
    // Deserialize message field [im_screw_probs_2]
    data.im_screw_probs_2 = _arrayDeserializer.float64(buffer, bufferOffset, 5)
    // Deserialize message field [im_screw_probs_3]
    data.im_screw_probs_3 = _arrayDeserializer.float64(buffer, bufferOffset, 5)
    // Deserialize message field [im_screw_probs_4]
    data.im_screw_probs_4 = _arrayDeserializer.float64(buffer, bufferOffset, 5)
    // Deserialize message field [tally]
    data.tally = _arrayDeserializer.float64(buffer, bufferOffset, 5)
    // Deserialize message field [safe_move]
    data.safe_move = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 201;
  }

  static datatype() {
    // Returns string type for a message object
    return 'imu_vision_interaction/kinect_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7d063af4b46c588d600951ce9d186617';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[5] im_screw_probs_1
    float64[5] im_screw_probs_2
    float64[5] im_screw_probs_3
    float64[5] im_screw_probs_4
    float64[5] tally
    bool safe_move
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new kinect_msg(null);
    if (msg.im_screw_probs_1 !== undefined) {
      resolved.im_screw_probs_1 = msg.im_screw_probs_1;
    }
    else {
      resolved.im_screw_probs_1 = new Array(5).fill(0)
    }

    if (msg.im_screw_probs_2 !== undefined) {
      resolved.im_screw_probs_2 = msg.im_screw_probs_2;
    }
    else {
      resolved.im_screw_probs_2 = new Array(5).fill(0)
    }

    if (msg.im_screw_probs_3 !== undefined) {
      resolved.im_screw_probs_3 = msg.im_screw_probs_3;
    }
    else {
      resolved.im_screw_probs_3 = new Array(5).fill(0)
    }

    if (msg.im_screw_probs_4 !== undefined) {
      resolved.im_screw_probs_4 = msg.im_screw_probs_4;
    }
    else {
      resolved.im_screw_probs_4 = new Array(5).fill(0)
    }

    if (msg.tally !== undefined) {
      resolved.tally = msg.tally;
    }
    else {
      resolved.tally = new Array(5).fill(0)
    }

    if (msg.safe_move !== undefined) {
      resolved.safe_move = msg.safe_move;
    }
    else {
      resolved.safe_move = false
    }

    return resolved;
    }
};

module.exports = kinect_msg;
