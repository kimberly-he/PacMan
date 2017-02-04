# appreciate for reading my long and complicated code,hope the comment can give some help^^
# I basically delete the None direction, since I don't want my ghost just stupid stay some place,at least it should move


from cmptman import *
import random
road = []
board = []

# algorithm 1
def initialized_direction():
    raw = cmpt.allContents()
        global road
	    global board
	        w,h = cmpt.boardSize()
		    directions = [N,S,W,E]
		        n = 0

			    for i in range (w):                             #copy the content of the board into a 2-D matrix
			            board.append([])
				        
					        for j in range(h):
						            c = 0
							                cpy = [N,S,W,E]
									            n = (h*j + i)
										                board[i].append(raw[n])
												            n += 1
													        print   board
														        
															    n = 0        
															        for i in range (w):                                                         
																        road.append([])
																	        for j in range(h):
																		            c = 0
																			                cpy = [N,S,W,E]
																					            road[i].append([])

																						                n += 1
																								        
																									            if board[i][j] == BLOCK:                                #When there is a block on the coordinate
																										                    road[i][j] = [None]

																												                else:
																														                if (j - 1) < 0:                                         #Check for the edge of the board
																																                    del cpy[0]
																																		                        c+=1
																																					                if (j + 2) > h:
																																							                    del cpy[1 - c]
																																									                        c+=1
																																												                if (i - 1) < 0:
																																														                    del cpy[2 - c]
																																																                        c+=1
																																																			                if (i + 2) > w:
																																																					                    del cpy[3 - c]
																																																							                    if len(cpy) != 4:                                       #If on the edge
																																																									                        counter = 0
																																																												                
																																																														                    if cpy[counter] == N:
																																																																                                
																																																																				                        if board[i][j-1] == BLOCK:

																																																																							                            del cpy[counter]

																																																																										                            elif counter < (len(cpy)-1):

																																																																													                                counter += 1
																																																																																	                        if counter > (len(cpy)-1):

																																																																																				                            counter -= 1

																																																																																							                        if cpy[counter] == S:

																																																																																										                        if board[i][j+1] == BLOCK:

																																																																																													                            del cpy[counter]

																																																																																																                            elif counter < (len(cpy)-1):

																																																																																																			                                counter += 1
																																																																																																							                        if counter > (len(cpy)-1):

																																																																																																										                            counter -= 1

																																																																																																													                        if cpy[counter] == W:

																																																																																																																                        if board[i-1][j] == BLOCK:

																																																																																																																			                            del cpy[counter]
																																																																																																																						                            elif counter < (len(cpy)-1):

																																																																																																																									                                counter += 1
																																																																																																																													                        if counter > (len(cpy)-1):

																																																																																																																																                            counter -= 1
																																																																																																																																			                   
																																																																																																																																					                       if cpy[counter] == E:

																																																																																																																																							                         
																																																																																																																																										                         
																																																																																																																																													                         if board[i+1][j] == BLOCK:

																																																																																																																																																                             del cpy[counter]
																																																																																																																																																			                             elif counter < (len(cpy)-1):

																																																																																																																																																						                                 counter += 1
																																																																																																																																																										               

																																																																																																																																																											                           road[i][j] = cpy
																																																																																																																																																														           
																																																																																																																																																															                   else:                                                   #If not on the edge

																																																																																																																																																																	                       templist = []

																																																																																																																																																																			                           counter = 0
																																																																																																																																																																						                   
																																																																																																																																																																								                       if cpy[counter] == N:
																																																																																																																																																																										                               
																																																																																																																																																																													                               if board[i][j-1] == BLOCK:

																																																																																																																																																																																                                   del cpy[counter]

																																																																																																																																																																																				                           elif counter < (len(cpy)-1):

																																																																																																																																																																																							                               counter += 1
																																																																																																																																																																																										                               if counter > (len(cpy)-1):

																																																																																																																																																																																													                                   counter -= 1

																																																																																																																																																																																																	                      
																																																																																																																																																																																																			                          if cpy[counter] == S:

																																																																																																																																																																																																						                          if board[i][j+1] == BLOCK:

																																																																																																																																																																																																									                              del cpy[counter]

																																																																																																																																																																																																												                              elif counter < (len(cpy)-1):

																																																																																																																																																																																																															                                  counter += 1
																																																																																																																																																																																																																			                          if counter > (len(cpy)-1):

																																																																																																																																																																																																																						                              counter -= 1


																																																																																																																																																																																																																									                          if cpy[counter] == W:

																																																																																																																																																																																																																												                          if board[i-1][j] == BLOCK:

																																																																																																																																																																																																																															                              del cpy[counter]
																																																																																																																																																																																																																																		                              elif counter < (len(cpy)-1):

																																																																																																																																																																																																																																					                                  counter += 1
																																																																																																																																																																																																																																									                          if counter > (len(cpy)-1):

																																																																																																																																																																																																																																												                              counter -= 1
																																																																																																																																																																																																																																															                     
																																																																																																																																																																																																																																																	                         if cpy[counter] == E:
																																																																																																																																																																																																																																																				     
																																																																																																																																																																																																																																																				                             if board[i+1][j] == BLOCK:

																																																																																																																																																																																																																																																							                                 del cpy[counter]
																																																																																																																																																																																																																																																											                         elif counter < (len(cpy)-1):

																																																																																																																																																																																																																																																														                             counter += 1

																																																																																																																																																																																																																																																																	                         road[i][j] = cpy        
																																																																																																																																																																																																																																																																				 # the most basic part - initialized direction of the ghosts corresponding to their position
																																																																																																																																																																																																																																																																				 # i,e. the N is out of board,W is BLOCK,so the initialized direction of this point is [S,E]
																																																																																																																																																																																																																																																																				 # the global list - road stores all initialized direction of ghosts corresponding to postion

																																																																																																																																																																																																																																																																				         
																																																																																																																																																																																																																																																																					 # algorithm 2
																																																																																																																																																																																																																																																																					 def linear_chase(g):
																																																																																																																																																																																																																																																																					     """
																																																																																																																																																																																																																																																																					         Find the linear distance between the ghost and CMPTman.
																																																																																																																																																																																																																																																																						     """
																																																																																																																																																																																																																																																																						         lon=[]

																																																																																																																																																																																																																																																																							     x,y= cmpt.currentPosition()

																																																																																																																																																																																																																																																																							         pos= cmpt.ghostPositions()
																																																																																																																																																																																																																																																																								     j,k= pos[g]
																																																																																																																																																																																																																																																																								         w,h= cmpt.boardSize()
																																																																																																																																																																																																																																																																									     global n_ghosts

																																																																																																																																																																																																																																																																									         for i in range(n_ghosts):

																																																																																																																																																																																																																																																																										         if  g != i:

																																																																																																																																																																																																																																																																											             if pos[g] == pos[i]:

																																																																																																																																																																																																																																																																												                     return random_chase(g)  # in case ghosts move together, use random-chase to separate them when ghosts in same position
																																																																																																																																																																																																																																																																														                 

																																																																																																																																																																																																																																																																																     for i in range(len(road[j][k])):

																																																																																																																																																																																																																																																																																             if str(road[j][k][i])== "N":
																																																																																																																																																																																																																																																																																	                 dis= (j-x)*(j-x)+ (k-1-y)*(k-1-y)
																																																																																																																																																																																																																																																																																			             lon.append(dis)
																																																																																																																																																																																																																																																																																				             if str(road[j][k][i])== "S":
																																																																																																																																																																																																																																																																																					                 dis= (j-x)*(j-x)+ (k+1-y)*(k+1-y)
																																																																																																																																																																																																																																																																																							             lon.append(dis)
																																																																																																																																																																																																																																																																																								             if str(road[j][k][i])== "W":
																																																																																																																																																																																																																																																																																									                 dis= (j-1-x)*(j-1-x)+ (k-y)*(k-y)
																																																																																																																																																																																																																																																																																											             lon.append(dis)
																																																																																																																																																																																																																																																																																												             if str(road[j][k][i])== "E":
																																																																																																																																																																																																																																																																																													                 dis= (j+1-x)*(j+1-x)+ (k-y)*(k-y)
																																																																																																																																																																																																																																																																																															             lon.append(dis)

																																																																																																																																																																																																																																																																																																             
																																																																																																																																																																																																																																																																																																	         
																																																																																																																																																																																																																																																																																																		     d=road[j][k]
																																																																																																																																																																																																																																																																																																		         cpy=lon[:]
																																																																																																																																																																																																																																																																																																			     cpy.sort()
																																																																																																																																																																																																																																																																																																			         
																																																																																																																																																																																																																																																																																																				     for pos in range(len(lon)):
																																																																																																																																																																																																																																																																																																				             if cpy[0]== lon[pos]:
																																																																																																																																																																																																																																																																																																					                 return d[pos]
																																																																																																																																																																																																																																																																																																							         
																																																																																																																																																																																																																																																																																																								 # calculate the possible directions after initialized_direction ,return the linear distance of ghost and CMPTman
																																																																																																																																																																																																																																																																																																								 # compare the distance,sort it and find the shortest one


																																																																																																																																																																																																																																																																																																								 # algorithm 3 
																																																																																																																																																																																																																																																																																																								 def random_chase(g):
																																																																																																																																																																																																																																																																																																								     """
																																																																																																																																																																																																																																																																																																								         Chase the CMPTman is a random order from [N,S,W,E], end when CMPTman and the ghost are very close.
																																																																																																																																																																																																																																																																																																									     And transfer to linear_chase mode.
																																																																																																																																																																																																																																																																																																									         Run only have more than two ghosts.
																																																																																																																																																																																																																																																																																																										     """
																																																																																																																																																																																																																																																																																																										         
																																																																																																																																																																																																																																																																																																											     x,y= cmpt.currentPosition()
																																																																																																																																																																																																																																																																																																											         
																																																																																																																																																																																																																																																																																																												     pos= cmpt.ghostPositions()
																																																																																																																																																																																																																																																																																																												         j,k= pos[g]
																																																																																																																																																																																																																																																																																																													     lst=[N,S,W,E]
																																																																																																																																																																																																																																																																																																													         c = 0
																																																																																																																																																																																																																																																																																																														     if (x-j)*(x-j)+(y-k)*(y-k)>6:    # 6 doesn't have special meaning, I just want to choose numbers indicate CMPTman and ghost are close

																																																																																																																																																																																																																																																																																																														             lst = road[j][k]
																																																																																																																																																																																																																																																																																																															             
																																																																																																																																																																																																																																																																																																																             
																																																																																																																																																																																																																																																																																																																	             d = random.choice(lst)
																																																																																																																																																																																																																																																																																																																		             return d
																																																																																																																																																																																																																																																																																																																			         else:
																																																																																																																																																																																																																																																																																																																				         return linear_chase(g)
																																																																																																																																																																																																																																																																																																																					 # the original direction list is[N,S,W,E],we delete the corresponding direction when ghost run into BLOCK or out of testboard
																																																																																																																																																																																																																																																																																																																					 # pick random direction from the possible direction list
																																																																																																																																																																																																																																																																																																																					 # when they are close(<6), choose the linear_chase mode




																																																																																																																																																																																																																																																																																																																					     
																																																																																																																																																																																																																																																																																																																					     # create the game
																																																																																																																																																																																																																																																																																																																					     cmpt = CMPTman(testboard=12)
																																																																																																																																																																																																																																																																																																																					     w,h= cmpt.boardSize()
																																																																																																																																																																																																																																																																																																																					     n_ghosts = len(cmpt.ghostPositions())
																																																																																																																																																																																																																																																																																																																					     initialized_direction()
																																																																																																																																																																																																																																																																																																																					     # play turns until the game is over
																																																																																																																																																																																																																																																																																																																					     while cmpt.playing():
																																																																																																																																																																																																																																																																																																																					         directions = []
																																																																																																																																																																																																																																																																																																																						     if n_ghosts<= 2:
																																																																																																																																																																																																																																																																																																																						             
																																																																																																																																																																																																																																																																																																																							             for g in range(n_ghosts):
																																																																																																																																																																																																																																																																																																																								                 
																																																																																																																																																																																																																																																																																																																										             d = linear_chase(g)
																																																																																																																																																																																																																																																																																																																											         
																																																																																																																																																																																																																																																																																																																												             directions.append(d)
																																																																																																																																																																																																																																																																																																																													         else:
																																																																																																																																																																																																																																																																																																																														         for g in range(n_ghosts-1):
																																																																																																																																																																																																																																																																																																																															         
																																																																																																																																																																																																																																																																																																																																             d = linear_chase(g)
																																																																																																																																																																																																																																																																																																																																	         
																																																																																																																																																																																																																																																																																																																																		             directions.append(d)
																																																																																																																																																																																																																																																																																																																																			             
																																																																																																																																																																																																																																																																																																																																				             d= random_chase(n_ghosts-1)
																																																																																																																																																																																																																																																																																																																																					             directions.append(d)
																																																																																																																																																																																																																																																																																																																																						     # the random mode only run when we have more than two ghosts since somehow it looks stupid
																																																																																																																																																																																																																																																																																																																																						     # so,<=2ghosts, ghosts just do linear_chase
																																																																																																																																																																																																																																																																																																																																						     # >2 ghosts, one ghost will go randome dorection,others still linear_chase

																																																																																																																																																																																																																																																																																																																																						                 
																																																																																																																																																																																																																																																																																																																																								     print "CMPTman is at:", cmpt.currentPosition()
																																																																																																																																																																																																																																																																																																																																								         print "Dots left:", cmpt.dotsLeft()
																																																																																																																																																																																																																																																																																																																																									     print "Moving ghosts:", directions

																																																																																																																																																																																																																																																																																																																																									         # move the ghosts and wait for CMPTman to play
																																																																																																																																																																																																																																																																																																																																										     cmpt.moveGhosts(directions)
