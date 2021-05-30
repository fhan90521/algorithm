#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main(){
    /**
     * Open file I/O stream
     */

    ifstream in("words.inp");
    ofstream out("words.out");

    // Number of input strings
    int N;

    // string to check whether it is palindrome or not
    string input_str;

    in >> N;
    map<string,int> m;

    for(int i=0; i<N; i++) {

        in >> input_str;
        m[input_str]+=1;


    }

    int counts=0;
    for(auto it = m.begin(); it !=m.end(); it++){
        if(it->second>=N/2+1){
            out << it-> first<< "\n";
            counts+=1;
        }
    }
    if(N>0 && counts==0){
        out << "NONE" << "\n";
    }

    /**
     *  Close file I/O stream
     */

    in.close();
    out.close();

    return 0;
}
