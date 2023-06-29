#include<iostream>
using namespace std;

void verifica_viraj(float xp,float yp,float xq,float yq,float xr,float yr) //verificam pozitita punctului R fata pe PQ
{
   float d;
   d = xq * yr + xp * yq + xr * yp - xq * yp - xr * yq - xp * yr;
   if(d == 0)
    cout<<"TOUCH\n";
   else if(d < 0)
    cout<<"RIGHT\n";
   else
    cout<<"LEFT\n";
}
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        float xp,xq,xr,yp,yq,yr;
        cin>>xp>>yp>>xq>>yq>>xr>>yr;
        verifica_viraj(xp, yp, xq, yq, xr, yr);
    }
}
