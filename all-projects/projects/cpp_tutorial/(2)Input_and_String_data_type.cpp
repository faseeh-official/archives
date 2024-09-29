#include <iostream>
#include <string> // To include `string` data type.
int main() {
    std::cout << "Enter you input: ";
    std::string Input;
    std::cin >> Input; // `>>` is the extraction operator (not an insertion operator (<<)).
    std::cout << Input;
    return 0;
}