function elim_dir(arr, directions, opposites)
    final_arr = String[] 
    i = 1
    while (i <= length(arr))
            if i == length(arr)
                push!(final_arr, arr[i]) 
                break
            elseif i > length(arr)
                break
            elseif (occursin(arr[i+1], replace(opposites[get(directions, arr[i], 0)], arr[i]=>"")))
                i = i + 2
            else
                push!(final_arr, arr[i])
                i = i + 1
            end
    end
    return final_arr
end    

function dir_reduc(arr)

    directions = Dict("NORTH" => 1, "SOUTH" => 1, "EAST" => 2, "WEST" => 2)
    opposites = ("NORTHSOUTH", "WESTEAST")
    
    
    aux_arr = []
    final_arr = arr
    while (true)
        final_arr = elim_dir(final_arr, directions, opposites)
        println(final_arr)
        if length(final_arr) <= 1
            return final_arr
        elseif aux_arr == final_arr
            return final_arr
        else
            aux_arr = final_arr
        end
    end
    final_arr

end



println(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH"]))

