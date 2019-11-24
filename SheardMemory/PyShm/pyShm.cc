#include "Representations/Shm.hpp"
#include "Representations/ScalerVector.hpp"
#include <pybind11/pybind11.h>

std::map<const char *,managed_shared_memory*> segments;

namespace py = pybind11;
PYBIND11_MODULE(pyShm, m) {
   PYSHM(m)
   PYVECTOR(m)
 
} 