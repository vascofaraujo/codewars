function tojadencase(str)
    words = split(str, " ")
    final_str = ""
    for word in words
        final_str *= (uppercasefirst(word) * " ")
    end
    chop(final_str)
end


println(tojadencase("How can mirrors be real if our eyes aren't real"))
