#include <iostream>
#include <pthread.h>

using namespace std;

void* some_thread(void *args){
  int i = *((int *)args);
  cout << "hello from thread land:" << i << endl;
}

int main(){
  int data[10];
  for(int i=0; i<10; i++){
      pthread_t t;
      data[i] = i;
      pthread_create(&t, NULL, &some_thread, &data[i]);

      void* result;
      pthread_join(t, &result);
  }
  return 0;
}
