#include <stdio.h>

int main(){
  int val;
  int *ptr;
  
  val = 10; 
  ptr = &val;

  printf("Value {before change} from pointer is:%d\n", *ptr);
  *ptr = 20;
  printf("Value {after change} from pointer is:%d\n", *ptr);
}
