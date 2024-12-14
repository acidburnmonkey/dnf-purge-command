cmake_minimum_required(VERSION 3.10)

# Project name
project(MyProject)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Source files
set(SOURCES
    main.cpp
    template.cpp
)

# Header files (optional, for IDEs and organization)
set(HEADERS
    template.hpp
    arguments.hpp
)

add_definitions(-DGETTEXT_DOMAIN="dnf5")
# Create the executable
add_executable(MyProject ${SOURCES} ${HEADERS})

# Include directories
target_include_directories(MyProject PRIVATE ${CMAKE_SOURCE_DIR})

# Link libraries (if any are required)
target_link_libraries(MyProject PRIVATE libdnf5)
