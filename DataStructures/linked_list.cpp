/*
This code has all my linked list generation concepts
*/
#include <iostream>
#include <string.h>

typedef struct node{
	int data;
	node *next; // this line says that the node type variable is declared that points to the address of another node
	// in other words... node *v is a variable that points to other node type variables

}node;

// type is never pointer type! so never write function as *type
// The * will always come between, type and fucniton name.
node *make_list(int to_push[5]){
	node *prev = NULL;
	for(int i = 4; i >= 0; i--){
		// Always initialize this as a pointer to the structure
		node *N = (node*)malloc(sizeof(node));
		//this below line dont work as it is allocating memory Tat compile time
		// node N;
		// In c++ it can also be done by
		// node *N = new node; haha easy pesy. 
		N->data = to_push[i];
		N->next = prev;
		prev = N;
	}
	return prev;
}

int main(){

	// head points to the start of the linked list
	node *head = NULL; // not pointing to anything right now
	int to_push[5] = {3,4,5,1,2}; // push these into the linked list haha

	head = make_list(to_push);
	// head = head->next;
	while(head != NULL){
		std::cout << head->data << " ";
		head = head->next;
	}
		
	return 0;
}
