#include <stdio.h>
#include <stdint.h> // Include for int8_t
#define lli long long int

int countN(int start, int8_t digit) {
    int count = 0;

    while (start) {
        int rem = start % 10;
        if (rem == digit) {
            count++;
        }
        start /= 10;
    }
    return count;
}

int countTotalN(int8_t digit, int start, int end) {
    if (start > end) {
        return 0;
    }

    int count = 0;

    while (start != end + 1) {
        count += countN(start, digit);
        start++;
    }
    return count;
}

int8_t takeDigit() {
    int8_t digit;
    do {
        printf("Enter a digit (0-9): ");
        scanf("%hhd", &digit);
    } while (digit < 0 || digit > 9); // Validate input
    return digit;
}

int takeNonNegativeInt(const char s[]) {
    int x;
    do {
        printf("%s", s);
        scanf("%d", &x);
    } while (x < 0); // Validate non-negative input
    return x;
}

int main() {
    int8_t digit = takeDigit();
    int start = takeNonNegativeInt("Enter the start: ");
    int end = takeNonNegativeInt("Enter the end: ");
    printf("The number of %d from %d to %d is %d\n", digit, start, end, countTotalN(digit, start, end));
    return 0;
}
