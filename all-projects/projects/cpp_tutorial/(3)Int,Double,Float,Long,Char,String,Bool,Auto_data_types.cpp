#include <iostream>
#include <string>
int main() {
    std::string name = "Faseeh";
    // String data type. It's a part of STL. So we need to add the prefix "std::" and the header "#include <string>".
    // But we don't need the prefix "std::" and a header for int, long, float, double etc as they are not part of STL.
    // Data types like int, long, float, double etc are fundamental data types in C++.

    int age = 16;
    long height = 160;
    // The long type is often used when you need to store integer values that might exceed the range of values that can be represented by a standard int.
    // Typically, int is represented using 4 bytes (32 bits) on most modern systems.
    // Usually, long is represented using 4 bytes (32 bits) as well, but it's designed to hold larger values than int.
    // On some systems, particularly 64-bit systems, long is represented using 8 bytes (64 bits).
    // It's important to note that the sizes mentioned above are common conventions, but they're not guaranteed by the C++ standard.
    // To determine the exact sizes of int and long on your specific compiler and platform, you can use the sizeof operator.

    // Using the sizeof operator to find the size of int and long.
    std::cout << "Size of int: " << sizeof(int) << "bytes" << std::endl;
    std::cout << "Size of long: " << sizeof(long) << " bytes" << std::endl;

    float height = 162.23;
    double height = 162.23;
    // Both float and double are used to store decimals.
    // Double provides higher precision than float.
    // It typically has 15 decimal digits of precision, while float usually has around 7 decimal digits of precision.
    // Double typically requires twice as much memory as float.
    // On most systems, float is represented using 32 bits (4 bytes), while double is represented using 64 bits (8 bytes).
    
    char letter_a = 'a';
    // char data type contain a single character.
    // !---IMPORTANT---! To assign a value to a char data type, you must use single quotes ('), not double quotes(").

    bool cpp_is_great = true;
    // Bool (boolean) stores true or false.

    // Here, the compiler finds out the data type automatically.
    auto x = 5; // Compiler deduces that x is of type int
    auto y = 3.14; // Compiler deduces that y is of type double

    return 0;
}
