#include <stdio.h>

int main() {
    int n, t, r, s = 0;
    scanf("%d", &n);
    t = n;
    while (t > 0) {
        r = t % 10;
        s += r * r * r;
        t /= 10;
    }
    if (s == n)
        printf("Yes");
    else
        printf("No");
    return 0;
}
