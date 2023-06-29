#include <iostream>

using namespace std;
struct Punct{
    long long x,y;
};
long long verifica_cerc(Punct A,Punct B,Punct C, Punct R){
    return (A.x - B.x)*(C.y - B.y)*(R.x*R.x + R.y*R.y - B.x*B.x - B.y*B.y) +
    (C.x - B.x)*(R.y - B.y)*(A.x*A.x + A.y*A.y - B.x*B.x - B.y*B.y) +
    (R.x - B.x)*(A.y - B.y)*(C.x*C.x + C.y*C.y - B.x*B.x - B.y*B.y) -
    (R.x - B.x)*(C.y - B.y)*(A.x*A.x + A.y*A.y - B.x*B.x - B.y*B.y) -
    (C.x - B.x)*(A.y - B.y)*(R.x*R.x + R.y*R.y - B.x*B.x - B.y*B.y) -
    (A.x - B.x)*(R.y - B.y)*(C.x*C.x + C.y*C.y - B.x*B.x - B.y*B.y);
}
int main()
{
    Punct A,B,C,R;
    cin>>A.x>>A.y;
    cin>>B.x>>B.y;
    cin>>C.x>>C.y;
    int n;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        cin>>R.x>>R.y;
        if(verifica_cerc(A,B,C,R) == 0)
            cout<<"BOUNDARY\n";
        else
           if(verifica_cerc(A,B,C,R) > 0)
                cout<<"INSIDE\n";
        else
            cout<<"OUTSIDE\n";
           // cout<<verifica_cerc(A,B,C,R);
    }
    return 0;
}
