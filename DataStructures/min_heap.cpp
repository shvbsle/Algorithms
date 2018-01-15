/*
C++ code for building a min heap and performing actions on it
*/
#include <bits/stdc++.h>

void delete_root(int heap[], int heap_size){
	// here is how to delete the root

	heap[0] = heap[heap_size-1];
	heap_size--;
	int left = 1, right = 2, par = 0;
	while(heap[par] > heap[left] || heap[par] > heap[right]){
		if(heap[left] < heap[right]){
			heap[par] = heap[left]+heap[par];
			heap[left] = heap[par]-heap[left];
			heap[par] = heap[par]-heap[left];
			par = left;
		}
		else{
			heap[par] = heap[right]+heap[par];
			heap[right] = heap[par]-heap[right];
			heap[par] = heap[par]-heap[right];
			par = right;
		}
		left = 2*par+1;
		right = left+1;
	}

	std::cout << "\nafter root delete:\n";

	for(int i = 0; i < heap_size; i++){
		std::cout << heap[i] << " ";
	}

}

int main(){
	int heap[100] , heap_size = 0;
	for(int i = 0; i <15 ; i++){
		heap[i] = (int)std::rand()%50;
		std::cout << heap[i] << " ";
		heap_size++;
		int parent = (i-1)/2, child = i;
		while(parent >= 0 && heap[parent] > heap[child]){
			// swap them
			heap[parent] = heap[child]+heap[parent];
			heap[child] = heap[parent]-heap[child];
			heap[parent] = heap[parent]-heap[child];
			child = parent;
			parent = (child-1)/2;
		}
	}
	std::cout << "\nresult:\n";

	for(int i = 0; i < heap_size; i++){
		std::cout << heap[i] << " ";
	}

	/*
	Pseudo code for insertion on a heap:
	// num is the number to be inserted and "heap_end" is the end point of the heap
	Insert(num, heap_end){
		heap[heap_end] = num
		child = heap_end 
		parent = (child-1)/2 //is heap index starting from 0
		while(parent >=0 && heap[parent] > heap[child]){
			swap(heap[parent], heap[child])
			child = parent
			parent = (child-1)/2
		}
		heap_end++;
		This takes heapify as well
	}
	*/

	delete_root(heap, heap_size);
	

	std::cout << "\n\nafter general element delete:";

	//delete element 8
	heap[8] = -1; //give it the least possible value
	heap_size--;
	// float it up
	int parent = (8-1)/2, child = 8;
		while(parent >= 0 && heap[parent] > heap[child]){
			// swap them
			heap[parent] = heap[child]+heap[parent];
			heap[child] = heap[parent]-heap[child];
			heap[parent] = heap[parent]-heap[child];
			child = parent;
			parent = (child-1)/2;
		}

	std::cout << "\nsmall value floated up:\n";

	for(int i = 0; i < heap_size; i++){
		std::cout << heap[i] << " ";
	}

	delete_root(heap, heap_size);



	return 0;
}