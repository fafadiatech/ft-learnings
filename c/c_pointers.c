#include <stdio.h>

// This will increment value pointed by prt by adding offset
void increment(int *ptr, int offset){
  *ptr += offset;
}

int main(){
  int val;
  
  // Pointer to an integer
  // Remember int* ptr and int *prt are equivalent
  int *ptr;
  
  val = 10; 
  
  // Referencing using * operator
  ptr = &val;
  
  // Dereferencing using ** operator
  printf("Value {before change} from pointer is:%d\n", *ptr);
  increment(ptr, 14);
  printf("Value {after change} from pointer is:%d\n", *ptr);
  
  
}
