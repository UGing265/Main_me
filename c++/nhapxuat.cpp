#include <iostream>
#include <fstream>
#include <windows.h>
using namespace std;

int main(){

    //Beep(523,500); 
    
    int n;
    string name;
    ifstream fi("input.txt");   // mo file de doc
    ofstream fo("output.txt");  // mo file de ghi
     
    fi >> n;                  // doc 1 so tu file
    getline(fi, name);          // loai bo dau xuong dong sau khi doc so n
 
    for (int i = 0; i <n; i++)
    {
        getline(fi, name);      // doc 1 dong tu file
        fo << (i+1) << "." << name << '\n';     // ghi 1 dong ra file
    }
 
    fi.close();
    fo.close();

    return 0;
}