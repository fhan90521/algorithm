#include <iostream>
#include <vector>
#include <algorithm>
#include<fstream>
#include<string>

using namespace std;

int main()
{
    ifstream in("ballpark.inp");
    ofstream out("ballpark.out");

    int n,m;

    in>>n>>m;
    string input;
    int land[n][m];
    for(int i=0;i<n;i++){
        in>>input;
        for(int j=0;j<m;j++){
            if(input[j]=='0'){
                land[i][j]=1;
            }
            else{
                land[i][j]=0;
            }
        }
    }


    int longest=0;
    for(int i=1;i<n;i++)
    {
        for(int j=1;j<m;j++)
        {
            if(land[i][j]==1){
                land[i][j] = 1 + min({land[i-1][j-1],land[i-1][j],land[i][j-1]});
                longest = max(longest,land[i][j]);
            }
        }
    }
    int counts=0;
    vector<pair<int,int>> answer;

    for(int i=1;i<n;i++)
    {
        for(int j=1;j<m;j++)
        {
            if(land[i][j]==longest){
                counts+=1;
                answer.push_back(pair<int,int>(j-longest+2,n-i));
            }
        }
    }

    out<<longest<<' '<<counts<<endl;
    sort(answer.begin(),answer.end());
    for(int i=0;i<counts;i++){
        out<<answer[i].first<<' '<<answer[i].second<<endl;
    }
    in.close();
    out.close();

}
