#include <boost/interprocess/managed_shared_memory.hpp>
#include <boost/interprocess/allocators/allocator.hpp>
#include <boost/interprocess/containers/vector.hpp>
#include "Shm.hpp"
#include "bindShmVector.hpp"

typedef boost::interprocess::allocator<double, boost::interprocess::managed_shared_memory::segment_manager>  doubleAlecator;
typedef boost::interprocess::vector<double, doubleAlecator> scalerVector;

scalerVector * Vector(char * segmentName, const char * name){
    const doubleAlecator alloc_inst (segments.at(segmentName)->get_segment_manager());
    return segments.at(segmentName)->find_or_construct<scalerVector>(name)(alloc_inst);
}

PYBIND11_MAKE_OPAQUE(scalerVector);

namespace py = pybind11;
using namespace py;

#define PYVECTOR(m)              \
    bind_shm_vector<scalerVector>(m,"scalerVector"); \
    m.def("vector", &Vector); \



