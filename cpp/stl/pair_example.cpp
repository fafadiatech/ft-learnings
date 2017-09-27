#include <iostream>
#include <string>

using namespace std;

int main(){
  pair<string, int> lookup;
  lookup.first = "sidharth";
  lookup.second = 1;
  
  cout << "Output for Pair" << endl;
  cout << lookup.first << endl; 
  cout << lookup.second << endl;
  
  return 0;
}
