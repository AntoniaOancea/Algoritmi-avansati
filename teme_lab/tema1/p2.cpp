#include<iostream>
#include<vector>
using namespace std;

float verifica_viraj(float xp,float yp,float xq,float yq,float xr,float yr) //verificam pozitita punctului R fata pe PQ
{
   float d;
   d = xq * yr + xp * yq + xr * yp - xq * yp - xr * yq - xp * yr;
   return d;
}
int main()
{
    int t;
    float d;
    cin>>t;
    int c0 = 0, cs = 0, cd = 0; // c0 - pe aceeasi drepta , cs - viraj la stanga, cd - viraj la dreapta
    vector<pair<int,int> > puncte;
    for(int i=0;i<t;i++)
    {
        int x,y;
        cin>>x>>y;
        puncte.push_back(make_pair(x,y));
        if(i>1)
        {
            d = verifica_viraj(puncte[i-2].first, puncte[i-2].second, puncte[i-1].first, puncte[i-1].second, x, y);
            if(d == 0) c0 ++;
                else
                    if(d < 0) cd ++;
            else
                cs ++;
        }
    }
    d = verifica_viraj(puncte[t-2].first, puncte[t-2].second, puncte[t-1].first, puncte[t-1].second, puncte[0].first, puncte[0].second);
            if(d == 0) c0 ++;
                else
                    if(d < 0) cd ++;
            else
                cs ++;
    cout<<cs<<" "<<cd<<" "<<c0;
}
