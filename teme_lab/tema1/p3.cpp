#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

long long verifica_viraj(long long xp,long long yp,long long xq,long long yq,long long xr,long long yr) //verificam pozitita punctului R fata pe PQ
{
   long long d;
   d = xq * yr + xp * yq + xr * yp - xq * yp - xr * yq - xp * yr;
   return d;
}
int main()
{
    int t,n,ok;
    long long d;
    cin>>t;
    vector<pair<long long,long long> > puncte;
    vector<int> acoperire; //multimea de puncte din acoperire
    pair<int, int> pMin = make_pair(100000, 100000); //cautam pozitia punctului cel mai din stanga jos
    int pos = 0;
    for (int i=0;i<t;i++)
    {
        long long x,y;
        cin>>x>>y;
        puncte.push_back(make_pair(x,y));
        if(puncte[i].first<pMin.first||(puncte[i].first==pMin.first && puncte[i].second < pMin.second))
        {
            pMin = puncte[i];
            pos = i;
        }
    }
    rotate(puncte.begin(), puncte.begin() + pos, puncte.end()); //rotim vectorul a.i. primul element sa fie cel mai din stanga jos

    puncte.push_back(puncte[0]);
    for(int i=0;i<puncte.size();i++)
    {
        ok=0;
        while(acoperire.size() >= 2 && ok == 0)
        {
            n = acoperire.size();
            d = verifica_viraj(puncte[acoperire[n-2]].first, puncte[acoperire[n-2]].second, puncte[acoperire[n-1]].first, puncte[acoperire[n-1]].second, puncte[i].first, puncte[i].second);
            if(d > 0) // daca e viraj la stanga mergem la urmatorul punct
                ok=1;
            else
                acoperire.pop_back(); //altfel stergem ultimul punct din acoperire si il verificam cu penultimul punct din acoperire...

        }
        acoperire.push_back(i);//daca am terminat verificarile il adaugam la acoperire
    }
    acoperire.pop_back();
    cout<<acoperire.size()<<endl;
    for(int i = 0;i<acoperire.size();i++)
        cout<<puncte[acoperire[i]].first<<" "<<puncte[acoperire[i]].second<<endl;
    return 0;
}
