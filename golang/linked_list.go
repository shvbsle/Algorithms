// This is my algorithm practice in golang
// Aim of this code is to implement a linked list and some linked list based operations in golang

/*
 A lot of great lessons for pointers in Golang

 declare a pointer type:
	ptype *int

 assign a pointer type

	ptype := &object

 object can be directly access via a pointer type variable haha hehe

 instead of doing:
	temp := *ptype
	temp.val

	we can do:
	ptype.val
	
*/
package main

import(
	"fmt"
	"strconv"
)

type LL struct{
	value int
	next *LL
}

func makeLL(list_items []int) *LL{
	// accept a list of numbers as an input and return the head of the linked list
	HEAD := &LL{}
	var temp = HEAD
	for _, item := range list_items{
		var new = LL{value:item, next:nil}
		temp.next = &new
		temp = &new
	}
	fmt.Println("Linked List Built. Returning the head")
	return HEAD
}

func walkLL(head *LL, num int){
	// num is the element till which you want to travel in the linked list
	var start = head.next
	counter := 0
	for start != nil{
		if counter == num{
			fmt.Println("element "+strconv.Itoa(num)+" reached")
			break
		}
		fmt.Println(start.value)
		start = start.next
		counter+=1
	}
}


func main(){
	var list_to_push = []int{1,1,2,3,5,8,13,21}
	var head = makeLL(list_to_push)
	walkLL(head, 3)

}