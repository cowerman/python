/*************************************************************************
    > File Name: test.c
    > Author:		
    > Mail:		
    > Created Time: 2018年01月18日 星期四 16时14分40秒
 ************************************************************************/

#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#define size_4k (4*1024)
#define loop_count 1024*500
int main(int argc, char *argv[])
{

    int loop = loop_count;
    char **buf = NULL;
    int i = 0;
    int LOOP_COUNT = 0;
    int loop_countxx = 0;
    if (argc > 1)
	loop = atoi(argv[1]);

    printf("loop = %d\n", loop);
    buf = (char **) malloc(loop * sizeof(void *));

    if (buf == NULL) {
	printf("There is no enough memeory for running this test\n");
	return -1;
    }

    for ( ; ; ) {
//	printf("LOOP %d\n", LOOP_COUNT++);
	for ( i = 0 ;i < loop; i++)
	{
	printf("i=%d\n", i);

	    buf[i] = (char *) malloc(size_4k);
	    if (!buf[i]) {
		printf("malloc failed!!!\n");
		i--;
		continue;
	    }

	    buf[i][0] = 'a';
	    buf[i][size_4k -1] = 'b';

	    if (buf[i][0] == 'a' && buf[i][size_4k-1] == 'b') {

	    } else {
		printf("memeory access error!!\n");
	    }
	}

	sleep(15);

	for (i = 0; i < loop; i++)
	{
	    free(buf[i]);
	}
    }
    
    return 0;
}
