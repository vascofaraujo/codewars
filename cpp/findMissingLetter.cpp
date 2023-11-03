#include <iostream>
#include <vector>
#include <algorithm>


const std::vector<char> abc {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};    


template <typename T>
void printVector(T vec){
    for (auto i : vec) {std::cout << i << " ";}
}

char findMissingLetter(const std::vector<char>& chars)
{
    auto it = std::find(abc.begin(), abc.end(), *chars.begin());
    for (auto i = chars.begin(); i != chars.end(); ++i){
        if (*it != *i){
            return *it;
        }else{
            ++it;
        }
    }
    return ' ';
}



int main(){
    const std::vector<char>& chars {'a', 'b', 'c', 'd', 'f'};
    auto solution = findMissingLetter(chars);

    std::cout << std::endl << solution;
    return 0;
}
