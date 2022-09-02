#include "timebomb.h"
#include <iostream>
#include <list>


int main() {
    int result;
    int N;
    int a;
    int b;
    int a_index;
    int b_index;
    int max;
    int second= -1;
    int second_index=0;
    box_ready();
    N = box_size();
    std::list<int> q;
    std::list<int> q_index;
    std::list<int> last;
    std::list<int> last_index;
    std::list<int> vs;
    std::list<int> vs_index;
    for (int i=1;i<N+1;i=i+2){
        
        result = box_comp(Box[i], Box[i+1]);
        if (result==-1){
            q.push_back(Box[i]);
            q_index.push_back(i);
        }
        else if(result==1) {
            q.push_back( Box[i+1]);
            q_index.push_back(i+1);
        }
        vs.push_back(Box[i]);
        vs_index.push_back(i);
        vs.push_front(Box[i+1]);
        vs_index.push_front(i+1);
    }
    while(!q.empty()){
        a = q.front();
        q.pop_front();
        b = q.front();
        q.pop_front();
        a_index=q_index.front();
        q_index.pop_front();
        b_index=q_index.front();
        q_index.pop_front();
        result =box_comp(a, b);
        if (result==-1){
            q.push_back(a);
            q_index.push_back(a_index);
        }
        else if(result==1) {
            q.push_back(b);
            q_index.push_back(b_index);
        }
        vs.push_back(a);
        vs_index.push_back(a_index);
        vs.push_front(b);
        vs_index.push_front(b_index);

    }
    max = q.back();
    while (!vs.empty()){
        if (vs.front() == max){
            last.push_back(vs.front());
            last_index.push_back(vs_index.front());

        }
        if (vs.back() == max){
            last.push_back(vs.front());
            last_index.push_back(vs.front());
        }
        vs.pop_front();
        vs.pop_back();
        vs_index.pop_front();
        vs_index.pop_back();
    }
    while(!last.empty()){
        if (second<last.back()){
            second = last.back();
            second_index = last_index.back();
            last.pop_back();
            last_index.pop_back();
        }
    }
    box_report(second_index+1);
    std::cout<< second_index;
    return 0;
}
