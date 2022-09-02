#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct work {
    int start;
    int end;
    int money;
    int days;
};
vector<work> job_list;

bool cmp(work a, work b) {
    return a.start<b.start;
}

int make_job(int n) {
    int start = 0, end = 0, money = 0, last_day = 0;
    for (int i = 0; i < n; i++) {
        work temp;
        cin >> start >> end >> money;
        if (last_day < end) last_day = end;
        temp.start = start; temp.end = end; temp.money = money-10; temp.days = end - start + 1;
        job_list.push_back(temp);
    }
    sort(job_list.begin(), job_list.end(), cmp);

    return last_day;
}

int custom_max(int a, int b, int i, vector<int>& DAY, vector<int> DP) {
    int min_day = 0;
    if (a > b) {
        DAY[job_list[i].start] = DAY[job_list[i+1].start];
        return a;
    }
    else {
        if (i == job_list.size() - 1) DAY[job_list[i].start] = job_list[i].days;
        else {
            if (b == DP[job_list[i+1].start]) {
                min_day = min(DAY[job_list[i+1].start], DAY[job_list[i].end + 1] + job_list[i].days);
                DAY[job_list[i].start] = min_day;
            }
            else DAY[job_list[i].start] = DAY[job_list[i].end + 1] + job_list[i].days;
        }
        return b;
    }
}

void dy_pro(vector<int>& DP, vector<int>& DAY) {
    for (int i = job_list.size() - 1; i >= 0; i--) {
        int temp = 0;
        if (i == job_list.size() - 1) {
            DP[job_list[i].start] = custom_max(DP[job_list[i].start + 1], DP[job_list[i].end + 1] + job_list[i].money, i, DAY, DP);
        }
        else {
            if (job_list[i].start == job_list[i + 1].start) {
                temp = custom_max(DP[job_list[i].start + 1], DP[job_list[i].end + 1] + job_list[i].money, i, DAY, DP);
                if (temp > DP[job_list[i].start]) DP[job_list[i].start] = temp;
            }
            else DP[job_list[i].start] = custom_max(DP[job_list[i].start + 1], DP[job_list[i].end + 1] + job_list[i].money, i, DAY, DP);
        }
        if (i != 0) {
            for (int k = job_list[i - 1].start + 1; k < job_list[i].start; k++) {
                DP[k] = DP[job_list[i].start];
                DAY[k] = DAY[job_list[i].start];
            }
        }
    }
}

int main() {
    int n = 0, idx = 2000, last_day = 0;
    int res1, res2;
    cin >> n;

    last_day = make_job(n);
    vector<int> DP(last_day+2);
    vector<int> DAY(last_day+2);
    dy_pro(DP, DAY);

    res1 = *max_element(DP.begin(), DP.end());
    res2 = *max_element(DAY.begin(), DAY.end());
    cout << res1+10 << " " << res2;
    return 0;
}
