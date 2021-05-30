#include <bits/stdc++.h>


using namespace std;
int maxlen=0;
int maxvalue=0;
int vertexs[26]={0,};
vector<pair<int,int>> edges[26];
int stac[26];
int stac_last=1;
int **answers;
int answers_num=0;
int vertex_num,edge_num;
int predict;
bool flag;

int dfs(int current,int total){
    /*for(int i=0; i<26;i++){
        cout<<stac[i]<<" ";
    }
    cout<<endl;*/
    for(int i=0;i<edges[current].size();i++){
        if(vertexs[edges[current][i].first]!=0 && vertexs[edges[current][i].first]!=-1){
            stac[stac_last]=edges[current][i].first;
            stac_last+=1;
            total+=edges[current][i].second;
            vertexs[edges[current][i].first]=-1;

            predict=0;
            for(int m=0;m<26;m++){
                if(vertexs[m]==1){
                    for(int u=0;u<edges[m].size();u++){
                        if(vertexs[edges[m][u].first]!=-1 || edges[m][u].first==0 || edges[m][u].first == stac[stac_last-1]){
                            predict+=edges[m][u].second;
                            break;
                        }
                    }
                }
            }
            flag=false;
            for(int m=0;m<edges[0].size();m++){
                if(vertexs[edges[0][m].first]!=-1 || edges[0][m].first == stac[stac_last-1] ){
                    flag=true;
                    predict+=edges[0][m].second;
                }
            }
            if(predict+total>=maxvalue && flag){
                dfs(edges[current][i].first,total);
            }


            vertexs[edges[current][i].first]=1;
            total-=edges[current][i].second;
            stac_last-=1;
            stac[stac_last]=-1;
        }
        else{
            if(edges[current][i].first==0){
                if(total+edges[current][i].second>maxvalue){
                    maxvalue=total+edges[current][i].second;
                    maxlen=stac_last;
                    answers_num=0;
                    for(int k=0;k<26;k++){
                        answers[answers_num][k]=stac[k];
                    }
                    answers_num+=1;


                }
                else{
                    if(total+edges[current][i].second==maxvalue){
                        if(stac_last>maxlen){
                            maxlen=stac_last;
                            answers_num=0;
                            for(int k=0;k<26;k++){
                                answers[answers_num][k]=stac[k];
                            }
                            answers_num+=1;


                        }
                        else if(stac_last==maxlen){

                           for(int k=0;k<26;k++){
                                answers[answers_num][k]=stac[k];
                            }
                            answers_num+=1;

                        }
                    }
                }

            }

        }
    }

}

bool cmp( int* p1, int* p2){
    if(p1[2] > p2[2]){
        return true;
    }
    else{
        return false;
        }
    }
bool comp( int* p1, int* p2){
    for(int i=0;i<26;i++){
        if(p1[i] < p2[i]){
            return true;

        }
        else if(p1[i] == p2[i]){
            continue;
        }
        return false;
    }


}





int main(){


    ifstream in("iron.inp");
    ofstream out("iron.out");
    memset(stac,-1,sizeof(stac));

    /*for(int i=0;i<26;i++){
        cout<<stac[i]<<" ";
    }
    cout<<endl;*/



    in >> vertex_num >> edge_num;

    char left,right;
    int cost;
    int **edges_list=new int*[edge_num];
    answers=new int*[1000];
    for(int i=0;i<1000;i++){
        answers[i] = new int[26];

    }
    for(int i=0;i<edge_num;i++){
        edges_list[i] = new int[3];
        in>>left>>right>>cost;
        edges_list[i][0]=left-'a';
        edges_list[i][1]=right-'a';
        edges_list[i][2]=cost;
        vertexs[left-'a']=1;
        vertexs[right-'a']=1;
    }
    stable_sort(edges_list,edges_list+edge_num,cmp);

    for(int i=0; i<edge_num; i++){
            edges[edges_list[i][0]].push_back({edges_list[i][1],edges_list[i][2]});
            edges[edges_list[i][1]].push_back({edges_list[i][0],edges_list[i][2]});
    }
    /*for(int i=0; i<26; i++){
        for(int k=0; k<edges[i].size();k++){
            cout<<edges[i][k].first<<" ";
        }
        cout<<endl;
    }*/
    stac[0]=0;
    vertexs[0]=-1;
    int lastone=0;
    for(int i=0;i<edges[0].size();i++){
        if(lastone<edges[0][i].first){
            lastone=edges[0][i].first;
        }
    }
    for(int i=0;i<edges[0].size();i++){
        if(edges[0][i].first!=lastone){
            stac[stac_last]=edges[0][i].first;
            stac_last+=1;
            vertexs[edges[0][i].first]=-1;
            dfs(edges[0][i].first,edges[0][i].second);
            vertexs[edges[0][i].first]=1;
            stac_last-=1;
            stac[stac_last]=-1;
        }
    }


    /*cout<<maxvalue<<endl;
    for(int i=0;i<answers_num;i++){
        for(int j=0; j<26;j++){
        cout<<(char)(answers[i][j]+0x61)<<" ";
        }
        cout<<endl;

    }*/


    stable_sort(answers,answers+answers_num,comp);
    cout<<answers_num<<endl;
    for(int i=0;i<answers_num;i++){
        for(int j=0; j<26;j++){
        cout<<(char)(answers[i][j]+0x61)<<" ";
        }
        cout<<endl;

    }
    out<<maxvalue<<endl;
    for(int i=0;answers[0][i]!=-1;i++){
        out<<(char)(answers[0][i]+0x61)<<" ";
    }

    in.close();
    out.close();






    return 0;
}
