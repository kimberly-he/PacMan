def selection_sort(lst, start, end):
    """
        A recursive version of the selection sort algorithm.
	    """
	        count = start
		    
		        if start == end:
			        return lst
				    else:
				            minumum = lst[count]
					            minpos = count
						            for i in range(count+1, end+1):
							                if lst[i] < minumum:
									                minumum = lst[i]
											                minpos = i
													        lst[count], lst[minpos] = lst[minpos], lst[count]
														        start += 1
															        selection_sort(lst, start, end)
																        return lst


