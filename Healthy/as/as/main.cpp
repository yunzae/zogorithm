// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int i,*ptr;
    int array[] = {10,20,30,40,50};
    ptr=array;
    printf("%d\n",array);
    printf("%d %d\n",&array[3],array[3]);
    printf("%d\n",*(ptr+2));
    printf("%d\n",*(ptr+2)+6);
    printf("%d\n", ptr+2);
    printf("%d\n",(ptr+2)-1);
    printf("%d\n",*(ptr+2)-1);
    return 0;
}
