#include <stdio.h>
#include <stdlib.h>

struct node{
  int data;
  struct node *next;
};

void appendNode(struct node *head, int value){
  while(head->next != NULL){
    head = head->next;
  }
  
  struct node *current = (struct node *)malloc(sizeof(struct node));
  current->data = value;
  current->next = NULL;
  
  head->next = current;
}

int length(struct node *head){
  int n = 0;

  while(head->next != NULL){
    head = head->next;
    n += 1;
  }
  return n + 1;
}

void traverse(struct node *head){
  while(head->next != NULL){
    printf("%d\n", head->data);
    head = head->next;
  }
  
  printf("%d\n", head->data);
}

int main(){
  struct node *root = (struct node *)malloc(sizeof(struct node));
  root->data = 10;
  root->next = NULL;

  printf("Root value is:%d\n", root->data);
  printf("Length of List:%d\n", length(root));
  
  for(int i=2; i<= 10; i++){
    appendNode(root, i*10);
  }

  printf("Length of List:%d\n", length(root));
  
  traverse(root);
  return 0;
}
