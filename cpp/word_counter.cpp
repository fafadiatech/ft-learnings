#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <regex>
#include <map>
#include <stdlib.h>

using namespace std;

int main(int argc, char* argv[]){
  
  if (argc <= 1){
    cout << "Please specify input" << endl;
    exit(-1);
  }else{
    map <string, long> counts;
    regex re("\\w+");
    for(int i=1; i<argc; i++){
      cout << "Processing file:" << endl;
      cout<< argv[i] <<endl;
      ifstream infile(argv[i]);
      string line; 
      
      //Read input line by line
      while(getline(infile, line)){
	istringstream iss(line);
	regex_iterator<string::iterator> it(line.begin(), line.end(), re);
	regex_iterator<string::iterator> end;
	
	for(; it != end; ++it){
	  string token = it->str();
	  transform(token.begin(), token.end(), token.begin(), ::tolower);
	  if(counts.count(token) > 0){
	    counts[token] += 1;
	  }else{
	    counts[token] = 1;
	  }
	}
	
	map<string, long>::iterator counts_it;
	
	for(counts_it=counts.begin(); counts_it!= counts.end(); ++counts_it){
	  string token = counts_it->first;
	  long count = counts_it->second;
	  
	  cout << "(" << token << "," << count << ")" << endl;
	}
      }
    }
  }
  
  return 0;
}
