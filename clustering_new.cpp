#include<bits/stdc++.h>
using namespace std;

int totalPoints = 22;

#define pi 3.1416

struct point
{
    double x, y;
};

struct endPoint
{
    point a, b;
};

double pointDistance(point a, point b)
{
    return sqrt(((a.x - b.x) * (a.x - b.x)) + ((a.y - b.y) * (a.y - b.y)));
}

point centroid(point points[100], int n)
{
    point centre;
    centre.x = 0;
    centre.y = 0;
    for(int i=0; i<n; i++)
    {
        centre.x += points[i].x;
        centre.y += points[i].y;
    }
    cout << centre.x << " " << centre.y << "\n";
    centre.x /= n;
    centre.y /= n;

    return centre;
}

double radius(point points[100], int n)
{
    point centre = centroid(points, n);
    double rad = 0.0, pointDist;
    for(int i=0; i<n; i++)
    {
        pointDist = pointDistance(centre, points[i]);
        if(pointDist > rad)
        {
            rad = pointDist;
        }
    }
    return rad;
}

double diameter(point points[100], int n)
{
    double diam = 0.0, pointDist;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            pointDist = pointDistance(points[i], points[j]);
            if(pointDist > diam)
            {
                diam = pointDist;
            }
        }
    }
    return diam;
}

endPoint diameterPoints(point points[100], int n)
{
    double diam = 0.0, pointDist;
    endPoint dep;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            pointDist = pointDistance(points[i], points[j]);
            if(pointDist > diam)
            {
                diam = pointDist;
                dep.a = points[i];
                dep.b = points[j];
            }
        }
    }
    return dep;
}

/*double fn(point points[100], int n, int mode)
{
    double rad = radius(points, n);

    //double r_by_nr = (totalPoints - n)

}*/


int main()
{
    /*while(true)
    {
        point a, b;
        cin >> a.x >> a.y >> b.x >> b.y;
        cout << pointDistance(a, b) << "\n";
    }*/

    point testPoint1;
    testPoint1.x = 7;
    testPoint1.y = 13;

    point testPoint2;
    testPoint2.x = 2;
    testPoint2.y = 12;


    /*int n;
    cin >> n;
    point points[100];
    for(int i=0; i<n; i++)
    {
        cin >> points[i].x >> points[i].y;
    }*/
    /***-----------------------------------------------------case 1----------------------------------------------------*/
    /***------------------------------------------------whole point set-------------------------------------------------*/
    //point points[]={{2, 14}, {3, 17}, {5, 21}, {7, 13}, {9, 16}, {10, 20}, {2, 4}, {3, 6}, {4, 4}, {5, 6}, {6, 8}, {7, 7}, {8, 9}, {9, 3}, {20, 16}, {18, 18}, {19, 20}, {22, 17}, {24, 22}, {26, 23}, {27, 21}, {30, 15}};
    //point points[]={{2, 14}, {3, 17}, {5, 21}, {7, 13}, {9, 16}, {10, 20}, {3, 6}, {4, 4}, {5, 6}, {6, 8}, {7, 7}, {8, 9}, {9, 3}, {20, 16}, {18, 18}, {19, 20}, {22, 17}, {24, 22}, {27, 21}, {30, 15}};
    //point points[]={{2, 14}, {3, 17}, {5, 21}, {7, 13}, {9, 16}, {10, 20}, {3, 6}, {5, 6}, {6, 8}, {7, 7}, {8, 9}, {9, 3}, {20, 16}, {18, 18}, {19, 20}, {22, 17}, {24, 22}, {30, 15}};
    //point points[]={{2, 14}, {3, 17}, {5, 21}, {7, 13}, {9, 16}, {10, 20}, {5, 6}, {6, 8}, {7, 7}, {8, 9}, {9, 3}, {20, 16}, {18, 18}, {19, 20}, {22, 17}, {24, 22}};
    //point points[]={{2, 14}, {3, 17}, {5, 21}, {7, 13}, {9, 16}, {10, 20}, {6, 8}, {7, 7}, {8, 9}, {9, 3}, {20, 16}, {18, 18}, {19, 20}, {22, 17}};
    //point points[]={{3, 17}, {5, 21}, {7, 13}, {9, 16}, {10, 20}, {6, 8}, {7, 7}, {8, 9}, {9, 3}, {20, 16}, {18, 18}, {19, 20}};
    //point points[]={{3, 17}, {5, 21}, {7, 13}, {9, 16}, {10, 20}, {6, 8}, {7, 7}, {8, 9}, {20, 16}, {18, 18}};
    //point points[]={{5, 21}, {7, 13}, {9, 16}, {10, 20}, {6, 8}, {7, 7}, {8, 9}, {18, 18}};
    //point points[]={{5, 21}, {7, 13}, {9, 16}, {10, 20}, {7, 7}, {8, 9}};
    //point points[]={{7, 13}, {9, 16}, {10, 20}, {8, 9}};
    //point points[]={{7, 13}, {9, 16}};



    /*point cluster1[] = {{2, 4}, {4, 4}, {3, 6}, {5, 6}, {2, 14}, {9, 3}, {3, 17}, {6, 8}, {7, 7}, {8, 9}, {7, 13}};
    point cluster2[] = {{26, 23}, {27, 21}, {30, 15}, {24, 22}, {22, 17}, {19, 20}, {20, 16}, {18, 18}, {5, 21}, {10, 20}, {9, 16}};



    point new_cluster1[] = {{2, 4}, {4, 4}, {3, 6}, {5, 6}, {2, 14}, {9, 3}, {3, 17}, {6, 8}, {7, 7}, {8, 9}, {7, 13}};
    point new_cluster2[] = {{26, 23}, {27, 21}, {30, 15}, {24, 22}, {22, 17}, {19, 20}, {20, 16}, {18, 18}};

    point another_new_cluster1[] = {{2, 4}, {4, 4}, {3, 6}, {5, 6}, {2, 14}, {9, 3}, {3, 17}, {6, 8}, {7, 7}, {8, 9}, {7, 13}, {5, 21}, {10, 20}, {9, 16}};
    point another_new_cluster2[] = {{26, 23}, {27, 21}, {30, 15}, {24, 22}, {22, 17}, {19, 20}, {20, 16}, {18, 18}, {5, 21}, {10, 20}, {9, 16}};*/
    /***-----------------------------------------------whole point set end----------------------------------------------*/







    /***-------------------------------------------------first cluster----------------------------------------------------*/
    //point points[]={{2, 4}, {4, 4}, {3, 6}, {5, 6}, {2, 14}, {9, 3}, {3, 17}, {6, 8}, {7, 7}, {8, 9}, {7, 13}, {5, 21}, {10, 20}, {9, 16}};
    //point points[]={{2, 4}, {4, 4}, {3, 6}, {5, 6}, {2, 14}, {3, 17}, {6, 8}, {7, 7}, {8, 9}, {7, 13}, {10, 20}, {9, 16}};
    //point points[]={{4, 4}, {3, 6}, {5, 6}, {2, 14}, {3, 17}, {6, 8}, {7, 7}, {8, 9}, {7, 13}, {9, 16}};
    //point points[]={{3, 6}, {5, 6}, {2, 14}, {6, 8}, {7, 7}, {8, 9}, {7, 13}, {9, 16}};
    //point points[]={{5, 6}, {2, 14}, {6, 8}, {7, 7}, {8, 9}, {7, 13}};
    //point points[]={{5, 6}, {6, 8}, {8, 9}, {7, 13}};
    //point points[]={{6, 8}, {8, 9}};



    /*point cluster1[] = {{9, 3}, {2, 4}, {4, 4}, {3, 6}, {7, 7}, {5, 6}, {6, 8}};
    point cluster2[] = {{5, 21}, {10, 20}, {3, 17}, {9, 16}, {2, 14}, {7, 13}, {8, 9}};

    point new_cluster1[] = {{9, 3}, {2, 4}, {4, 4}, {3, 6}, {7, 7}, {5, 6}};
    point new_cluster2[] = {{5, 21}, {10, 20}, {3, 17}, {9, 16}, {2, 14}};

    point another_new_cluster1[] = {{9, 3}, {2, 4}, {4, 4}, {3, 6}, {7, 7}, {5, 6}, {6, 8}, {7, 13}, {8, 9}};
    point another_new_cluster2[] = {{5, 21}, {10, 20}, {3, 17}, {9, 16}, {2, 14}, {7, 13}, {8, 9}, {6, 8}};*/

    /***--------------------------------------------first cluster end--------------------------------------------------*/
    /***-----------------------------------------------case 1 end----------------------------------------------------*/

    /***----------------------------------------------------case 2 circle-------------------------------------------------*/
    //point points[]={{0, 5}, {0, -5}, {5, 0}, {-5, 0}, {(5 * cos(45 * pi / 180)), (5 * sin(45 * pi / 180))}, {(5 * cos(135 * pi / 180)), (5 * sin(135 * pi / 180))}, {(5 * cos((-1) * 45 * pi / 180)), (5 * sin((-1) * 45 * pi / 180))}, {(5 * cos((-1) * 135 * pi / 180)), (5 * sin((-1) * 135 * pi / 180))}};
    //point points[]={{5, 0}, {-5, 0}, {(5 * cos(45 * pi / 180)), (5 * sin(45 * pi / 180))}, {(5 * cos(135 * pi / 180)), (5 * sin(135 * pi / 180))}, {(5 * cos((-1) * 45 * pi / 180)), (5 * sin((-1) * 45 * pi / 180))}, {(5 * cos((-1) * 135 * pi / 180)), (5 * sin((-1) * 135 * pi / 180))}};
    //point points[]={{(5 * cos(45 * pi / 180)), (5 * sin(45 * pi / 180))}, {(5 * cos(135 * pi / 180)), (5 * sin(135 * pi / 180))}, {(5 * cos((-1) * 45 * pi / 180)), (5 * sin((-1) * 45 * pi / 180))}, {(5 * cos((-1) * 135 * pi / 180)), (5 * sin((-1) * 135 * pi / 180))}};
    //point points[]={{(5 * cos(135 * pi / 180)), (5 * sin(135 * pi / 180))}, {(5 * cos((-1) * 45 * pi / 180)), (5 * sin((-1) * 45 * pi / 180))}};

    point cluster1[] = {{0, 5}, {5, 0}, {(5 * cos(45 * pi / 180)), (5 * sin(45 * pi / 180))}, {(5 * cos((-1) * 45 * pi / 180)), (5 * sin((-1) * 45 * pi / 180))}};
    point cluster2[] = {{0, -5}, {-5, 0}, {(5 * cos(135 * pi / 180)), (5 * sin(135 * pi / 180))}, {(5 * cos((-1) * 135 * pi / 180)), (5 * sin((-1) * 135 * pi / 180))}};



    /***--------------------------------------------------case 2 circle end------------------------------------------------*/






    int n = 4;
    /*point cent = centroid(points, n);
    cout << "centroid: " << cent.x << " " << cent.y << "\n";
    cout << "radius: " << radius(points, n) << "\n";
    cout << "diameter: " << diameter(points, n) << "\n";
    endPoint diamEndPoints = diameterPoints(points, n);
    cout << "diameter points: " << "(" << diamEndPoints.a.x << ", " << diamEndPoints.a.y << ") " << "(" << diamEndPoints.b.x << ", " << diamEndPoints.b.y << ")";*/
    //cout << pointDistance(cent, testPoint1);
    //cout << pointDistance(testPoint1, testPoint2);

    point cent1 = centroid(cluster1, n);
    point cent2 = centroid(cluster2, n);
    cout << "centroid of cluster 1: " << cent1.x << " " << cent1.y << "\n";
    cout << "centroid of cluster 2: " << cent2.x << " " << cent2.y << "\n";

    point totalCentroid;
    totalCentroid.x = (cent1.x + cent2.x) / 2;
    totalCentroid.y = (cent1.y + cent2.y) / 2;
    cout << "centroid of both clusters: " << totalCentroid.x << " " << totalCentroid.y << "\n";

    double distCentroid, distMidCentroid;
    cout << "closer points to mid centroid: \n";
    for(int i=0; i<n; i++)
    {
        distCentroid = pointDistance(cluster1[i], cent1);
        distMidCentroid = pointDistance(cluster1[i], totalCentroid);

        if(distMidCentroid < distCentroid)
        {
            cout << "(" << cluster1[i].x << ", " << cluster1[i].y << ")\n";
        }

        distCentroid = pointDistance(cluster2[i], cent2);
        distMidCentroid = pointDistance(cluster2[i], totalCentroid);

        if(distMidCentroid < distCentroid)
        {
            cout << "(" << cluster2[i].x << ", " << cluster2[i].y << ")\n";
        }
    }

    //cout << pointDistance(totalCentroid, testPoint1) << "\n" <<pointDistance(cent1, testPoint1);



    //cout << diameter(cluster1, n) / n << "\n" << diameter(cluster2, n) / n << "\n";
    //cout << diameter(new_cluster1, 6) / 6 << "\n" << diameter(new_cluster2, 5) / 5 << "\n";
    //cout << diameter(another_new_cluster1, 9) / 9 << "\n" << diameter(another_new_cluster2, 8) / 8 << "\n";

    //cout << 5 * cos(45) << " " << 5 * cos(45 * pi / 180) << "\n";
    //cout << 5 * sin(45) << " " << 5 * sin(45 * pi / 180) << "\n";

    return 0;
}
