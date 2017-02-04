def bin_to_int(val):
    """
        Convert the unsigned binary value to integer.
	    """
	        n=len(str(val))
		    if len(val)== 1:
		            return int(val)
			        else:
				        
					        return 2* bin_to_int(val[0:(len(val)-1)])+ int(val[len(val)-1])
						            
							    print bin_to_int("100101")
