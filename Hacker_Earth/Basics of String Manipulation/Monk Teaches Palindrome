#include <stdio.h>
#include <string.h>

int main () {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        char string[100000];
        scanf("%s", string);
        size_t word_len = strlen(string);
        int word_is_palindrome = 1;
        for (int i = 0; i < word_len / 2; i++) {
            if (string[i] != string[word_len - 1 - i]) {word_is_palindrome = 0; break;}
            }
        if (word_is_palindrome == 0) {printf("NO\n");}
        if (word_is_palindrome == 1 && word_len % 2 == 0) {printf("YES EVEN\n");}
        if (word_is_palindrome == 1 && word_len % 2 == 1) {printf("YES ODD\n");}
        }
}    
