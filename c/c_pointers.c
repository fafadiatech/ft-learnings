#include <stdio.h>

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
  *ptr = 20;
  printf("Value {after change} from pointer is:%d\n", *ptr);
}
