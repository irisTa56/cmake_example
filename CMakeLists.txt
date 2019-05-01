cmake_minimum_required(VERSION 2.8.12)
project(cmake_example)

find_package(pybind11)

IF(NOT pybind11_FOUND)
  add_subdirectory(pybind11)
  include_directories(pybind11/include)
ENDIF()

pybind11_add_module(cmake_example src/main.cpp)

target_link_libraries(cmake_example PRIVATE profiler)
