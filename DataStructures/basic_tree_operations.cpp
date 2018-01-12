/*
this code is my method of performing basic tree operations..

like:
no.of nodes
no of leafs
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

int count_nodes(node *root){
	if(root!=NULL){
		return 1+count_nodes(root->left)+count_nodes(root->right);
	}
	else{
		return 0;
	}
}

int count_leafs(node *root){
	if(root!=NULL){
		if(root->left == NULL && root->right == NULL){
			return 1;
		}
		else{
			return count_leafs(root->left)+count_leafs(root->right);
		}
	}
	else{
		return 0;
	}
}

// Non recursive leaf count

// this idea of mine is based on tree traversal algo that I wrote before. I will write the post
// order non recursive algorithm to get better accustomed to this

//The idea behind non recursive leaf count is that, I simply traverse the tree in a non-recursive
//manner and the point where I print/visit the node, I simply check the children of the node and
//increment the count.

//This is a great approach because, I don't have to come up with a new algorithm for non recursive leaf count
// or any such thing. One traversal algorithm will do it all!
// make a flash card out of this!

int non_recur_leaf_count(node *root){
	std::vector<std::pair<node *, int>> stack;
	int count = 0;

	while(root != NULL){
		stack.push_back(std::make_pair(root, 0));
		root = root->left;
	}

	while(!stack.empty()){
		std::pair<node *, int> R = stack.back();
		stack.pop_back();
		root = R.first;
		if(R.second == 0){
			stack.push_back(std::make_pair(root, 1));
			root = root->right;
			while(root!=NULL){
				stack.push_back(std::make_pair(root, 0));
				root = root->left;
			}
		}
		else{
			if(root->left == NULL && root->right == NULL){
				count++;
			}
		}
	}
	return count;
}

int main(){
	char to_push[9]= {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'};
	node *root = NULL;

	root = make_tree(to_push);


	// haha works!
	std::cout << "no of nodes are: " << count_nodes(root);

	//leaf nodes
	std::cout << "\nno of leaf nodes are: " << count_leafs(root);

	std::cout << "\n(non recurr)no of leaf nodes are: " << non_recur_leaf_count(root);


	return 0;
}