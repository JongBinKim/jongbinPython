#include <iostream>
using namespace std;

int main(){
	cout << "201511208 ������" << endl;

	int data[] = { 10, 20, 30, 40, 50, 60, 70, 80, 45, 23, 74, 58 };

	cout << "�迭�� �����ּ� : " << data << endl;
	cout << "ù��° ���� �ּ� : " << &data[0] << endl;

	cout << "��ü �迭 ũ�� : " << sizeof(data) << endl;
	cout << "���� ũ�� : " << sizeof(data[0]) << endl;
	cout << "���� ���� : " << sizeof(data) / sizeof(data[0]) << endl;

	return 0;
}