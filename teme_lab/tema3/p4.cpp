#include <bits/stdc++.h>
#include <vector>
#include <limits>
using namespace std;
struct Line {
    long long a,b,c;
};
struct Point{
    float x,y;
};
int main()
{
    int n;
    cin>>n;
    vector<Line> linii;
    long long min_x= LLONG_MAX,min_y= LLONG_MAX,max_x= LLONG_MIN,max_y= LLONG_MIN;
    for (int i=0;i<n;i++)
    {
        Line p;
        cin>>p.a>>p.b>>p.c;
        linii.push_back(p);
    }
    vector<Point> intersection;
    for(int i=0;i<n;i++)
        if(linii[i].a == 0)
        {
            //dr orizontala
            Point p;
            p.y =  0 - float(linii[i].c / linii[i].b);
            if(p.y < min_y) min_y = p.y;
            if(p.y > max_y) max_y = p.y;
            for(int j=0;j<n;j++)
                if(linii[j].b == 0)//dr verticala
            {
                p.x = 0 - float(linii[j].c / linii[j].a);
                if(p.x < min_x) min_x = p.x;
                if(p.x > max_x) max_x = p.x;
                intersection.push_back(p);
            }

        }
    /*cout<<"\n--------------------------\n";
    for(int i=0;i<intersection.size();i++)
        cout<<intersection[i].x <<" "<<intersection[i].y<<endl;

    cout<<"\n--------------------------\n";*/
    int m;
    cin>>m;
    Point p;
    //cout<< min_x <<" "<<max_x << " "<<min_y << " "<<max_y<<endl;
    for(int i=0;i<m;i++)
    {
        cin>>p.x>>p.y;
        //cout<<p.x<<" "<<p.y;
        if(min_x == LLONG_MAX || min_y == LLONG_MAX || max_x == LLONG_MIN || max_y == LLONG_MIN)
            {cout<<"NO\n";}
        else
            if(float(p.x) <= float(min_x) || float(p.x) >= float(max_x) || float(p.y) <= float(min_y) || float(p.y) >= float(max_y))
                {cout<<"NO\n";}
        else{
            long long x_max_st = LLONG_MIN, x_min_dr = LLONG_MAX , y_max_jos =LLONG_MIN, y_min_sus =LLONG_MAX;
            for(int j = 0 ;j <intersection.size();j ++)
            {
                if(p.x > intersection[j].x && x_max_st < intersection[j].x)
                {
                    x_max_st = intersection[j].x;
                }
                if(p.x < intersection[j].x && x_min_dr > intersection[j].x)
                {
                    x_min_dr = intersection[j].x;
                }
                if(p.y > intersection[j].y && y_max_jos < intersection[j].y)
                {
                    y_max_jos = intersection[j].y;
                }
                if(p.y < intersection[j].y && y_min_sus > intersection[j].y)
                {
                    y_min_sus = intersection[j].y;
                }
            }
            float arie;
            //cout<<x_min_dr <<" "<<x_max_st <<" "<<y_min_sus<<" "<<y_max_jos;
            arie = abs(x_min_dr - x_max_st) * abs(y_min_sus - y_max_jos);
            cout<< fixed << setprecision(6) <<"YES\n"<<arie<<endl;
        }
    }
    return 0;
}
