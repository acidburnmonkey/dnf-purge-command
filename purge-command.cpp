#include <Python.h>
#include <iostream>
#include <sstream>
#include <string>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <arg1> <arg2> <arg3> ..." << std::endl;
        return 1;
    }

    // Build the Python command with arguments
    std::ostringstream command;
    command << "import sys; sys.argv = ['./testing/args.py'";

    // Add C++ arguments as Python script arguments
    for (int i = 1; i < argc; ++i) {
        command << ", '" << argv[i] << "'";
    }
    command << "]; exec(open('./testing/args.py').read())";

    // Initialize the Python Interpreter
    Py_Initialize();

    // Execute the Python command
    int result = PyRun_SimpleString(command.str().c_str());
    if (result != 0) {
        std::cerr << "Error running Python script." << std::endl;
    }

    // Finalize the Python Interpreter
    Py_Finalize();

    return result;
}
