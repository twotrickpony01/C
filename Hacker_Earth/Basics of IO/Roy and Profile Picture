#include <stdio.h>
int main() {
    int number_of_photos;
    int length;
    scanf("%d", &length);
    scanf("%d", &number_of_photos);
    for (int i; i < number_of_photos; i++) {
        int width;
        int height;
        scanf("%d", &width);
        scanf("%d", &height);
        if (width >= length && height >= length) {
            if (width == height) {
                printf("ACCEPTED\n");
            } else {
                printf("CROP IT\n");
            }
        } else {
            printf("UPLOAD ANOTHER\n");
        }
  }
}
