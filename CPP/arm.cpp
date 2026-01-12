#include<iostream>
#include<cmath>
using namespace std;


int main(){
    int n = 371;
    int copy_n = n;
    int count = 0;
      // Count digits
    while(copy_n>0){
        copy_n=copy_n/10;
        count++;
    }
    copy_n=n;
    int val =0;
    // Sum of digits^count
    while (copy_n>0)
    {
        int digit = copy_n%10;
        val += pow(digit,count);
        copy_n=copy_n/10;
    }
    
    if(val==n){
        cout<<"TRUE";
    }
    else{
        cout<<"False";
    }
}