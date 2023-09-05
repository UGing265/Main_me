#include <iostream>
#include <cstdlib> // for rand() and srand()
#include <ctime> // for time()
#include <windows.h>
using namespace std;
 int dota(int a, int b){
	return a + rand() % (b - a + 1);
 }
int main(){
	SetConsoleOutputCP(65001);
	
   int x,y;
   cout<<"Nhập dota vào: ";
   cin >> x;
   cout<<"Nhập dota vào: ";
   cin >> y;
    
	srand(time(0));
	for (int i = 0 ; i <= 10; i++){
	int a = dota(x,y);
  
  cout <<"ĐẾM " << i <<": "<< a << "   " ;
	}
	


 
	return 0;
}