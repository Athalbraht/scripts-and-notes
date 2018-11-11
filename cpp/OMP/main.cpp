#include <iostream>
//#include <boost/random.hpp>
//#include <boost/thread/thread.hpp>
#if defined(ENABLE_OPENMP)
#include <omp.h>
#else
typedef int omp_int_t;
inline omp_int_t omp_get_thread_num() { return 0;}
inline omp_int_t omp_get_max_threads() { return 1;}
#endif

//#include <omp.h>
//#include <mpi.h>
#include <stdio.h>
#include <unistd.h>
void f()
{
								std::cout<<"f"<<std::endl;
}

int main(int argc, char *argv[])
{


int th = atoi(argv[2]);
	unsigned int t=100000;//0000;
	int a=100;
	bool x=true;
	omp_set_num_threads(th);
	double t1,t2;
	t1=omp_get_wtime();

#pragma omp parallel if(x) shared(t)
{
#pragma omp sections nowait
	{
		#pragma omp setion
		{
						std::cout<<"x"<<std::endl;

						usleep(t);
}
				}
														printf("T %d/%d\n",
																					omp_get_thread_num(),
																					omp_get_num_threads());
																					usleep(t);

#pragma omp single
{
	printf("single %d/%d\n",
								omp_get_thread_num(),
								omp_get_num_threads());
								usleep(t);

}
#pragma omp for schedule(dynamic,11) lastprivate(a) nowait
																for(int i=0;i<13;i++)
																{
																	usleep(t);
																	a=i;
																				printf("T:%d, i:%d\n",omp_get_thread_num(), i);


}
//#pragma omp barrier
#pragma omp for schedule(dynamic,1)
																for(int i=0;i<13;i++)
																{
																	usleep(t);
																				printf("-->T:%d, i:%d\n",omp_get_thread_num(), i);
																}
								}
	t2 = omp_get_wtime();
								printf("\nA=%d\n",a);
							printf("\nTIME:%g\n",t2-t1);

								return 0;
}
