def ips_between(start, end):
    start_split = start.split('.')
    end_split = end.split('.')

    difference = []
    for s,e in reversed(list(zip(start_split,end_split))):
        dif_aux = int(e)-int(s)
        difference.append(dif_aux)

    ips = 0
    for index, value in enumerate(difference):
        ips += value*pow(256,index)

    return ips




# print(ips_between("10.0.0.0", "10.0.0.50"))#, 50))
print(ips_between("20.0.0.10", "20.0.1.0"))#, 246))
