#include <stdio.h>
int main(){
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) {
        int f;
        scanf("%d", &f);
        arr[i] = f;
    }
    for (n; n > 0; n--){
        printf("%d\n", arr[n - 1]);
    }
    return 0;
}
