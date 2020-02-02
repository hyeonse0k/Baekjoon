#include <iostream>
using namespace std;

int main(void)
{
	int hour, min;
	cin >> hour >> min;
	
	if (hour == 0 && min < 45)
	{
		hour = 23;
		min = min + 15;
	}
	else if (min < 45) {
		hour -= 1;
		min += 15;
	}
	else if(min >= 45){
		min -= 45;
	}
	cout << hour <<" "<< min << endl;
	
}