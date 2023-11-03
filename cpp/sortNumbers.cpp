#include <vector>
#include <iostream>

template <typename T>
void printVector(T vec){
    for (auto i : vec) {std::cout << i << " ";}
}

bool compareNumbers(int a, int b){
    if (a>b){
        return true;
    }else{
        return false;
    }
}

// implement bubble sort algorithm
std::vector<int> solution(std::vector<int> nums) {
 
    for (int i = 0; i < nums.size(); ++i){
       for (int j = 0; j < (nums.size()-i-1); ++j){
            if (compareNumbers(nums[j], nums[j+1])){
                int temp = nums[j];
                nums[j] = nums[j+1];
                nums[j+1] = temp;
            }
        } 
    }
    return nums;
}


int main(){

    std::vector<int> nums {1, 20, 3, 4, 2};
    printVector(solution(nums));
   return 0; 
}
