#include <iostream>
#include <vector>
using namespace std;

int input1 = 0, input2 = 0, max_len = 0;
vector<vector<char>> input_path(26, vector<char>());
vector<vector<int>> input_len(26, vector<int>(26, 0));
vector<bool> visit(26, 0);
vector<char> my_stack;



void search(int index, int len) {
    if (!my_stack.empty() && my_stack[my_stack.size() - 1] == 'a') {
        if (max_len < len){
            max_len = len;
        }
        return;
    }


    for (int i = 0; i < input_path[index].size(); i++) {
        if (visit[input_path[index][i] - 'a']) {
            continue;
        }
        else{
        len += input_len[index][input_path[index][i] - 'a'];
        visit[input_path[index][i] - 'a'] = true;
        my_stack.push_back(input_path[index][i]);
        search(input_path[index][i] - 'a', len);
        my_stack.pop_back();
        len -= input_len[index][input_path[index][i] - 'a'];
        visit[input_path[index][i] - 'a'] = false;
        }
    }
}

int main() {
    char temp1, temp2;
    int leng = 0;
    cin >> input1 >> input2;

    for (int i = 0; i < input2; i++) {
        cin >> temp1 >> temp2 >> leng;
        input_path[temp1 - 'a'].push_back(temp2);
        input_path[temp2 - 'a'].push_back(temp1);
        input_len[temp1 - 'a'][temp2 - 'a'] = leng;
        input_len[temp2 - 'a'][temp1 - 'a'] = leng;
    }
    search(0, 0);
    cout << max_len;
}
