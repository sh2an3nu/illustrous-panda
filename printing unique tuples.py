lis = [(1,2),(2,1),(3,3),(4,3)]
result = set()
some_list_to_get_answer = [result.add((a,b)) for (a,b) in lis if(a,b) and (b,a) not in result]
print("List after removing duplicates: ",str(list(result)))