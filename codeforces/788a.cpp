#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int main(){
    int t;
    cin >> t;
    while (t--){
        int n;
        cin >> n;
        int array[n];
        int count = 0;
        for(int i = 0; i <n;i++){
            cin >> array[i];
            if(array[i] < 0){
                count ++;

            }
            array[i] = abs(array[i]);
        }
        for(int i = 0; i < n; i++){
            if(count == 0){
                break;
            }
            count --;
            array[i] = -array[i];

        }
        int flag = 0;
        for(int i = 1;i<n;i++){
            if(array[i]<array[i-1]){
                flag = 1;
                break;
            }
        }
    
    if (flag){
        cout << "no\n";

    }
    else{
        cout << "yes"<<endl;
    }

    }
    return 0;

}