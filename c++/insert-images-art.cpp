#include <iostream>
#include <string>
#include <fstream>
#include <stdio.h>
#include <conio.h>
#include <ctime>
#include <vector>
#include "windows.h"
using namespace std;



void SetColor(WORD color) 

{
	HANDLE hConsoleOutput;
	hConsoleOutput = GetStdHandle(STD_OUTPUT_HANDLE);

	CONSOLE_SCREEN_BUFFER_INFO screen_buffer_info;
	GetConsoleScreenBufferInfo(hConsoleOutput, &screen_buffer_info);

	WORD wAttributes = screen_buffer_info.wAttributes;
	color &= 0x000f;
	wAttributes &= 0xfff0;
	wAttributes |= color;

	SetConsoleTextAttribute(hConsoleOutput, wAttributes);
}


int main()
{
	string ngiu;
	while (true)
	{
		SetConsoleOutputCP(65001);
		system("cls");
		cout << endl << endl;
		cout << "\t\tSinh nhật Phương Thy là ngày: ";
		getline(cin, ngiu);
		if (ngiu == "23/01")
		{
			cout << "\t\t---Chúc mừng bạn nhận được một phần quà---" << endl <<endl;
            cout << "\t\tHÃY BẮT ĐẦU CHUẨN BỊ" << endl; Sleep(2000);
			cout << "\t\t5" << endl; Sleep(1000);
			cout << "\t\t4" << endl; Sleep(1000);
			cout << "\t\t3" << endl; Sleep(1000);
			cout << "\t\t2" << endl; Sleep(1000);      
			cout << "\t\t1" << endl; Sleep(1000);
			cout << "\t\t..." << endl << endl; Sleep(1);

			vector <int> A;
			A.push_back(7);
			A.push_back(12);
			A.push_back(14);
			A.push_back(10);
			while(true)
			{
				int i = 0;
				SetColor(A.at(i++ % A.size()));

				ifstream file;
				file.open("E:\\CC+\\huongdan\\simp.txt", ios_base::in);
				string line;
				while (getline(file, line)) {
					cout << line << endl;
					Sleep(30); 
				}
				file.close();

				break; 
			
				
			}
			_getch();
		}
		else
		{
			cout << "\t\tSAI ROI ;((" << endl << endl;
			system("pause");
		}
	}
}