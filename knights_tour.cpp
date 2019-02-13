/*
The knight is placed on the first block of an empty board &&, moving according to the rules of chess, must visit each square exactly once. 

Backtracking problem. These are usually trail && error problems.

Goal is to print the path matrix of the tour that coveres all the squares exaclty once

Starting is always 0,0

Don't try for 8,8.. will take too long. 

---------------------------------------

What the fuck!  C++ is so muc more faster than Python for this task

This solution stops as soon as it finds a working solution. This can be considered as branch & bound as well
*/
#include <bits/stdc++.h>
int size_x = 5, size_y = 5;
int total_left = size_x*size_y;

std::vector<std::pair<int, int>> possible_moves(int x, int y, int board[][5]){
	std::vector<std::pair<int, int>> moves;
	if (x+2 < size_x && y+1 < size_y && board[x+2][y+1] != 1)
		moves.push_back(std::make_pair(x+2, y+1));
	if (x-2 >= 0 && y+1 < size_y && board[x-2][y+1] != 1)
		moves.push_back(std::make_pair(x-2,y+1));
	if (x+2 < size_x && y-1 >= 0 && board[x+2][y-1] != 1)
		moves.push_back(std::make_pair(x+2, y-1));
	if (x-2 >=0 && y-1 >=0 && board[x-2][y-1] != 1)
		moves.push_back(std::make_pair(x-2, y-1));
	if (y+2 < size_y && x+1 < size_x && board[x+1][y+2] != 1)
		moves.push_back(std::make_pair(x+1, y+2));
	if (y-2 >= 0 && x+1 < size_x && board[x+1][y-2] != 1)
		moves.push_back(std::make_pair(x+1, y-2));
	if (y+2 < size_y && x-1 >= 0 && board[x-1][y+2] != 1)
		moves.push_back(std::make_pair(x-1,y+2));
	if (y-2 >=0 && x-1 >=0 && board[x-1][y-2] != 1)
		moves.push_back(std::make_pair(x-1, y-2));
	return moves;

}

void render_board(std::vector<std::pair<int, int>> path){
	int brd[5][5] = {0};
	// memset(brd, -1, sizeof(brd[0][0])*size_x*size_y);

	for(int i = 0; i < path.end() - path.begin(); i++){
		brd[path[i].first][path[i].second] = i+1;
	}

	for(int i = 0; i < 5; i++){
		std::cout << brd[i][0] << " " << brd[i][1] << " " << brd[i][2] << " " << brd[i][3] << " " << brd[i][4] << "\n";
	}
}

void show_brd(int board[][5]){
	for(int i = 0; i<5; i++){
		std::cout << board[i][0] << " " << board[i][1] << " " << board[i][2] << board[i][3] << " " << board[i][4] <<"\n";
	}
}

std::vector<std::pair<int, int>> tour(int x, int y, int board[][5], std::vector<std::pair<int, int>> path, int total_left){
	int brd_copy[5][5];
	for(int i = 0; i < 5; i++){
		brd_copy[i][0] = board[i][0];
		brd_copy[i][1] = board[i][1];
		brd_copy[i][2] = board[i][2];
		brd_copy[i][3] = board[i][3];
		brd_copy[i][4] = board[i][4];
	}
	brd_copy[x][y] = 1;
	path.push_back(std::make_pair(x,y));
	total_left --;
	std::vector<std::pair<int, int>> moves = possible_moves(x, y, brd_copy), p;
	if(!moves.empty()){
		for(int i = 0; i < moves.end() - moves.begin(); i++){
			// std::cout << "moving: " << moves[i].first << ", " << moves[i].second << "\n";
			// show_brd(brd_copy);
			// std::cout << "--------------------------------------\n";
			p = tour(moves[i].first, moves[i].second, brd_copy, path, total_left);
			if(p.end() - p.begin() == size_y*size_x){
				return p;
			}
		}
		return {};
	}
	else if(total_left == 0){
		return path;
	}
	else{	
		// render_board(path);
		return {};
	}
}

int main(){
	int board[5][5];
	// initialize the array values
	// args: array_name, init_value, total_size
	std::memset(board, 0, sizeof(board[0][0]) * size_x * size_y);

	std::vector<std::pair<int, int>> T, path;
	T = tour(0 ,0, board, path, total_left);

	if(!T.empty()){
		std::cout << "Tour found!\n";
		render_board(T);
	}
	else{
		std::cout << "no tour!";
	}
	return 0;
}
