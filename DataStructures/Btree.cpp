/*
I think this will be challenging but here is my attempt at creating a Btree and doing insertion in it
*/
#include <bits/stdc++.h>


// Dayum today I learnt interdependent struct declarations
struct key;

typedef struct node
{
	struct key *head;
	int key_count;
}node;


typedef struct key{
	int data;
	// this will be a nice doubly linked list
	key *next, *prev;
	// these are pointers to it's two children
	node *left;
	node *right;
}key;

node *insert(node* root, int value){
	if(root!=NULL){
		key *traversal = root->head, *K, *old;
		int move_count = 1;
		while(traversal!=NULL && traversal->data < value){
			old = traversal;
			traversal = traversal->next;
			move_count++;
		}
		if(traversal == NULL){
			traversal = old;
		}
		if(root->key_count < 3){
			// insert new node into empty space
			K = (key*)malloc(sizeof(key));
			K->data = value;
			K->next = traversal->next;
			K->prev = traversal;
			K->left = traversal->right;
			K->right = NULL;
			// update linked list
			traversal->next = K;
			root->key_count++;
			// std::cout << K->prev->data << " "<< K->data << " |"<<root->key_count<< "\n";
		}
		else{

			K = (key*)malloc(sizeof(key));
			K->data = value;
			K->next = traversal->next;
			K->prev = traversal;
			K->left = traversal->right;
			if(move_count < 4){
				K->right = traversal->next->left;
			}
			else{
				K->right = NULL;
			}
			// create a split point
			key *split_point = root->head->next->next;
			root->head->next->next = NULL;
			// create new nodes
			node *R1 = (node*)malloc(sizeof(node)), *R2 = (node*)malloc(sizeof(node));
			R1->head = root->head;
			R1->key_count = 1;
			R2->head = split_point;
			R2->key_count = 1;

			root->head = traversal;
			root->key_count = 0;
			// std::cout << " whoa dayum!\n";
			return root;
		}
	}
	else{

		root = (node*)malloc(sizeof(node));
		// set the first key
		key *K = (key*)malloc(sizeof(key));
		K->data = value;
		K->next = NULL;
		K->prev = NULL;
		K->left = NULL;
		K->right = NULL;
		// set the head of the root to first element
		root->head = K;
		root->key_count = 0;
		return root;
	}
	return NULL;
}

int main(){
	node *root = insert(root, 10);
	insert(root, 50);
	insert(root, 60);
	insert(root, 70);
	insert(root, 100);
	// std::cout << "compiles";
	return 0;
}