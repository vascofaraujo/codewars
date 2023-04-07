function likes(names) {
// TODO
if (names != ""){
    // let person_names = names.split()
    let length = names.length;
    if (length == 1){
        return `${names} likes this`;
    }else if (length == 2){
        return `${names[0]} and ${names[1]} like this`;
    }else if (length == 3){
        return `${names[0]}, ${names[1]} and ${names[2]} like this`;
    }else if (length >= 4){
        let len = names.length - 2; 
        return `${names[0]}, ${names[1]} and ${len} others like this`;
    }
}else{
    return 'no one likes this';
}
}

console.log(likes([]), 'no one likes this');
console.log(likes(["Peter", "John"]), 'Peter and likes this');