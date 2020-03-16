#include <iostream>
using namespace std;

int popLeft(int *arr) {
	int val = arr[0];
	int length = sizeof(arr)/sizeof(arr[0]);
	for(int i = 0; i < length-1; i++) {
		arr[i] = arr[i+1];
	}
	return val;
}

int getMid(int* arrs, int lengthArr, int data[] = {}, int queue[] = {}) {
	int lengthData = sizeof(data)/sizeof(data[0]);
	int lengthArrs = sizeof(arrs)/sizeof(arrs[0]);
	if(lengthData == lengthArr) {
		return *data;
	} else {
		if(lengthArrs == 2) {
			for(int i = 0; i < 2; i++) {
				int sizeArr = sizeof(arrs[i]/4);
				if(sizeArr != 0) {
					queue.append(arrs[i]);
				}	
			}
		} else {
			return *data;
		}
	}
}

int main() {
	

	return 0;
}

