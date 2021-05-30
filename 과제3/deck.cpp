#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){


    ifstream in("deck.inp");
    ofstream out("deck.out");


    int N;

    in >> N;

    int  num,totalSum=0,totalMulti=0;

    for(int i=1;i<N+1;i++){
        totalSum+=i;
        totalMulti+=i*i;
    }

    int counts=0;
    while(in >> num){
        counts+=1;
        totalSum-=num;
        totalMulti-=num*num;
    }

    if(counts==N-1){
        out<<totalSum<<"\n";
    }
    if(counts==N-2){

        int left=1;
        int right=totalSum-1;
        while(left<right){

            if((left*left)+(right*right)==totalMulti){
                out<<left<<"\n";
                out<<right<<"\n";
                break;
            }
            left+=1;
            right-=1;
        }
    }





    in.close();
    out.close();

    return 0;
}
