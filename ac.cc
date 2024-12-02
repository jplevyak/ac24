#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
  {
    ifstream ifs("1");
    std::vector<int> X;
    std::vector<int> Y;
    string line;
    while (getline(ifs, line)) {
      int x, y;
      sscanf(line.c_str(), "%d %d", &x, &y);
      X.push_back(x);
      Y.push_back(y);
    }
    sort(X.begin(), X.end());
    sort(Y.begin(), Y.end());
    int t = 0;
    for (int i = 0; i < X.size(); i++) {
      t += abs(X[i] - Y[i]);
    }
    printf("1a %d\n", t);

    int x = 0, y = 0;
    t = 0;
    while (x < X.size() && y < Y.size()) {
      if (X[x] == Y[y]) {
        t += Y[y];
        y++;
      } else if (X[x] < Y[y]) {
        x++;
      } else {
        y++;
      }
    }
    printf("1b %d\n", t);
  }
  return 0;
}
