#include <vector>
#include <iostream>

bool compareNums(int a, int b){
    if (a > b){
        return true;
    }else{
        return false;
    }
}
std::vector<int> solution(std::vector<int> nums) {
 
    for (auto i = nums.begin(); i != nums.end(); ++i){
        std::cout << *(++i) << std::endl;
       // biggerNum = compareNums(*i, *(++i)) ;
    }
    return nums;
}


template <typename T>
void printVector(T vec){
    for (auto i : vec) {std::cout << i << " ";}
}

int main(){

    std::vector<int> nums {1, 20, 3, 4, 2};
    printVector(solution(nums));
    
}
