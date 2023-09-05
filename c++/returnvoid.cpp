#include <iostream>
#include <windows.h>

using namespace std;

double ct(double a, double b){
    
return a/b;

} 

int main(){
    SetConsoleOutputCP(65001);
    int i = 0;
    system("cls");
    while ( i < 3){
    double a, b;
    cout<< "Bạn A đi được quãng đường là: "; cin>>a;
    cout<<"Bạn A đi bao lâu: "; cin>>b; 
    cout<< "Bạn A chạy một chiếc xe đạp với quãng đường dài "<<a<<" km và đi trong vào "<< b << " h giờ. Hỏi bạn ấy đi đạt được vận tốc là nhiêu ? "<<endl; 
    Sleep(5000);
    
    double ketqua = ct(a,b);
    
    cout <<"Bạn đạt được vận tốc: "<< ketqua <<" km/h\n\n" <<endl; Sleep(2000);
    
    i++;
    }
    system("pause");
    return 0;
}
// 3
