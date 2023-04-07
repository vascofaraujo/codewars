function onlyUnique(value, index, self) {
  return self.indexOf(value) === index;
}

function onlyDifferent(a, b){
    const diff = []
    d_i = 0
    for(let i in a){
        if (b.includes(a[i]) == false){
            console.log(a[i])
            diff[d_i] = a[i]
            d_i++
        }  
    }
    console.log(diff)
    return diff
    
}

function arrayDiff(a, b) {
  let b_unique = b.filter(onlyUnique)
  return onlyDifferent(a, b_unique) 

}


// console.log(arrayDiff([1,2], [1]), [2], "a was [1,2], b was [1]");
// console.log(arrayDiff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1]");
console.log(arrayDiff([], [1,2]), [], "a was [], b was [1,2]");
