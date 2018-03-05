/*************************************************************************
    > File Name: test.c
    > Author:		
    > Mail:		
    > Created Time: 2017年12月01日 星期五 11时12分03秒
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>

int comp(const void *a, const void *b)
{
    const int *aa = a;
    const int *bb = b;

    if (*aa > *bb) {
	return 0;
    }

    if (*aa < *bb) {
	return 0;
    }

    return 0;

}

int main()
{
    int c[] = {2, 9, 3, 8, 4, 1, 5, 7, 6};
    int i;
    printf("sizeof(c)=%d, sizeof(c)/sizeof(c[0])= %d\n", sizeof(c), sizeof(c)/sizeof(c[0]));
    printf("Before Sort: ");
    for(i = 0; i < sizeof(c)/sizeof(c[0]); i ++)
	printf("%d ", c[i]);
    qsort(&c[0], sizeof(c)/sizeof(c[0]), sizeof(c[0]), comp);
    printf("\nAfter Sort: ");
    for(i = 0; i < sizeof(c)/sizeof(c[0]); i ++)
	printf("%d ", c[i]);
    printf("\n");

    return 0;
}
