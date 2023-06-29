#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
struct Point{
    int x,y;
};
// function to check if a polygon is x-monotone
bool isXMonotone(vector<Point> polygon) {
    int n = polygon.size();
    int increasing = 0, decreasing = 0;
    bool x_increase=false;

    for (int i = 0; i < n-1; i++) {
        if (polygon[i].x < polygon[i+1].x && x_increase == false)
            {increasing ++;x_increase=true;}
        else if (polygon[i].x > polygon[(i+1)%n].x && x_increase == true)
            {decreasing ++;x_increase=false;}
    }
    if (increasing + decreasing>2)
            return false;
    return true;
}

// function to check if a polygon is y-monotone
bool isYMonotone(vector<Point> polygon) {
    int n = polygon.size();
    int increasing = 0, decreasing = 0;
    bool y_increase=false;
    for (int i = 0; i < n-1; i++) {
        if (polygon[i].y < polygon[i+1].y && y_increase == false)
            {increasing ++; y_increase = true;}
        else if (polygon[i].y > polygon[(i+1)%n].y && y_increase == true)
            {decreasing ++; y_increase = false;}

    }
    if (increasing + decreasing>2)
            return false;
    return true;
}
int main()
{
    int m,n,ok;
    long long d;
    cin>>n;
    vector<Point >polygon;
    for (int i=0;i<n;i++)
    {
        long long x,y;
        cin>>x>>y;
        polygon.push_back({x,y});
    }
    if(isXMonotone(polygon))
        cout<<"YES\n";
    else
        cout<<"NO\n";

    if(isYMonotone(polygon))
        cout<<"YES\n";
    else
        cout<<"NO\n";
}

