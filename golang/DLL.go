/*
Doubly linked list in golang and some implementations in golang
*/

package main

import(
	"fmt"
)

type Node struct{
	val int
	next *Node
	prev *Node
}

func makeDLL(to_push []int) *Node{
	// Built a tree and access the head
	HEAD := &Node{next:nil, prev:nil}
	temp := HEAD
	for _, item  := range to_push{
		var new = Node{val:item, prev:temp, next:nil}
		temp.next = &new
		temp = &new
	}
	return HEAD
}

func walkDLL(head *Node){
	for head != nil{
		fmt.Println(head)
		head = head.next
	}
}

func main(){
	to_push := []int{1,1,2,3,5,8,13,21}
	head := makeDLL(to_push)
	walkDLL(head)
	

}