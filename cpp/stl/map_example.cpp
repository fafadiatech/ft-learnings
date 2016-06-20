#include <iostream>
#include <map>
#include <string>

using namespace std;

int main(){
  map<string, string> mobiles;
  mobiles["sidharth shah"] = "9321009382";
  mobiles["manan shah"] = "9657003382";
  for(map<string, string>::iterator it=mobiles.begin(); it != mobiles.end(); ++it){
    cout << it->first << "->" << it->second << endl;
  }
}
