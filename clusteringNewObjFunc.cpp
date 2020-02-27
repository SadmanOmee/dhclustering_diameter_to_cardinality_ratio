#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

#define pi 3.1416
#define k 2
#define vp vector<point>
#define mode 1

double horizontalVariance = 0.0, verticalVariance = 0.0;

struct point
{
    double x, y;
};

struct diameter
{
    double diam;
    point a, b;
    ll it_a, it_b;
};

struct cluster
{
    vp cl1, cl2;
};

/** distance measure functions implementation*/
double euclideanDistance(point a, point b)
{
    return sqrt(((a.x - b.x) * (a.x - b.x)) + ((a.y - b.y) * (a.y - b.y)));
}

double manhattanDistance(point a, point b)
{
    return (abs(a.x - b.x) + abs(a.y - b.y));
}

double minkowskiDistance(point a, point b)
{
    double sum = 0, r = 10.0;
    sum += pow(a.x - b.x, r);
    sum += pow(a.y - b.y, r);
    return pow(sum, 1.0 / r);
}

double chebychevDistance(point a, point b)
{
    return max(abs(a.x - b.x), abs(a.y - b.y));
}

double cosineDistance(point a, point b)
{
    double cosineSimilarity = ((a.x * b.x) + (a.y * b.y)) / (sqrt((a.x * a.x) + (a.y * a.y)) * sqrt((b.x * b.x) + (b.y * b.y)));
    return (1 - cosineSimilarity);
}

double mahalanobisDistance(point a, point b)
{
    string distribution = "normal";
    double x_bar, y_bar, var_x, var_y, covar_xy, dist;
    if(distribution == "normal")
    {
        x_bar = (a.x + b.x) / 2;
        y_bar = (a.y + b.y) / 2;
        var_x = (a.x - x_bar) * (a.x - x_bar) + (a.y - y_bar) * (a.y - y_bar);
        var_y = (b.x - x_bar) * (b.x - x_bar) + (b.y - y_bar) * (b.y - y_bar);
        covar_xy = ((a.x - x_bar) * (a.y - y_bar) + (b.x - x_bar) * (b.y - y_bar)) / 2;

        double ad_bc = var_x * var_y - covar_xy * covar_xy;
        double d = var_y / ad_bc;
        double p = var_x / ad_bc;
        double q = (-1) * covar_xy / ad_bc;
        double c = q;   /** [ d -q
                             -c  p]*/
        point meanPoint;
        meanPoint.x = x_bar;
        meanPoint.y = y_bar;
        double row1 = manhattanDistance(a, meanPoint) * d + manhattanDistance(b, meanPoint) * c;
        double row2 = manhattanDistance(a, meanPoint) * q + manhattanDistance(b, meanPoint) * p;

        dist = sqrt((row1 * row1) + (row2 * row2));
    }
    return dist;
}

double pointDistance(point a, point b)
{
    return euclideanDistance(a, b);
}
/** distance measure functions implementation end*/

point centroid(vp points)
{
    point centre;
    centre.x = 0;
    centre.y = 0;
    for(auto i=points.begin(); i<points.end(); ++i)
    {
        point Point = *i;
        centre.x += Point.x;
        centre.y += Point.y;
    }
    centre.x /= points.size();
    centre.y /= points.size();
    //cout << centre.x << " " << centre.y << "\n";
    return centre;
}

double radius(vp points)
{
    point centre = centroid(points);
    double rad = 0.0, pointDist;
    for(auto i=points.begin(); i<points.end(); ++i)
    {
        point Point = *i;
        pointDist = pointDistance(centre, Point);
        if(pointDist > rad)
        {
            rad = pointDist;
        }
    }
    return rad;
}

/*double diameter(vector<point> points)
{
    double diam = 0.0, pointDist;
    for(auto i=points.begin(); i<points.end(); ++i)
    {
        point PointA = *i;
        for(auto j=points.begin(); j<points.end(); ++j)
        {
            point PointB = *j;
            pointDist = pointDistance(PointA, PointB);
            if(pointDist > diam)
            {
                diam = pointDist;
            }
        }
    }
    return diam;
}*/

diameter findDiameter(vp points)
{
    double diam = 0.0, pointDist;
    ll itA = -1;
    diameter diameterDetails;
    for(auto i=points.begin(); i<points.end(); ++i)
    {
        point PointA = *i;
        itA++;
        ll itB = -1;
        for(auto j=points.begin(); j<points.end(); ++j)
        {
            point PointB = *j;
            itB++;
            pointDist = pointDistance(PointA, PointB);
            //cout << PointA.x << " " << PointA.y << " | " << PointB.x << " " << PointB.y << "\n";
            if(pointDist > diam)
            {
                diam = pointDist;
                diameterDetails.diam = diam;
                diameterDetails.a = PointA;
                diameterDetails.b = PointB;
                diameterDetails.it_a = itA;
                diameterDetails.it_b = itB;
            }
        }
    }
    return diameterDetails;
}

ll nearestNeighbour(vp points, point pnt)
{
    ll ind = -1;
    ll minDist = 9999999999999, minIndex;
    for(auto i=points.begin(); i<points.end(); ++i)
    {
        ind++;
        point Point = *i;
        if(pointDistance(Point, pnt) < minDist)
        {
            minDist = pointDistance(Point, pnt);
            minIndex = ind;
        }
    }
    return minIndex;
}

/*void removeVec(vector<point> &points, ll pos)
{
    vector<point>::iterator it1 = points.begin();
    it1 += pos;
    points.erase(it1);
}*/

double intraClusterDistance(vp clust)
{
    point clusterCenter = centroid(clust);
    double intraClustDist = 0.0;
    for(auto i=clust.begin(); i<clust.end(); ++i)
    {
        point Point = *i;
        intraClustDist += pointDistance(clusterCenter, Point);
    }
    return intraClustDist;
}

double avgIntraClusterDistance(vp &clust)
{
    double avgIntraClustDist = intraClusterDistance(clust) / clust.size();
    //clust.clear();
    return avgIntraClustDist;
}

double calculateRatio(vp &clust)
{
    diameter d = findDiameter(clust);
    double ratio_d_nd = d.diam / clust.size();
    //clust.clear();
    return ratio_d_nd;
}

double calculateRatioRadius(vp &clust)
{
    double ratio_d_nd = radius(clust) / clust.size();
    //clust.clear();
    return ratio_d_nd;
}

cluster clustering(vp &points)
{
    cluster clust;
    vp cluster1, cluster2, tempCluster;
    point centroidPointSet, centroidCluster1, centroidCluster2;

    centroidPointSet = centroid(points);
    //cout << "Centroid of whole point set: " << centroidPointSet.x << " " << centroidPointSet.y << "\n";
    diameter d = findDiameter(points);
    cluster1.push_back(d.a);
    cluster2.push_back(d.b);
    if(d.it_a < d.it_b)
    {
        points.erase(points.begin() + d.it_a);
        points.erase(points.begin() + d.it_b - 1);
    }
    else
    {
        points.erase(points.begin() + d.it_b);
        points.erase(points.begin() + d.it_a - 1);
    }

    while(!points.empty())
    {
        if(mode == 1)
        {
            /***----n * nlogn solution-----*/
            d = findDiameter(points);
            if(pointDistance(d.a, centroid(cluster1)) <= pointDistance(d.b, centroid(cluster1)))
            {
                cluster1.push_back(d.a);
                cluster2.push_back(d.b);
            }
            else
            {
                cluster1.push_back(d.b);
                cluster2.push_back(d.a);
            }
            if(d.it_a < d.it_b)
            {
                points.erase(points.begin() + d.it_a);
                points.erase(points.begin() + d.it_b - 1);
            }
            else
            {
                points.erase(points.begin() + d.it_b);
                points.erase(points.begin() + d.it_a - 1);
            }
            /***----n * nlogn solution end-----*/
        }
        else if(mode == 2)
        {
            /***----nlogn solution-----*/
            auto head = points.begin();
            point pnt = *head;
            if(pointDistance(pnt, centroid(cluster1)) <= pointDistance(pnt, centroid(cluster1)))
            {
                cluster1.push_back(pnt);
            }
            else
            {
                cluster2.push_back(pnt);
            }
            points.erase(points.begin());
            /***----nlogn solution end-----*/
        }
        else
        {
            //centroidCluster1 = cluster1.back();
            //centroidCluster2 = cluster2.back();
            centroidCluster1 = centroid(cluster1);
            centroidCluster2 = centroid(cluster2);

            ll nn;
            nn = nearestNeighbour(points, centroidCluster1);
            cluster1.push_back(points[nn]);
            points.erase(points.begin() + nn);

            nn = nearestNeighbour(points, centroidCluster2);
            cluster2.push_back(points[nn]);
            points.erase(points.begin() + nn);
        }
    }

    cout << "Initial points of cluster 1:\n-----------------------------\n";
    for(auto i=cluster1.begin(); i<cluster1.end(); ++i)
    {
        point Point = *i;
        cout << "(" << Point.x << ", " << Point.y << ") ";
    }
    cout << "\n\n";

    cout << "Initial points of cluster 2:\n-----------------------------\n";
    for(auto i=cluster2.begin(); i<cluster2.end(); ++i)
    {
        point Point = *i;
        cout << "(" << Point.x << ", " << Point.y << ") ";
    }
    cout << "\n\n";

    centroidCluster1 = centroid(cluster1);
    centroidCluster2 = centroid(cluster2);

    cout << "Centroid of cluster 1: " << centroidCluster1.x << " " << centroidCluster1.y << "\n";
    cout << "Centroid of cluster 2: " << centroidCluster2.x << " " << centroidCluster2.y << "\n";

    /*//double avgClust1Dist = avgIntraClusterDistance(cluster1);
    //double avgClust2Dist = avgIntraClusterDistance(cluster2);
    //double avgClust1Dist = findDiameter(cluster1).diam;
    //double avgClust2Dist = findDiameter(cluster2).diam;
    double avgDistRatio;
    if(avgClust1Dist < avgClust2Dist)
    {
        avgDistRatio = avgClust2Dist / avgClust1Dist;
    }
    else
    {
        avgDistRatio = avgClust1Dist / avgClust2Dist;
    }
    centroidPointSet.x *= avgDistRatio;
    centroidPointSet.y *= avgDistRatio;*/

    cout << "Centroid of whole point set: " << centroidPointSet.x << " " << centroidPointSet.y << "\n";

    cout << "Points of temp cluster:\n-----------------------\n";
    for(auto i=cluster1.begin(); i<cluster1.end(); ++i)
    {
        point Point = *i;
        if(pointDistance(Point, centroidPointSet) < pointDistance(Point, centroidCluster1))
        {
            tempCluster.push_back(Point);
            cluster1.erase(i);
            i--;
            cout << "(" << Point.x << ", " << Point.y << ") ";
        }
    }

    for(auto i=cluster2.begin(); i<cluster2.end(); ++i)
    {
        point Point = *i;
        if(pointDistance(Point, centroidPointSet) < pointDistance(Point, centroidCluster2))
        {
            tempCluster.push_back(Point);
            cluster2.erase(i);
            i--;
            cout << "(" << Point.x << ", " << Point.y << ") ";
        }
    }
    cout << "\n\n";

    double ratio_d1_nd1, ratio_d2_nd2;
    vp copyCluster1, copyCluster2;
    copyCluster1.insert(copyCluster1.end(), cluster1.begin(), cluster1.end());
    copyCluster1.insert(copyCluster1.end(), tempCluster.begin(), tempCluster.end());
    copyCluster2.insert(copyCluster2.end(), cluster2.begin(), cluster2.end());
    copyCluster2.insert(copyCluster2.end(), tempCluster.begin(), tempCluster.end());

    //ratio_d1_nd1 = calculateRatio(copyCluster1);
    //ratio_d2_nd2 = calculateRatio(copyCluster2);

    //ratio_d1_nd1 = calculateRatioRadius(copyCluster1);
    //ratio_d2_nd2 = calculateRatioRadius(copyCluster2);

    //ratio_d1_nd1 = avgIntraClusterDistance(copyCluster1);
    //ratio_d2_nd2 = avgIntraClusterDistance(copyCluster2);

    //ratio_d1_nd1 = calculateRatio(copyCluster1) + findDiameter(copyCluster1).diam;
    //ratio_d2_nd2 = calculateRatio(copyCluster2) + findDiameter(copyCluster2).diam;

    //ratio_d1_nd1 = avgIntraClusterDistance(copyCluster1) + calculateRatio(copyCluster1);
    //ratio_d2_nd2 = avgIntraClusterDistance(copyCluster2) + calculateRatio(copyCluster2);

    //ratio_d1_nd1 = (2 * avgIntraClusterDistance(copyCluster1) / copyCluster1.size()) + calculateRatioRadius(copyCluster1);
    //ratio_d2_nd2 = (2 * avgIntraClusterDistance(copyCluster2) / copyCluster2.size()) + calculateRatioRadius(copyCluster2);

    //ratio_d1_nd1 = avgIntraClusterDistance(copyCluster1) + calculateRatioRadius(copyCluster1);
    //ratio_d2_nd2 = avgIntraClusterDistance(copyCluster2) + calculateRatioRadius(copyCluster2);

    //ratio_d1_nd1 = min(avgIntraClusterDistance(copyCluster1), calculateRatio(copyCluster1));
    //ratio_d2_nd2 = min(avgIntraClusterDistance(copyCluster2), calculateRatio(copyCluster2));

    ratio_d1_nd1 = calculateRatio(copyCluster1) + calculateRatio(cluster2);
    ratio_d2_nd2 = calculateRatio(copyCluster2) + calculateRatio(cluster1);

    //ratio_d1_nd1 = calculateRatio(copyCluster1) + calculateRatio(cluster2) + pointDistance(centroid(copyCluster1), centroid(cluster2)) / (copyCluster1.size() + cluster2.size());
    //ratio_d2_nd2 = calculateRatio(copyCluster2) + calculateRatio(cluster1) + pointDistance(centroid(copyCluster2), centroid(cluster1)) / (copyCluster2.size() + cluster1.size());

    //ratio_d1_nd1 = calculateRatioRadius(copyCluster1) + calculateRatioRadius(cluster2);
    //ratio_d2_nd2 = calculateRatioRadius(copyCluster2) + calculateRatioRadius(cluster1);

    //ratio_d1_nd1 = avgIntraClusterDistance(copyCluster1) + avgIntraClusterDistance(cluster2);
    //ratio_d2_nd2 = avgIntraClusterDistance(copyCluster2) + avgIntraClusterDistance(cluster1);

    //ratio_d1_nd1 = 2 * avgIntraClusterDistance(copyCluster1) / copyCluster1.size() + 2 * avgIntraClusterDistance(cluster2) / cluster2.size();
    //ratio_d2_nd2 = 2 * avgIntraClusterDistance(copyCluster2) / copyCluster2.size() + 2 * avgIntraClusterDistance(cluster1) / cluster1.size();

    cout << "---------********------------------\n";
    cout << avgIntraClusterDistance(copyCluster1) << " " << calculateRatioRadius(copyCluster1) << " " << calculateRatio(copyCluster1) << "\n";
    cout << avgIntraClusterDistance(copyCluster2) << " " << calculateRatioRadius(copyCluster2) << " " << calculateRatio(copyCluster2)  << "\n";

    cout << avgIntraClusterDistance(copyCluster1) - avgIntraClusterDistance(copyCluster2) << "\n";
    cout << calculateRatioRadius(copyCluster1) - calculateRatioRadius(copyCluster2) << "\n";
    cout << calculateRatio(copyCluster1) - calculateRatio(copyCluster2) << "\n";
    cout << "---------********------------------\n";

    //ratio_d1_nd1 *= (double)((double)copyCluster1.size() / (double)(copyCluster1.size() + copyCluster2.size()));
    //ratio_d2_nd2 *= (double)((double)copyCluster2.size() / (double)(copyCluster1.size() + copyCluster2.size()));
    //ratio_d1_nd1 += calculateRatioRadius(copyCluster1);
    //ratio_d2_nd2 += calculateRatioRadius(copyCluster2);

    cout << "ratios: " << ratio_d1_nd1 << " " << ratio_d2_nd2 << "\n\n";

    if(ratio_d1_nd1 <= ratio_d2_nd2)
    {
        cluster1.insert(cluster1.end(), tempCluster.begin(), tempCluster.end());
    }
    else
    {
        cluster2.insert(cluster2.end(), tempCluster.begin(), tempCluster.end());
    }
    tempCluster.clear();

    centroidCluster1 = centroid(cluster1);
    centroidCluster2 = centroid(cluster2);
    cout << "New centroid of cluster 1: " << centroidCluster1.x << " " << centroidCluster1.y << "\n";
    cout << "New centroid of cluster 2: " << centroidCluster2.x << " " << centroidCluster2.y << "\n";

    for(auto i=cluster1.begin(); i<cluster1.end(); ++i)
    {
        point Point = *i;
        if(pointDistance(Point, centroidCluster1) > pointDistance(Point, centroidCluster2))
        {
            tempCluster.push_back(Point);
            cluster1.erase(i);
            i--;
            cout << "a";
        }
    }
    cluster2.insert(cluster2.end(), tempCluster.begin(), tempCluster.end());
    tempCluster.clear();

    for(auto i=cluster2.begin(); i<cluster2.end(); ++i)
    {
        point Point = *i;
        if(pointDistance(Point, centroidCluster2) > pointDistance(Point, centroidCluster1))
        {
            tempCluster.push_back(Point);
            cluster2.erase(i);
            i--;
            cout << "b";
        }
    }
    cluster1.insert(cluster1.end(), tempCluster.begin(), tempCluster.end());
    tempCluster.clear();
    cout << "\n\n";

    clust.cl1 = cluster1;
    clust.cl2 = cluster2;

    /**calculation of sum squared error*/
    double sse = 0.0;
    centroidCluster1 = centroid(cluster1);
    centroidCluster2 = centroid(cluster2);

    for(auto i=cluster1.begin(); i<cluster1.end(); ++i)
    {
        point Point = *i;
        double distFromCentroid = pointDistance(Point, centroidCluster1);
        distFromCentroid *= distFromCentroid;
        sse += distFromCentroid;
    }

    for(auto i=cluster2.begin(); i<cluster2.end(); ++i)
    {
        point Point = *i;
        double distFromCentroid = pointDistance(Point, centroidCluster2);
        distFromCentroid *= distFromCentroid;
        sse += distFromCentroid;
    }
    cout << "Sum squared error: " << setprecision(20) << sse << "\n"; //kmeans
    /**calculation of sum squared error end*/

    double dc1 = findDiameter(cluster1).diam, dc2 = findDiameter(cluster2).diam;
    double rc1 = radius(cluster1), rc2 = radius(cluster2);
    double avgICD1 = avgIntraClusterDistance(cluster1), avgICD2 = avgIntraClusterDistance(cluster2);
    double DbyNdRatio1 = dc1 / cluster1.size(), DbyNdRatio2 = dc2 / cluster2.size();
    double RbyNrRatio1 = rc1 / cluster1.size(), RbyNrRatio2 = rc2 / cluster2.size();

    cout << "diameters: " << dc1 << " " << dc2 << "\n";
    cout << "sum of diameters: " << dc1 + dc2 << "\n";
    cout << "average diameter: " << (dc1 + dc2) / 2 << "\n";
    cout << "radii: " << rc1 << " " << rc2 << "\n";
    cout << "sum of radii: " << rc1 + rc2 << "\n";
    cout << "average radius: " << (rc1 + rc2) / 2 << "\n";
    cout << "intra-cluster distances: " << intraClusterDistance(cluster1) << " " << intraClusterDistance(cluster2) << "\n"; //kmeans
    cout << "average intra-cluster distances: " << avgICD1 << " " << avgICD2 << "\n"; //kmeans
    cout << "sum of average intra-cluster distances: " << avgICD1 + avgICD2 << "\n"; //kmeans

    /**new measures*/
    cout << "d by nd ratio: " << DbyNdRatio1 << " " << DbyNdRatio2 << "\n";
    cout << "sum of d by nd ratios: " << DbyNdRatio1 + DbyNdRatio2 << "\n";
    cout << "r by nr ratio: " << RbyNrRatio1 << " " << RbyNrRatio2 << "\n";
    cout << "sum of r by nr ratios: " << RbyNrRatio1 + RbyNrRatio2 << "\n";
    cout << "centroid distances: " << pointDistance(centroidCluster1, centroidCluster2) << "\n";
    /**new measures end*/

    return clust;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ifstream input;
    ofstream output, cluster1Points, cluster2Points;
    input.open("input1.txt");
    output.open("output.txt");
    cluster1Points.open("cluster1Points.txt");
    cluster2Points.open("cluster2Points.txt");

    ll n;
    double horr_bar = 0.0, ver_bar = 0.0;
    //cin >> n;
    input >> n;
    vp pointSet, copyPointSet;
    for(ll i=0; i<n; i++)
    {
        point Point;
        //cin >> Point.x >> Point.y;
        input >> Point.x >> Point.y;
        pointSet.push_back(Point);
        copyPointSet.push_back(Point);
        horr_bar += Point.x;
        ver_bar += Point.y;
    }
    cout << "Data reading finished...\n\n";

    horr_bar /= n;
    ver_bar /= n;

    for(ll i=0; i<n; i++)
    {
        point Point;
        horizontalVariance += (abs(Point.x - horr_bar) * abs(Point.x - horr_bar));
        verticalVariance += (abs(Point.y - ver_bar) * abs(Point.y - ver_bar));
    }

    horizontalVariance /= n;
    verticalVariance /= n;

    //cout << "The point set: (" << pointSet.size() << " points)\n-----------------\n";
    output << "The point set: (" << pointSet.size() << " points)\n-----------------\n";
    for(auto i=pointSet.begin(); i<pointSet.end(); ++i)
    {
        point Point = *i;
        //cout << "(" << Point.x << ", " << Point.y << ") ";
        output << "(" << Point.x << ", " << Point.y << ") ";
    }
    //cout << "\n\n";
    output << "\n\n";

    cluster clusters = clustering(pointSet);

    horizontalVariance = 0.0;
    verticalVariance = 0.0;

    //cout << "Final points of cluster 1: (" << clusters.cl1.size() << " points)\n-------------------------------------\n";
    output << "Final points of cluster 1: (" << clusters.cl1.size() << " points)\n-------------------------------------\n";
    cluster1Points << clusters.cl1.size() << "\n";
    for(auto i=clusters.cl1.begin(); i<clusters.cl1.end(); ++i)
    {
        point Point = *i;
        //cout << "(" << Point.x << ", " << Point.y << ") ";
        output << "(" << Point.x << ", " << Point.y << ") ";
        cluster1Points << Point.x << " " << Point.y << "\n";
    }
    //cout << "\n\n";
    output << "\n\n";

    //cout << "Final points of cluster 2: (" << clusters.cl2.size() << " points)\n-------------------------------------\n";
    output << "Final points of cluster 2: (" << clusters.cl2.size() << " points)\n-------------------------------------\n";
    cluster2Points << clusters.cl2.size() << "\n";
    for(auto i=clusters.cl2.begin(); i<clusters.cl2.end(); ++i)
    {
        point Point = *i;
        //cout << "(" << Point.x << ", " << Point.y << ") ";
        output << "(" << Point.x << ", " << Point.y << ") ";
        cluster2Points << Point.x << " " << Point.y << "\n";
    }
    //cout << "\n\n";
    output << "\n\n";

    //cout << "Remaining points of point set:\n--------------------------------\n";
    output << "Remaining points of point set:\n--------------------------------\n";
    for(auto i=pointSet.begin(); i<pointSet.end(); ++i)
    {
        point Point = *i;
        //cout << "(" << Point.x << ", " << Point.y << ") ";
        output << "(" << Point.x << ", " << Point.y << ") ";
    }
    //cout << "\n\n";
    output << "\n\n";

    input.close();
    output.close();
    cluster1Points.close();
    cluster1Points.close();

    return 0;
}






/*
22
2 14
3 17
5 21
7 13
9 16
10 20
2 4
3 6
4 4
5 6
6 8
7 7
8 9
9 3
20 16
18 18
19 20
22 17
24 22
26 23
27 21
30 15

















14
2 14
3 17
5 21
7 13
9 16
10 20
2 4
3 6
4 4
5 6
6 8
7 7
8 9
9 3
*/
