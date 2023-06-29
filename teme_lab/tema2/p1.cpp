#include<bits/stdc++.h>
using namespace std;
struct Point
{
    int x,y;
};
vector <Point> poligon;
long long verifica_viraj(Point p, Point q, Point r) //verificam pozitita punctului R fata pe PQ
{
    return 1LL *q.x * r.y + 1LL *p.x * q.y + 1LL *r.x * p.y - 1LL *q.x * p.y - 1LL *r.x * q.y - 1LL *p.x * r.y;
}
int main()
{
    int n,m;
    cin>>n;
    Point pMin;
    pMin.x = pMin.y = 10000;
    int pos = -1;
    for (int i=0;i<n;i++)
    {
        Point p;
        cin>>p.x>>p.y;
        poligon.push_back(p);
        if(p.x < pMin.x||(p.x == pMin.x && p.y < pMin.y))
        {
            pMin = p;
            pos = i;
        }
    }
    rotate(poligon.begin(), poligon.begin() + pos, poligon.end());

    cin>>m;
    for(int i=1; i<=m; i++)
    {
        Point p;
        cin>>p.x>>p.y;
        if(verifica_viraj(poligon[0], poligon[n-1], p) > 0 || verifica_viraj(poligon[0], poligon[1], p) < 0)
            cout << "OUTSIDE\n";
        else
        {
            int s = 1;
            int d = n-2;
            while(s <= d)
            {
                int  m = (s+d)/2;
                if(verifica_viraj(poligon[0],poligon[m],p)>0)
                {
                    s = m+1;
                }
                else
                {
                    d = m-1;
                }
            }
                long long a1, a2, a3, aTotal;
                a1 = abs(verifica_viraj(poligon[0], poligon[d], p));
                a2 = abs(verifica_viraj(p, poligon[d], poligon[s]));
                a3 = abs(verifica_viraj(poligon[0], p, poligon[s]));
                aTotal = abs(verifica_viraj(poligon[0], poligon[d], poligon[s]));
                    if(a1 + a2 + a3 == aTotal) {
                        if(verifica_viraj(poligon[s], poligon[d], p) == 0 || verifica_viraj(poligon[0], poligon[1], p) == 0 || verifica_viraj(poligon[0], poligon[n-1], p) == 0)
                            cout << "BOUNDARY\n";
                        else
                            cout << "INSIDE\n";
                    }
                    else
                        cout << "OUTSIDE\n";
        }
    }


    return 0;
}

