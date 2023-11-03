#include <iostream>
#include <string>

void move_characters(std::string &solution, std::string str, int currIndex, int lastWordIndex){
    
    solution[currIndex] = str[lastWordIndex];
    int b = lastWordIndex;
    for (int j = currIndex; j >= lastWordIndex; --j, b++){
        solution[j] = str[b];
    } 
}

std::string reverse_words(std::string str){

     std::string solution (str.length(), ' ');
    
    int lastWordIndex = 0;
    for (int i = 0; i < str.length(); i++){
        if (std::isalpha(str[i]) || std::ispunct(str[i])){
            if (i > 0){
                move_characters(solution, str, i, lastWordIndex);
            }else{
                solution[i] = str[i];
            }
        }else{
            lastWordIndex = i+1;
            solution[i] = str[i];
        }
    }
    return solution;
}

int main(){

    // std::string s {"a b c d"};
    std::string s {"double  space"};

    auto solution = reverse_words(s);

    std::cout << solution;

    return 0;
}
