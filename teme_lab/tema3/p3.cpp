#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    long long a,b,c;
    long long max_x = -999999999,max_y = -999999999,min_x = 999999999,min_y = 999999999;
    for(int i=1;i<=n;i++)
    {
        cin>>a>>b>>c;
        if(b==0)
        {
            if(a>0){
                c=c/a;
                if(0-c < min_x)
                    min_x = 0-c;
            }
            else
            {
                c=c/(0-a);
                if(c > max_x)
                    max_x = c;
            }
        }
        else
            if(a == 0)
            {
                if(b>0){
                    c=c/b;
                    if(0-c < min_y)
                        min_y = 0-c;
                }
                else
                {
                    c=c/(-b);
                    if(c > max_y)
                        max_y = c;
                }
        }
    }
    if(max_x > min_x || max_y > min_y) //nu exista intersectie
        cout<<"VOID";
    else
        if(min_x == 999999999 || min_y == 999999999 || max_x == -999999999 || max_y == -999999999) //nemarginita
            cout<<"UNBOUNDED";
    else //marginita
        cout<<"BOUNDED";
    return 0;
}
