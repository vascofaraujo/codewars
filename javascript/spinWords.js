function spinWords(string){
    //TODO Have fun :)
    let words = string.split(" ");
  
    const newWords  = [];

    for(let i=0; i<words.length; i++){
        // console.log(words[i])
        let len = words[i].length;
        if (len >= 5) {
            const newWord = [];
            for (let p=0, q=len-1; p<len; p++, q--){
                // console.log(string[i]);
                console.log(words[i][q])
                newWord[p] = words[i][q];
                // console.log(newWord);
                }
            newWords[i] = newWord.join("")
        }else{
            newWords[i] = words[i]
        }
    }
    return newWords.join(" ") 
}

// console.log(spinWords('Welcome'), 'emocleW')
console.log(spinWords('Hey fellow warriors'), 'Hey wollef sroirraw')