#ifndef SHM_HPP
#define SHM_HPP
#include <boost/interprocess/managed_shared_memory.hpp>
#include <vector>
#include <iostream>

using namespace boost::interprocess;

extern std::map<const char *,managed_shared_memory*> segments;
typedef std::pair<char*,managed_shared_memory*> shmHandle;


void open_or_create_shm(char * name,int size){
    auto segment = segments.find(name);
    if(segment == segments.end()){
        managed_shared_memory * segment = new managed_shared_memory(open_or_create,name,size);
        segments.insert(shmHandle(name,segment));
    }
    
}
managed_shared_memory * get_segment(char * name){
    auto  _handle = segments.find(name);
    if (_handle == segments.end()){
        std::cout<<"segment :"<<name<<" dose not exist in the table."<<std::endl;
        auto segment = new managed_shared_memory(open_only,name);
        return segment;
    }
    return _handle->second;
}

class scalar{
public:
    scalar(char * segmentName,char * name){
        auto segment = get_segment(segmentName);
        value = segment->find_or_construct<double>(name)(0);
    }
    double * value;
    void set(double& _value){
        *value = _value;
    }
    double * get(){
        return value;
    }
    
};


// void remove(char * name){
//     shared_memory_object::remove(segments.at(name));  
// }

#define PYSHM(m) \
      m.def("open_or_create_shm",&open_or_create_shm,py::return_value_policy::reference); \
      py::class_<scalar>(m, "scalar") \
        .def(py::init<char *,char *>()) \
        .def_property("value", &scalar::get, &scalar::set,py::return_value_policy::reference);

#endif