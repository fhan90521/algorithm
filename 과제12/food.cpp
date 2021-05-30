#include <bits/stdc++.h>
using namespace std;

int stac[51]={0,};
int stac_last=0;
int food_num;
int c[4];
int cstack[4]={0,};
int **food_list;
int answers[51];
int answers_last=0;
int total_cost=0;
int min_cost= INT_MAX;

bool cmp( int* p1, int* p2){
    if(p1[4] < p2[4]){
        return true;
    }
    else if(p1[4] == p2[4]){
        if(p1[6] > p2[6]){
            return true;
        }
        else if(p1[6] == p2[6]){
            if(p1[5]<p2[5]){
                return true;
            }
        }
    }
    return false;

}

bool check(){

    for(int i=0;i<4;i++){
        if(cstack[i]<c[i]){
            return false;
        }
    }
    return true;

}

int dfs(int current){
    for(int i=current;i<food_num;i++){
        cstack[0]+=food_list[i][0];
        cstack[1]+=food_list[i][1];
        cstack[2]+=food_list[i][2];
        cstack[3]+=food_list[i][3];
        total_cost+=food_list[i][4];
        stac[stac_last]=food_list[i][5];
        stac_last+=1;
        if(total_cost>=min_cost){
            cstack[0]-=food_list[i][0];
            cstack[1]-=food_list[i][1];
            cstack[2]-=food_list[i][2];
            cstack[3]-=food_list[i][3];
            total_cost-=food_list[i][4];
            stac_last-=1;
            stac[stac_last]=0;
            break;
        }
        else{
                if(check()){
                    min_cost=total_cost;
                    answers_last=stac_last;
                    for(int k=0;k<stac_last;k++){
                        answers[k]=stac[k];
                    }
                    cstack[0]-=food_list[i][0];
                    cstack[1]-=food_list[i][1];
                    cstack[2]-=food_list[i][2];
                    cstack[3]-=food_list[i][3];
                    total_cost-=food_list[i][4];
                    stac_last-=1;
                    stac[stac_last]=0;
                    break;
                }
                else{
                    dfs(i+1);
                    cstack[0]-=food_list[i][0];
                    cstack[1]-=food_list[i][1];
                    cstack[2]-=food_list[i][2];
                    cstack[3]-=food_list[i][3];
                    total_cost-=food_list[i][4];
                    stac_last-=1;
                    stac[stac_last]=0;
                }
        }




    }

}





int main(){


    ifstream in("food.inp");
    ofstream out("food.out");

    in >> food_num;
    in >> c[0] >> c[1] >> c[2] >> c[3];
    food_list=new int*[food_num];
    int a1,a2,a3,a4,cost;

    for(int i=0;i<food_num;i++){
        food_list[i] = new int[7];
        in >> a1 >> a2 >> a3 >> a4 >> cost;
        food_list[i][0]=a1;
        food_list[i][1]=a2;
        food_list[i][2]=a3;
        food_list[i][3]=a4;
        food_list[i][4]=cost;
        food_list[i][5]=i+1;
        food_list[i][6]=a1+a2+a3+a4;
    }

    stable_sort(food_list,food_list+food_num,cmp);

    int index;
    for(index=0;index<food_num;index++){
        if(food_list[index][4]!=0) break;
        cstack[0]+=food_list[index][0];
        cstack[1]+=food_list[index][1];
        cstack[2]+=food_list[index][2];
        cstack[3]+=food_list[index][3];
        total_cost+=food_list[index][4];
        stac[stac_last]=food_list[index][5];
        stac_last+=1;
    }




    if(check()){
        sort(stac,stac+stac_last);
        for(int i=0;i<stac_last;i++){
            out<<stac[i];
            out<<" ";
        }
    }
    else{
        dfs(index);
        if(answers[0]==0){
            out<< 0;
        }
        else{

            sort(answers,answers+answers_last);


            for(int i=0 ; i<answers_last ; i++){
                out<<answers[i];
                out<<" ";
            }
        }
    }



    in.close();
    out.close();






    return 0;
}
