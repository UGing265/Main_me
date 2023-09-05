#include <iostream>
#include "windows.h"

#include <cstdlib>
#include "phude.cpp"
using namespace std;
  
int main (){ 
    system("cls");
    SetConsoleOutputCP(65001);
    
    int a,b;
    string x;
    
    cout<<"\tNhập số tiền cần thanh toán: ";
     cin>>a ; cin >>b; cout<<" Đang xử lý..."<<endl; Sleep(2000);
     double c = ct(a,b);
     cout<< c;
    cout<<"\tNhập số lượng: " ;
     cin>>b; cout<<"đang tính toán..."<<endl;Sleep(2000);

    cout<<"Nhập tên con card cần tìm: "; Sleep(1000);// nhap sai ten thi di ve
    cin >> x;   

    
    cout<<"in ra phai\n"; 
    
    cout<<"yes hay no: \n"; //dem tu 10 den 1 ma ko phan hoi thi tu bo -> tro lai giao dien nhap so tien
    
    cout<<"xac nhan ?\n"; //dem tu 10 den 1 ma ko phan hoi thi tu bo -> tro lai giao dien nhap so tien
    
    cout<<"dang thanh toan..\n.";

    cout<<"da mua thanh cong \n";
    
    cout<<"dang giao hang \n";
    
    cout<<"cam on quy khach da ung ho<3\n";

}
