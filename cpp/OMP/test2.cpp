#include <omp.h>
#include <stdio.h>
#include <unistd.h>


class X
{
	public:
		int a[10];
		int b;
		void seta()
		{
			for(int i=0;i<10;i++)
			{
				a[i] = i;
			}
		}
		void setb()
		{
			b = 99;
		}
		void print()
		{
			for(int i=0;i<10;i++)
			{
			printf("a[%d]=%d ",i,a[i]);
			}
			printf("\n%d\n",b);
		}
};

int main()
{
	const int t= 1000000;
#pragma omp parallel
#pragma omp for schedule(dynamic,1)
	for(int i=0;i<10;i++)
	{
		printf("T:%d i:%d\n",omp_get_thread_num(),i);
	}

	int a[1];
	a[0] = 0;
#pragma omp parallel 
#pragma omp for schedule(dynamic,1)  reduction(-:a)
	for(int i=0;i<10;i++)
	{
		a[0] -= i;
		printf("T:%d i:%d\n",omp_get_thread_num(),i);
	}

printf("a=%d",a[0]);

#pragma omp parallel sections
{
#pragma omp section
{
usleep(t);
printf("a\n");
usleep(t);
}

#pragma omp section
{
usleep(t);
printf("b\n");
usleep(t);
}
#pragma omp section
{
usleep(t);
printf("c\n");
}}
#pragma omp parallel
#pragma omp master
{printf("critical= %d\n",omp_get_thread_num());
usleep(t*3);
}


X* ob = new X();
#pragma omp parallel sections shared(ob)
{
#pragma omp section
	{ob->seta();}
#pragma omp section
	{ob->setb();}
}
ob->print();



struct en_omp
{
	int a;
	int b;
};

en_omp* xd = new en_omp();
xd -> a = 1;
xd -> b = 2;

printf("xd %d %d", xd->a,xd->b);


return 0;



}
