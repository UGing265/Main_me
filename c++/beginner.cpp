/*#include<stdio.h>

int main () {
int a;
printf("NHAP: ");
scanf("%d",&a);
switch(a) {
case 2:printf("LOL ?");
break;
default:printf("WWTF?");
}
return 0;
}*/
/*#include<stdio.h>

int main() {
	for (int i = 1; i <= 10; i++) {
		printf("gay\n");
	}
	return 0;
}*/
/*#include<stdio.h>

int main() {
    int a;
    scanf("%d",&a);
    for (int n=-5; n<=a;n++){
        printf("%d ",n);
    }
    return 0;
}*/
/*#include<stdio.h>
int main() {
    int a,b;
    scanf("%d %d",&a,&b);
    for (int i =a;i<=b;i++){
        if(i%3==0){
            printf("%d",i);
        }
    }
    return 0;
}*/
/*#include<stdio.h>

int main() {
    int a,b=1;
    scanf("%d",&a);
    for (int i=1;i<=a;i++){
        b=b*i;
        printf("%d ",b);
    }
    
    return 0;
}*/


/*int main() {
	int n;
    int a=1;
    int b=0;
	scanf("%d",&n);
	while (a<=n){
         if( n%a ==0){
			 b++;
             printf("b  is here: %d\n",b);
		 }
		 a++;
         printf("                    A--- %d\n",a);
	}
	printf("%d",b);
	return 0;
}*/
//#include<stdio.h>

/*int main() {
    int a,b;
    int sum=1,n=0;
    printf("a: ");
    scanf("%d",&a);
    printf("b: ");
    scanf("%d",&b);
    while (n<b){
        sum=sum*a;
        n++;
    }
    printf("%d",sum);
    return 0;
}*/
/*#include<stdio.h>

int main() {
	int a,b;
	scanf("%d %d",&a,&b);
	int n;
	while(n<=b){
		if(n % 3==0 && n % 5== 0){
			printf("%d ",n);
		}
		n++;
	}
	return 0;
}
#include<stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int a[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    int maxValue = a[1000]; //a0=1 a1 =5 a2 =10 a3 = 2
    /*for (int i = 0; i < n; i++) {
        if (a[i] > maxValue) {
            maxValue = a[i];
        }
    }
    printf("%d", maxValue);
    printf("%d",maxValue);
    return 0;
}
#include<stdio.h>

int main() {
    int n;
    int arr[n];
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    
    }
for (int i=0;i<n;i++){
if (arr[i]%2==0){
    printf("%d ",arr[i]);
}
}
    return 0;
}
#include<stdio.h>

int main() {
    int n,m,arr[100][100];
    scanf("%d %d",&n,&m);
    for (int i = 0; i<n; i++){
for (int j = 0; j < m ; j++){
          scanf("%d",&arr[i][j]);
     printf("%d",arr[i][j]);
    }
     
     }
    
    return 0;
}*/
#include<stdio.h>
#include<string.h>

int main() {
    char c='a';
   
    printf("%d",c);
    return 0;
}

