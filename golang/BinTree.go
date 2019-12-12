/* Go exmaple of building a binary tree*/
package main

import(
	"fmt"
	"math/rand"
)

type Node struct{
	val int
	left *Node
	right *Node
}

func insertNode(item int, root *Node){
	newNode := &Node{val:item}
	for root != nil{
		if item > root.val{
			if root.right == nil{
				root.right = newNode
				break
			} else{
				root = root.right
			}
		} else{
			if root.left == nil{
				root.left = newNode
				break
			} else{
				root = root.left
			}
		}
	}
}

func buildTree(to_push []int) *Node{
	// build the tree and return the root
	ROOT := &Node{val:to_push[0]}
	for _, item := range to_push[1:]{
		insertNode(item, ROOT)
	}
	fmt.Println("Tree built")
	return ROOT
}

// Tree traversal
// Should be pretty straight forward by now
func traverseTree(root *Node){
	if root == nil{
		return 
	}
	traverseTree(root.left)
	fmt.Println(root.val)
	traverseTree(root.right)
}

func main(){
	values := []int{}

	for i:=0; i<10; i++{
		values = append(values, rand.Intn(30))
	}

	fmt.Println("Will start building this tree:")
	fmt.Println(values)

	ROOT := buildTree(values)
	fmt.Println("\nTraversing the tree in Left-Center-Right:")
	traverseTree(ROOT)


}