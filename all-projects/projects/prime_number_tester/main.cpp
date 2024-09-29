#include<iostream>
#include<cmath>

bool isPrime(int n) {
    if (n <= 1)
        return false;
    for (int i = 2; i <= sqrt(n); ++i) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    while (true) {
        // Storing input in "input":
        std::cout << std::endl << "Enter a number: ";
        int input;
        std::cin >> input; 

        // If the input is 1:
        if (input == 1) {
            std::cout << "1 is neither prime nor composite." << std::endl;
            continue;
        }

        // Checking whether the "input" is prime:
        if (isPrime(input)) {
            std::cout << "The number is prime." << std::endl;
        } else {
            std::cout << "The number is composite." << std::endl;
        }        
    }

    return 1;
}
