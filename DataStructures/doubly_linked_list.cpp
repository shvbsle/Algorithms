/*
code to reverse a doubly linked list
*/

#include <iostream>
typedef struct node
{
	int data;
	node *next;
	node *prev;
	
}node;

node *make_list(int to_push[5]){
	node *prev = NULL;
	// dont rush. check if conditions are correct
	for(int i= 4; i>=0; i--){
		node *N = (node*)malloc(sizeof(node));
		N->prev = NULL;
		if(i != 4){
			prev->prev = N; // great trick to set previous nodes :)
		}
		N->data = to_push[i];
		N->next = prev;
		prev = N;
	}
	return prev;
}

// Amazing code to reverse a list. Learnt a lot!
// what i did here was, swap the prev and next pointers and 
// at the end of the original DLL, head pointed to NULL and temp pointed to second last element
// so setting head = temp->prev after the while loop makes head the start of the linked list!
node *reverse(node *head){
	head->prev = NULL;
	node *temp;
	while(head != NULL){
		temp = head->prev;
		head->prev  = head->next;
		head->next = temp;
		head = head->prev;
	}
	head = temp->prev;	
	return head;
}

int main(){

	node *head = NULL, *travel =  NULL;
	int to_push[5] = {3,2,5,6,7};
	head = make_list(to_push);
	travel = head;
	while(travel!= NULL){
		std::cout << travel->data << " ";
		travel = travel->next;
	}
	std::cout << "\nrev order is: \n";
	travel = reverse(head);
	while(travel!= NULL){
		std::cout << travel->data << " ";
		travel = travel->next;
	}
	return 0;
}