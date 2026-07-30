#include<iostream>
using namespace std;
int main()
{
	int a = 5;
	int *p = &a;
	
	cout << "Value of num : " << a << endl;
  	cout << "Address of num : " << &a << endl;
	cout << "Value stored in p : " << p << endl;
	cout << "Value pointer to by p : " << *p << endl;
	
	*P = 20;
	
	cout << " Updated value of a : " << a << endl;
	
	return 0;
}