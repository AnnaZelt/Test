def sumofdigits(num):
    #change to str
    str_num = str(num)
    #map the string into an int list
    mapped_num = map(int, str_num)
    separeted_num = list(mapped_num)
    res = 0
    #iterate over each element and combine them
    for n in separeted_num:
        res += n 
    return res

def ispal(num):
    #change to str
    str_num = str(num)
    #map the string into an int list
    mapped_num = map(int, str_num)
    separeted_num = list(mapped_num)
    pal = False
    #check if the list length is even or odd
    if (int(len(separeted_num)%2)) == 0:
        #create two separte lists, each half of separated_sum
        fwd = separeted_num[0:int(len(separeted_num)/2)].copy()
        bck = separeted_num[int(len(separeted_num)/2):int(len(separeted_num))].copy()
        bck.reverse()
        if fwd == bck:
            pal = True
    else:
        mid = int(len(separeted_num)-1)/2
        tmp_lst = separeted_num.copy()
        #remove the middle number in the list
        tmp_lst.pop(int(mid))
        fwd = tmp_lst[0:int(len(tmp_lst)/2)]
        bck = tmp_lst[int(len(tmp_lst)/2):int(len(tmp_lst))]
        bck.reverse()
        if fwd == bck:
            pal = True
    return(pal)
