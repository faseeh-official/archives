#include <iostream>

// This line includes the standard input-output stream library, which allows the program to perform input and output operations.
// iostream (input output stream) is a part of the C++ standard library (or STL). It is a header.
// The iostream library contains the definitions for cin (standard input) and cout (standard output).

int main() {

// This line declares the main function.
// The main function code goes inside "{}".
// In C++, every program must have a main function, which serves as the entry point for execution.
// The end of the main function is the end of the program.
// The int before main() indicates that the function returns an integer value.

    std::cout << "Hello, World!" << std::endl;

// This line uses the cout object from the std namespace to output the string "Hello, World!" to the standard output (usually the console).
// "cout" is located in the standard library of C++. So we need to specify "std::" (standard) before "cout".
// In C++, << is the insertion operator, used to insert data into a stream, typically used with std::cout for output.
// On the other hand, >> is the extraction operator, used to extract data from a stream, commonly used with std::cin for input.
// std::endl is used to insert a newline character and flush the output buffer.

    return 0;

// This line marks the end of the main function.
// It returns an integer value of 0, indicating that the program terminated successfully.
// In C++, returning 0 from main typically signifies successful execution, while returning a non-zero value indicates an error condition.
// It is used as a standard way of finding how the program terminated. The user can't see it.

}