#include <omp.h>
#include <stdio.h>
#include <unistd.h>
#include <iostream>

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


int main(int argc,char** argv)
{
	
X* obj = new X();
int time = 1000000;
int tr;
tr=atoi(argv[1]);
//std::cin>>tr;
//std::cout<<typeid(tr).name()<<std::endl;
omp_set_num_threads(tr);

#pragma omp parallel shared(tr)
{
#pragma omp for schedule(static,4) nowait
for(int i=0;i<10;i++)
{
	printf("i=%d (Thread:%d/%d)\n", i, omp_get_thread_num(), omp_get_num_threads());
	usleep(time);
}
#pragma omp atomic
tr++;
#pragma omp single
{
printf(" Single %d  proc %d \n", omp_get_thread_num(),omp_get_num_procs());
usleep(time);}

#pragma omp sections
{
	#pragma omp section
	{printf("sec 1 (Thread:%d/%d)\n", omp_get_thread_num(), omp_get_num_threads());usleep(time);}
	#pragma omp section
	{printf("sec 2 (Thread:%d/%d)\n", omp_get_thread_num(), omp_get_num_threads());usleep(time);}
	#pragma omp section
	{printf("sec 3 (Thread:%d/%d)\n", omp_get_thread_num(), omp_get_num_threads());usleep(time);}
}
}
printf("inv barrier-----------\n");
#pragma omp parallel for schedule(static,1) num_threads(2)
for(int i=0;i<10;i++)
{
	printf("-j=%d (Thread:%d/%d)\n", i, omp_get_thread_num(), omp_get_num_threads());
}

obj->seta();
obj->setb();
int temp = 0;
#pragma omp parallel sections default(none) shared(obj) lastprivate(temp)
{
#pragma omp section
{obj->b=1;temp=99;}
#pragma omp section
{obj->a[1]=10;}	
}
obj->print();
printf("temp=%d\n",temp);
return 0;



}
