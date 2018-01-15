/*
Here is my attempt at building a trie.

I will build a trie for the following strings:

there
their
answer
any 
bye
*/

#include <bits/stdc++.h>
struct trie_node;

typedef struct trie_node
{
	char data;
	std::map<char, trie_node *> nodes;

}trie_node;

trie_node *insert_element(trie_node *root, std::string s1){
	std::cout << s1.at(0) << "\n";//| " << root<< "\n";
	if(root!=NULL){
		// std::cout << "not null!\n";
		std::map<char, trie_node*> M = root->nodes;
		if(M[s1.at(1)] == NULL){
			// std::cout << M[s1.at(1)]<<"|"<<s1.at(1) << " will add\n";
			trie_node *temp = insert_element(M[s1.at(1)], s1.substr(0, s1.length()));
			// M.insert(std::pair<char, trie_node*>(s1.at(0), temp));
			M[s1.at(1)] = temp;
			temp->nodes = M;
			return root;
		}else{
			std::cout << "vis\n";
			int sp = 0;
			trie_node *temp = M[s1.at(1)], *N;
			// temp->data = s1.at(0);
			N = insert_element(temp->nodes[s1.at(2)], s1.substr(2, s1.length()));
			// M = temp->nodes;
			// M.insert(std::pair<char, trie_node*>((char)s1.at(1), N));
			// temp->nodes = M;
			return root;
		}// insert_element
	}
	else{
		// std::cout << "bad side \n";
		trie_node *temp;
		root = (trie_node*)malloc(sizeof(trie_node));
		root->data = s1.at(0);
		if(s1.length() > 1){
			std::map<char, trie_node*> M = root->nodes;
			temp  =  insert_element(M[s1.at(1)], s1.substr(1, s1.length()));
			M[s1.at(1)] = temp;
			root->nodes = M;
		}
		// std::cout << temp<<"| "<< s1.at(0) << "| " << root<< "\n";
		return root;
	}
}

/*
Holy fuck this code was hard to write and learnt wayyy to many new things from this one. Wow


*/

int main(){
	std::string s1[5] = {"there", "their", "answer", "any", "bye"};
	trie_node *root = (trie_node*)malloc(sizeof(trie_node)), *N = NULL;
	root->data = '!';
	std::map<char, trie_node*> M = root->nodes;
	/*
	Here is a very huge and frustrating thing about maps and a frustrating property
	about them.
	in c++ maps perform map.insert() iff map doesnt have that key

	however stupidity is that if, I use a variable such as, map[3] then it automatically
	sets the value of the map to NULL or 0. This is frustrating. I have been struggling to find fault 
	in my PERFECT algorithm when the only thing missing was that the map use sucked a lot

	*/
	for(int i = 0; i < 5; i++){
		// std::cout << s1[i].at(0) << "|" << M[s1[i].at(0)] << " \n";
		N = insert_element(M[s1[i].at(0)], s1[i]);
		M[s1[i].at(0)] = N;
		// std::cout << "now I have node: " << N << "\n";	
		root->nodes = M;
	}

	return 0;
}
