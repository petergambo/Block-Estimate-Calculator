#Lines Beginning with a # in Python are comments (or notes) so Python won't execute them 
#just like this one. I use them here to provide explanations for each line of code.


#Firstly, Let us set and get appropriate variables
unit = str("mm")
blocksList = []
sn = 1
running = 'y'

while running == 'y' or running == 'Y' or running == 'yes' or running == 'Yes' or running == 'YES' or running == 'yES' or running == 'yeS':
#Keep App Running unless user changes the value of y at the end of each calculation    
    faces = int(input("\n> Number of Total Wall Areas to Compute?: "))
    for i in range(faces):
        height = int(input(f"---Height of Face {sn} ({unit}): ")) 
        width = int(input(f"---Length of Face {sn} ({unit}): "))
        #Codes Above Shows "Height of Face 1 (mm)", "Length of Face 2 (mm)" etc to user and creates the height and width variable
    
        blocks = ((width/1000) * (height/1000)) * 10 
        #This line then converts the width and height from mm to metre then calculates the area (in metre square) of face. Then * 10 to get the sancrede block estimate for the face

        single_total = round(blocks, 2)  
        #This line then round the block estimate values to 2 decimal places

        blocksList.append(single_total)
        #This will then add calculated data stored in single_total to the blockList declared at the beginning

        if(sn == faces):
            sn = 1
        else:
            sn = sn + 1
        #Next this will update the current value sn serial number to be used for the next loop i.e 1,2,3,4,5

        print(f"{single_total} blocks\n")
        #This will now display to the user the final value of block estimate gotten for this face.

        #End of code, Process restart again for the number of times passed into range function from the faces variable in line 14 

    grand_total = sum(blocksList)
    #At this point, BlockList List have been created with block estimates for all the faces. We now sum up data in the list using the sum() function and now have the total sum in a new variable called grand_total

    print(f"Grand Total of {blocksList} Blocks\nis: {grand_total} blocks")
    #Now Show the User the Total Sum calculated with a custom note. Code Above will produce "Total of [200, 430, 1000, 20] Blocks is: 1450 block"

    running = str(input("*******************************\nTry Again? Y/N: "))
    #Now we ask the user if he wants to try again? Remember that code will repeat as long as the variable running is 'y', 'Yes', 'Y' etc (as specified in line 12 above). When User types Y, code repeat for a new calculation while if user types any other value, code end
    
input("Thank you for using my app, Press ENTER to exit")
#After code ends, user is Appreciated for using the App and would be required to Press ENTER to finally exit the application
