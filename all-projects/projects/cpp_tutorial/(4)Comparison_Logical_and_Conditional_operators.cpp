#include<iostream>
#include<string>

int main(){

    // Comparison operators:
    bool a = 10 > 5; // 'a' variable becomes true as 10 is greater than 5.
    bool b = 10 == 10; // 'b' variable becomes true as 10 is equal to 10.
    bool c = 10 != 5; // 'c' variable becomes true as 10 is not equal to 5.



    // Logical operators:
    bool d = a && b; // Logical AND. 'd' becomes true if both conditions are true.
    bool e = a || b; // Logical OR. 'e' becomes true of either of the conditions are true.
    bool f = !a;     // Logical NOT. 'f' becomes false if the condition is true and vice versa.

    // Logical if, else if and else:
    int temperature = 100;
    if (temperature < 37){
        // ...
    }
    else if (temperature < 40){
        // ...
    }
    else {
        // ...
    }



    // Conditional operator:
    int sales = 5'000;
    double commision = (sales < 10'000) ? 0.05 : 0.1;
    // If the condition inside the brackets is true, the first value (0.05) is assigned to the variable (commission).
    // If the condition inside the brackets is false, the second value (0.1) is assigned to the variable (commission).

    switch (1+2) { // Expression goes inside brackets"()".
        case 1: // If the result of the expression is 1, this code gets executed.
            // ...
            break; // Break breaks the switch statement.
        case 2: // If the result of the expression is 2, this code gets executed.
            // ...
            break;
        default: // If none of the cases match, this code gets executed.
            // ...
    }

    return 0;
}