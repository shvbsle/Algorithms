/*
this code is my method of creating a binary tree.
Turns out that this is not an easy task.

This is hardcoded construction
*/
#include <iostream>

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

int main(){
	char to_push[9]= {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'};
	node *root = NULL;

	root = make_tree(to_push);
	return 0;
}