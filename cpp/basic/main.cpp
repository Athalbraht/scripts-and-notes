#include <iostream>
#include <stdio.h>
#include <templates.hpp>

int main(int argvc, char** argv)
{
	int template_f2 = template_f<int>(2);
	std::cout<<template_f2<<std::endl;
	
	templateclass<int,2000> x;
	x.set();
	x.print();
	
	
	printf("pass");
	return 0;
}
