#include <iostream>
//#include <boost/random.hpp>
//#include <boost/thread/thread.hpp>
#include <omp.h>
//#include <mpi.h>
#include <stdio.h>
void f()
{
	std::cout<<"f"<<std::endl;
}

int main()

{
#pragma omp parallel
	//std::cout<<"x"<<std::endl;
	printf("T %d/%d\n",
			omp_get_thread_num(),
			omp_get_num_threads());	

	std::cout<<"MT"<<std::endl;

return 0;
}
