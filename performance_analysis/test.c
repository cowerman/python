/*************************************************************************
    > File Name: test.c
    > Author:		
    > Mail:		
    > Created Time: 2018年01月18日 星期四 16时14分40秒
 ************************************************************************/

#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>
#include<sys/times.h>

#define size_4k (4*1024)
#define loop_count 1024*25
#define data_size (loop_count/size_4k)	// 100M

int main(int argc, char *argv[])
{

    int loop = loop_count;
    char **buf = NULL;
    int i = 0;
    char *c;
    int clk_tck;
    clock_t begin, end;
    struct tms begin_tms, end_tms;
    double read_speed, write_speed;
    double read_time, write_time;

    if (argc > 1)
	loop = atoi(argv[1]);

    //printf("loop = %d\n", loop);
    buf = (char **) malloc(loop * sizeof(void *));

    if (buf == NULL) {
	printf("There is no enough memeory for running this test\n");
	return -1;
    }

    for ( ; ; ) {
	// allocate memory 100M
	for ( i = 0 ;i < loop; i++)
	{
	    buf[i] = (char *) malloc(size_4k);
	    if (!buf[i]) {
		printf("malloc failed!!!\n");
		i--;
		continue;
	    }
	}
	// times init
	clk_tck = sysconf(_SC_CLK_TCK);

	// write speed: datas / times
	begin = times(&begin_tms);
	for (i = 0; i < loop; i ++) {
	    memset(buf[i], 0xff, size_4k-1);
	}
	end = times(&end_tms);
	write_time = (end - begin) / (double)clk_tck;
	write_speed = data_size / write_time;

	c = &buf[0][0];
	// read speed: datas / times
	begin = times(&begin_tms);
	for (i = 0; i < loop * size_4k; i ++) {
	    if (*c != 0xff) {
		printf("read data %d %d is not previous set !!\n", *c, i);
		return -1;
	    }
	}
	end = times(&end_tms);
	read_time = (end - begin) / (double)clk_tck;
	read_speed = data_size / read_time;

	printf("read_speed: %lf\twrite_speed: %lf\n", read_speed, write_speed);

	// free these memory
	for (i = 0; i < loop; i++)
	{
	    free(buf[i]);
	}
    }
    
    return 0;
}
