#include <string>
#include <vector>
#include <iostream>


std::vector<std::string> solution(const std::string &s){

    std::vector<std::string> result {};
    std::string temp = s;
    if (temp.length() % 2 != 0){
        temp += "_";
    }

    for (auto i = temp.begin(); i != temp.end(); ++i){
        // std::cout << *i << *(++i) << std::endl;
        std::string aux { *i,  *(++i)};
        result.push_back(aux);
    }
    return result;
}

void printVector(std::vector<std::string> vec){
    for (auto i : vec) {std::cout << i << " ";}
}

int main(){

    std::string s {"abcdefj"};
    auto a = solution(s);
    printVector(a);
    // std::cout << a << std::endl;

    return 0;
}

