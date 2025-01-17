// Generated by gencpp from file imu_vision_interaction/IMU_msg.msg
// DO NOT EDIT!


#ifndef IMU_VISION_INTERACTION_MESSAGE_IMU_MSG_H
#define IMU_VISION_INTERACTION_MESSAGE_IMU_MSG_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace imu_vision_interaction
{
template <class ContainerAllocator>
struct IMU_msg_
{
  typedef IMU_msg_<ContainerAllocator> Type;

  IMU_msg_()
    : imu_msg()
    , imu_stat()  {
      imu_msg.assign(0.0);

      imu_stat.assign(0);
  }
  IMU_msg_(const ContainerAllocator& _alloc)
    : imu_msg()
    , imu_stat()  {
  (void)_alloc;
      imu_msg.assign(0.0);

      imu_stat.assign(0);
  }



   typedef boost::array<double, 5>  _imu_msg_type;
  _imu_msg_type imu_msg;

   typedef boost::array<int8_t, 4>  _imu_stat_type;
  _imu_stat_type imu_stat;





  typedef boost::shared_ptr< ::imu_vision_interaction::IMU_msg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::imu_vision_interaction::IMU_msg_<ContainerAllocator> const> ConstPtr;

}; // struct IMU_msg_

typedef ::imu_vision_interaction::IMU_msg_<std::allocator<void> > IMU_msg;

typedef boost::shared_ptr< ::imu_vision_interaction::IMU_msg > IMU_msgPtr;
typedef boost::shared_ptr< ::imu_vision_interaction::IMU_msg const> IMU_msgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::imu_vision_interaction::IMU_msg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::imu_vision_interaction::IMU_msg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::imu_vision_interaction::IMU_msg_<ContainerAllocator1> & lhs, const ::imu_vision_interaction::IMU_msg_<ContainerAllocator2> & rhs)
{
  return lhs.imu_msg == rhs.imu_msg &&
    lhs.imu_stat == rhs.imu_stat;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::imu_vision_interaction::IMU_msg_<ContainerAllocator1> & lhs, const ::imu_vision_interaction::IMU_msg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace imu_vision_interaction

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::imu_vision_interaction::IMU_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::imu_vision_interaction::IMU_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::imu_vision_interaction::IMU_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::imu_vision_interaction::IMU_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::imu_vision_interaction::IMU_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::imu_vision_interaction::IMU_msg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::imu_vision_interaction::IMU_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "affaccaeab02b87844ca1675a87c3358";
  }

  static const char* value(const ::imu_vision_interaction::IMU_msg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xaffaccaeab02b878ULL;
  static const uint64_t static_value2 = 0x44ca1675a87c3358ULL;
};

template<class ContainerAllocator>
struct DataType< ::imu_vision_interaction::IMU_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "imu_vision_interaction/IMU_msg";
  }

  static const char* value(const ::imu_vision_interaction::IMU_msg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::imu_vision_interaction::IMU_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64[5] imu_msg\n"
"int8[4] imu_stat\n"
;
  }

  static const char* value(const ::imu_vision_interaction::IMU_msg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::imu_vision_interaction::IMU_msg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.imu_msg);
      stream.next(m.imu_stat);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct IMU_msg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::imu_vision_interaction::IMU_msg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::imu_vision_interaction::IMU_msg_<ContainerAllocator>& v)
  {
    s << indent << "imu_msg[]" << std::endl;
    for (size_t i = 0; i < v.imu_msg.size(); ++i)
    {
      s << indent << "  imu_msg[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.imu_msg[i]);
    }
    s << indent << "imu_stat[]" << std::endl;
    for (size_t i = 0; i < v.imu_stat.size(); ++i)
    {
      s << indent << "  imu_stat[" << i << "]: ";
      Printer<int8_t>::stream(s, indent + "  ", v.imu_stat[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // IMU_VISION_INTERACTION_MESSAGE_IMU_MSG_H
