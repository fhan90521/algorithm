#include <iostream>
#include <fstream>
#include <bits/stdc++.h>

using namespace std;

double dt=0.00001;
double distance(double (&point1)[3],double (&point2)[3]){
    double dis=0;
    for(int i=0;i<3;i++){
        dis+=(point1[i]-point2[i])*(point1[i]-point2[i]);
    }
    return dis;
}
double searchP(double left,double right,double (&a)[3],double (&b)[3],double (&p)[3],double (&q)[3],double Preresult){

    double t=(left+right)/2;


    double mid_left[3];
    double mid_right[3];
    double mid[3];
    double result=Preresult;
    cout<<result<<endl;


    for(int i=0;i<3;i++){
        mid[i]=(t)*a[i]+(1-(t))*b[i];
    }
    double mid_value=distance(q,mid);

    if(mid_value<result){
        result=mid_value;
        for(int i=0;i<3;i++){
            p[i]=mid[i];
     }
    }

    if(right-left<2*dt){
        return result;
    }


    for(int i=0;i<3;i++){
        mid_left[i]=(t-dt)*a[i]+(1-(t-dt))*b[i];
    }
    for(int i=0;i<3;i++){
        mid_right[i]=(t+dt)*a[i]+(1-(t+dt))*b[i];
    }
    double left_value=distance(q,mid_left);
    double right_value=distance(q,mid_right);

    if(mid_value<right_value&&mid_value<left_value){
        return result;
    }
    if(left_value<right_value){
        result=left_value;
        for(int i=0;i<3;i++){
            p[i]=mid_left[i];
     }
        result=searchP(left,t,a,b,p,q,result);
    }
    else{
        result=right_value;
        for(int i=0;i<3;i++){
            p[i]=mid_right[i];
     }
        result=searchP(t,right,a,b,p,q,result);
    }

}
double searchQ(double left,double right,double c[3],double d[3],double (&p)[3],double (&q)[3],double Preresult){

    double t=(left+right)/2;
    double mid_left[3];
    double mid_right[3];
    double mid[3];
    double result=Preresult;
    cout<<result<<endl;



    for(int i=0;i<3;i++){
        mid[i]=(t)*c[i]+(1-(t))*d[i];
    }

    double mid_value=distance(p,mid);





    if(mid_value<result){
        result=mid_value;
        for(int i=0;i<3;i++){
            q[i]=mid[i];
     }
    }

    if(right-left<2*dt){
        return result;
    }



    for(int i=0;i<3;i++){
        mid_left[i]=(t-dt)*c[i]+(1-(t-dt))*d[i];
    }
    for(int i=0;i<3;i++){
        mid_right[i]=(t+dt)*c[i]+(1-(t+dt))*d[i];
    }
    double left_value=distance(p,mid_left);
    double right_value=distance(p,mid_right);

    if(mid_value<right_value&&mid_value<left_value){
        return result;
    }
    if(left_value<right_value){
        result=left_value;
        for(int i=0;i<3;i++){
        q[i]=mid_left[i];
        }
        result=searchQ(left,t,c,d,p,q,result);
    }
    else{
        result=right_value;
        for(int i=0;i<3;i++){
        q[i]=mid_right[i];
        }
        result=searchQ(t,right,c,d,p,q,result);
    }






}
int main(void) {

   ifstream in("2.inp");
   ofstream out("station.out");


   double a[3];
   double b[3];
   double c[3];
   double d[3];

   in >> a[0] >> a[1] >> a[2];
   in >> b[0] >> b[1] >> b[2];
   in >> c[0] >> c[1] >> c[2];
   in >> d[0] >> d[1] >> d[2];

   double p[3];
   cout<<"-------"<<endl;
   double q[3];
   cout<<"-------"<<endl;

   for(int i=0;i<3;i++){
        p[i]=a[i];
        q[i]=c[i];
   }


   double current=DBL_MAX;
   double result=DBL_MAX;

   while(true){




        current=searchP(0,1,a,b,p,q,current);
        current=searchQ(0,1,c,d,p,q,current);

        if(current<result){
            result=current;

        }
        else{

            break;
        }


   }

   if(result-floor(result)<0.01){
    result=floor(result);
    out<<sqrt(result)<<endl;
   }
   else{

   out<< ceil(sqrt(result))<<endl;}
   in.close();
   out.close();
   return 0;
}
