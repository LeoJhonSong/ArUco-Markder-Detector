cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
#set(CMAKE_CXX_STANDARD 14)
#set(CMAKE_CXX_STANDARD_REQUIRED TRUE)
project(detect_markers)

find_package( OpenCV 3 REQUIRED)
set(OpenCV_LIBS ${OpenCV_LIBS})

include_directories( ${OpenCV_INCLUDE_DIRS} include)

file(GLOB SOURCES "calibrate_camera_charuco.cpp")
file(GLOB SOURCES "detect_board_charuco.cpp")
file(GLOB SOURCES "detect_markers.cpp")
add_executable(${PROJECT_NAME} ${SOURCES})
target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})
