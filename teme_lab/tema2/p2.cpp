#include <bits/stdc++.h>
using namespace std;

struct Point {
    int x, y;
};

struct Line {
    Point p1, p2;
};

int relativePosition(Point point, vector<Point> polygon) {
    int numCrossings = 0;
    int numVertices = polygon.size();

    for (int i = 0; i < numVertices; i++) {
        Line edge = {polygon[i], polygon[(i+1)%numVertices]};
        if (edge.p1.y == edge.p2.y) continue;  //skip horizontal edges

        // check the intersection
        if (point.y >= min(edge.p1.y, edge.p2.y) && point.y < max(edge.p1.y, edge.p2.y)) {
            double xIntersection = (double)(point.y - edge.p1.y) * (double)(edge.p2.x - edge.p1.x) / (double)(edge.p2.y - edge.p1.y) + edge.p1.x;
            if (point.x < xIntersection) {
                numCrossings++;
            }
        }
    }

    if (numCrossings % 2 == 1) {
        return 1;  // inside
    } else if (numCrossings % 2 == 0) {
        return -1;  // outside
    }
}
bool boundary(int x1,int y1,int x2,int y2,int x,int y)
{
	if (x <= max(x1, x2) && x >= min(x1, x2) && y <= max(y1, y2) && y >= min(y1, y2))
    {
        int crossProduct = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1);
        if(crossProduct==0)
            return true;
    }
	return false;
}

int main()
{
    vector<Point>polygon;
    int n;
	cin>>n;
	for(int i=0;i<n;i++)
    {
        int x,y;
        cin>>x>>y;
        polygon.push_back({x,y});
    }
    int m;
    cin>>m;


	for(int i=0;i<m;i++){
            int x,y;
            cin>>x>>y;
            Point p = {x,y};
            int ok=0;
            for(int j=0;j<n-1;j++)
                if(ok==0 && boundary(polygon[j].x,polygon[j].y,polygon[j+1].x,polygon[j+1].y,p.x,p.y)==true)
            {
                cout<<"BOUNDARY\n";
                ok=1;
            }
            if(ok==0 && boundary(polygon[n-1].x,polygon[n-1].y,polygon[0].x,polygon[0].y,p.x,p.y)==true)
            {
                cout<<"BOUNDARY\n";
                ok=1;
            }
        if(ok==0)
            {if(relativePosition(p,polygon)==1)
                cout<<"INSIDE\n";
            else
                cout<<"OUTSIDE\n";
            }
	}
    return 0;
}

