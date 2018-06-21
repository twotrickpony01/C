#include <stdio.h>
int main() {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        long n;
        scanf("%ld", &n);
        long k;
        scanf("%ld", &k);
        long rotated_A[n];
        for (long j = 0; j < n; j++) {
            long value;
            scanf("%ld", &value);
            long rotated_value_position = (j + k) % n;
            rotated_A[rotated_value_position] = value;
        } 
        for (long h = 0; h < n; h++) {printf("%ld ", rotated_A[h]);}
        printf("\n");
    }
}
