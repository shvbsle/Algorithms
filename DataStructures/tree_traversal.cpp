/*
this code is to implement all my tree traversals
*/
#include <iostream>
#include <vector>

typedef struct node{
	char data;
	node *left;
	node *right;
}node;

node *make_tree(char to_push[9]){
	node *a = (node*)malloc(sizeof(node));
	a->data = to_push[0];
	node *b = (node*)malloc(sizeof(node));
	b->data = to_push[1];
	a->left = b;
	node *c = (node*)malloc(sizeof(node));
	c->data = to_push[2];
	a->right = c;
	b->left = NULL;
	node *d = (node*)malloc(sizeof(node));
	b->right = d;
	d->data = to_push[3];
	node *e = (node*)malloc(sizeof(node));
	node *f = (node*)malloc(sizeof(node));
	e->data = to_push[4];
	e->left = NULL;
	e->right = NULL;
	f->data = to_push[5];
	f->left = NULL;
	f->right = NULL;
	d->left = e;
	d->right = f;
	node *g = (node*)malloc(sizeof(node));
	node *h = (node*)malloc(sizeof(node));
	g->data = to_push[6];
	g->left = NULL;
	g->right = NULL;
	h->data = to_push[7];
	h->left = NULL;
	h->right = NULL;
	c->left = g;
	c->right = h;
	return a;

}

void recur_preorder(node *root){
	if(root != NULL){
		std::cout << root->data;
		recur_preorder(root->left);
		recur_preorder(root->right);
	}

}

void recur_inorder(node *root){
	if(root != NULL){
		recur_inorder(root->left);
		std::cout << root->data;
		recur_inorder(root->right);
	}
}

void recur_postorder(node *root){
	if(root != NULL){
		recur_postorder(root->left);
		recur_postorder(root->right);
		std::cout << root->data;
	}
}

// Non recursive preorder traversal for my own satisfaction

void pre_order(node *root){
	// not sue if this will work
	std::vector<node *> stack;
	// Initial push of nodes onto the stack
	while(root != NULL){
		std::cout << root->data;
		stack.push_back(root);
		root = root->left;
	}

	// std::cout << stack.back()->data;

	// Once the stack is ready, we are ready to traverse in order
	while(!stack.empty()){
		root = stack.back();
		stack.pop_back();
		root = root->right;
		// std::cout << root->data;
		while(root != NULL){
			std::cout << root->data;
			stack.push_back(root);
			root = root->left;
		}
	}
}

int main(){
	char to_push[9]= {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'};
	node *root = NULL;

	root = make_tree(to_push);

	// These are all recursive traversals
	std::cout << "preorder: ";
	recur_preorder(root);
	std::cout << "\ninorder: ";
	recur_inorder(root);
	std::cout << "\npostorder: ";
	recur_postorder(root);

	std::cout << "\n\nnon-recursice method for preorder: ";
	pre_order(root);
	return 0;
}