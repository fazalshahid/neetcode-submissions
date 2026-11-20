#include <unordered_set>
#include <bits/stdc++.h>
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        
        for (auto i = 0; i < board.size(); ++i)
        {
            unordered_set <int> seen;
            for (auto j = 0; j < board[i].size(); ++j) {
                if (seen.count(board[i][j])) {
                    return false;
                }
                if (! std::isdigit(board[i][j])){
                    continue;
                }
                seen.insert(board[i][j]);
            }
        }

        for (auto i = 0; i < board.size(); ++i)
        {
            unordered_set <int> seen;
            for (auto j = 0; j < board[i].size(); ++j) {
                if (seen.count(board[j][i])) {
                    return false;
                }
                if (! std::isdigit(board[j][i])){
                    continue;
                }
                seen.insert(board[j][i]);
            }
        }

        auto is_unique = [&board] (int rowS, int rowE, int colS, int colE) {
            unordered_set <int> seen;

            for (auto i = rowS; i <= rowE; ++i) {
                for (auto j = colS; j <= colE; ++j) {
                    if(seen.count (board[i][j])) {
                        return false;
                    }
                    if (! std::isdigit(board[i][j])){
                        continue;
                    }
                    seen.insert(board[i][j]);
                }
            }
            return true;
        };

        /*
        return is_unique(0, 2, 0, 2) &&
        is_unique(0, 2,3,5) && is_unique(0, 2, 6, 8)
        && is_unique(3, 5, 0, 2) && is_unique(3,5, 3, 5)
        && is_unique(3, 5, 6, 8) && is_unique(6, 8, 0, 2)
        && is_unique(6, 8,3,5) && is_unique(6, 8, 6, 8);
        */

        for (auto i = 0; i < 7; i = i + 3) {
            for (auto j = 0; j < 7; j = j + 3) {
                if (! is_unique(i, i + 2, j, j + 2)) {
                    return false;
                }
            }
        }

        return true;
    }
};
