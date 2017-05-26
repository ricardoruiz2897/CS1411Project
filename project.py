#Lab project#
#Ricardo Ruiz 501#

#file with operations to get qb pass rating in function 2 (see file in main folder)
import operations

#function 1
def part_1(file_name):
    list_ = []
    try:
        file_read = open(file_name,'r')
        
        #append elements to list
        for element in file_read:
            list_.append(element)

        #close file
        file_read.close()
            
        #call part two with list as an argument
        return(list_)
        
     ##if there is no file, tell the user   
    except FileNotFoundError:
        print('File not found')

#function 2
def part_2(list_):
    
    list_part2 = []
    temp_list = []
    temp_tuple = tuple()
    str_ = []
    rating = 0.0
    qb_name = ''

    #this for loop generates a list of tuples, each element of the list is a tuple with the QB name and it's rating [(name, rating)]
    for var in range(len(list_)):
        
        #avoid empty lists
        if len(list_[var]) > 1:
            
            #convert each element to a list
            str_ = list_[var].split()

            #get qb_name
            qb_name = str_[0] + ' ' + str_[1] 
        
            #get rating from the operations file (file need to be in the same folder)
            rating = operations.passing_rating(float(str_[-5]),float(str_[-4]),float(str_[-3]),float(str_[-2]),float(str_[-1]))

            #append to tuple
            temp_list.append(qb_name)
            temp_list.append(rating)
            temp_tuple = tuple(temp_list)

            #append to main list
            list_part2.append(temp_tuple)

            #clear tuple and qb_name for next iterarion
            temp_list = []
            temp_tuple = ()

    #return sorted_list
    return list_part2
    
#function 3
def part_3(list_part2):
    
    #sorting algorithm
    max_position = 0
     
    #rating is always the second element on tuple from list [var][1]
    for var in range(len(list_part2)-1):
        max_position = var
        for var_2 in range(max_position+1,len(list_part2)):
            if list_part2[var_2][1] < list_part2[max_position][1]:
                continue
            elif list_part2[var_2][1] > list_part2[max_position][1]:
                #sort the whole tuple
                list_part2[var_2],list_part2[max_position] =  list_part2[max_position],list_part2[var_2]

    #return as sorted list
    sorted_list = list_part2         
    return sorted_list

#funtion 4
def part_4(new_file_name,sorted_list):

    file_write = open(new_file_name,'w')

    #write in the file
    temp_list = []
    for element in sorted_list:
        #convert to list to avoid parenthesis
        temp_list = list(element)
        print(temp_list[1] , temp_list[0], file = file_write)

    file_write.close()
  
#funtion 5 main
def main():
    
    #check if functions have been done
    ispart1_completed = False
    ispart2_completed = False
    ispart3_completed = False
        
    menu = True
    while menu == True:
        try:
            #menu
            print('1.-Select input file\n2.-Calculate ratings\n3.-Sort ratings\n4.-Output ratings to a file\n' \
              '5.-Output ratings to console\n6.-Exit')
        
            menu_decision = int(input('Select: '))

            ###menu 1###
            if(menu_decision == 1):

                #ask for a file name a save returned list
                file_name = input('Give me the file name: ')
                ret_part1 =  part_1(file_name)

                #first option is completed
                ispart1_completed = True

                #let user know he is good to go
                print('\nFile name has been saved\n')

            ###menu 2###    
            elif(menu_decision == 2):

                #we can only do the second option if the first one is completed
                if ispart1_completed == False:
                    print('\nNo statistics have been read\b')
                
                else:
                    #create a list with what part 1 returns, this is the unsorted list of tuples
                    list_p2 = part_2(ret_part1)

                    #second option is completed
                    ispart2_completed = True

                    #let the user know he is good to go
                    print('\nRatings have been calculated\n')

            ###menu 3###       
            elif(menu_decision == 3):

                #we can only sort if we have the ratings
                if ispart2_completed == False:
                    print('\nNo ratings have been calculated\n')

                #Sort list by ratings
                else:
                    #sort list from part 2
                    sorted_list = part_3(list_p2)

                    #third option is completed
                    ispart3_completed = True
                    
                    #let the user know he is good to go
                    print('\nList has been sorted\n')
                    
                    
            ###menu 4###        
            elif(menu_decision == 4):

                #if there is no sorting or rating calculation
                if ispart3_completed == False or ispart2_completed == False:
                    print('\nYou have not sorted the elements or calculated the ratings\n')
                    
                else:
                    #prompt user for output name
                    output_filename = input('Give me the output file name: ')

                    #generate new file
                    part_4(output_filename,sorted_list)

                    #let the user know he is good to go
                    print('\nNew file has been created under main folder\n')

            ###menu 5###
            elif(menu_decision == 5):
                
                #if there is no sorting or rating calculation
                if ispart3_completed == False or ispart2_completed == False:
                    print('\nYou have not sorted the elements or calculated the ratings\n')

                #print directly to console
                else:
                    for element in sorted_list:

                        print(element[1], element[0], end='\n')

            ###menu 6###
            elif(menu_decision == 6):

                #get out of the loop
                menu = False

            ###invalid option###
            else:
                print('\nInvalid option\n')
                
        except ValueError:
            print('\nYour option must be an integer from 1 to 6\n')
            
main()










    
