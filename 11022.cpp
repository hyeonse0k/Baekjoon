#include <iostream>
using namespace std;

int main(void)
{
	int count;
	cin >> count;
	for (int i = 0; i < count; i++)
	{
		int a, b;
		cin >> a >> b;
		cout << "Case #" << i + 1 << ": " << a << " + " << b << " = " << a + b << endl;
	}
}