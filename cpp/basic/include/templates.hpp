#include <omp.h>
#include <unistd.h>
template<class type>
type template_f(type x)
{
	type result = x*2;
	return result;
}


template<class type, int n>
class templateclass
{
	public:
	type tab[n];
	
	void set()
	{
#pragma omp parallel for schedule(static,1)
	
	for(int i=0;i<n;i++){tab[i] = i;
		usleep(10000);
		}
	
}
	void print()
	{
	for(int i=0;i<n;i++){std::cout<<"template class tab[i]="<<i<<std::endl;}
}
	};
