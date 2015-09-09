#include <iostream>
using namespace std;

int main(){
	cout << "201511208 유선규" << endl;

	int data[] = { 10, 20, 30, 40, 50, 60, 70, 80, 45, 23, 74, 58 };

	cout << "배열의 시작주소 : " << data << endl;
	cout << "첫번째 방의 주소 : " << &data[0] << endl;

	cout << "전체 배열 크기 : " << sizeof(data) << endl;
	cout << "방의 크기 : " << sizeof(data[0]) << endl;
	cout << "방의 개수 : " << sizeof(data) / sizeof(data[0]) << endl;

	return 0;
}