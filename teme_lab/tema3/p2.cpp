#include<bits/stdc++.h>

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
    Punct A,B,C,D;
    cin>>A.x>>A.y;
    cin>>B.x>>B.y;
    cin>>C.x>>C.y;
    cin>>D.x>>D.y;
    if(verifica_cerc(A,B,C,D) <= 0)
        cout<<"AC: LEGAL\n";
    else
        cout<<"AC: ILLEGAL\n";
    if(verifica_cerc(B,C,D,A) <= 0)
        cout<<"BD: LEGAL\n";
    else
        cout<<"BD: ILLEGAL\n";
    return 0;
}
