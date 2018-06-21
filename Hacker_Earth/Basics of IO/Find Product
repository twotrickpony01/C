#include <stdio.h>
#include <math.h> 

int main () {
    int n;
    scanf("%d", &n);
    int arr[n];
    long long answer = 1;
    int pow_array = pow(10, 9) + 7;
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        answer = (answer * arr[i]) % pow_array;
    }
    printf("%d", answer);
}
