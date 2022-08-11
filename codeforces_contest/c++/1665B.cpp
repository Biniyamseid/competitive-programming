#include<iostream>
#include<bits/stdc++.h>
using namespace std;
#include<vector>
#include<math.h>
#include<numeric>
#include<stack>
#include<queue>
#include<string>
#include<algorithm>
#include<map>
#define mp make_pair
#define ins insert
#define lli long long int
#define ll long long
#define pb push_back
#define loop1(i,l,n) for(i=l;i<=n;i++)
#define loop0(i,l,n) for(i=l;i<n;i++)
#define inf (1<<28)
#define pi 3.1415926536
const int MAX=1e6+9;
set<int>ist;
map<string,int>msi;
map<string,string>mss;
map<int,string>mis;
map<int,int>mii;
pair<int,int>pii;
vector<int>v;
vector<pair<int,int> >vv;
int cc[]= {1,-1,0,0};
int rr[]= {0,0,1,-1};

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie();
    int t;
    cin >> t;
    while (t--){
        int n;
        cin >>n;
        int array[n];
        map<int,int>m;
        int maxi=0;
        for(int i=0;i<n;i++){
            cin >> array[i];
            m[array[i]]++;
            maxi = max(maxi,m[array[i]]);

        }
        for (int i = 0; i<6;i++){
            cout << m[array[i]]<< endl;
        }
        int ans = n - maxi;
        int count = maxi;
        while (count <n){
            ans ++;
            count += 2;
        }
        cout << ans<<"\n";
    }


    cout << "hello world";
    return 0;
}