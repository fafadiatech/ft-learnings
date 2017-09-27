#include <iostream>
#include <vector>

using namespace std;

int main(){
  vector <int> nums;
  for(int i=0; i<100; i++){
    nums.push_back(i);
  }
  
  cout << "Done inserting nums" << endl;
  cout << "Total numbers of elements:" << nums.size() << endl;
  
  cout << "Iterating using sizes" << endl;
  for(int i=0; i<nums.size(); i++){
    cout << nums[i] << endl;
  }
  
  cout << "Iterating using iterator" << endl;
  for(vector<int>::iterator it = nums.begin() ; it != nums.end(); ++it){
    cout << *it << endl;
  }
  return 0;
}
