from src.analysis import BOQAnalyzer
from src.exporter import export_to_word
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

import_folder = os.path.join(dir_path,'imports')

export_folder = os.path.join(dir_path,'exports')

#Lines Beginning with a # in Python are comments (or notes) so Python won't execute them 
#just like this one. I use them here to provide explanations for each line of code.


#Firstly, Let us set and get appropriate variables
analyzer = BOQAnalyzer()

unit = analyzer.default_unit
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
        analyzer.block_per_area(width, height, sn)
        
        print(f"{analyzer.results[sn-1][1]} blocks\n")
        #This will now display to the user the final value of block estimate gotten for this face.

        if(sn == faces):
            sn = 1
        else:
            sn = sn + 1
        #Next this will update the current value sn serial number to be used for the next loop i.e 1,2,3,4,5

        #End of code, Process restart again for the number of times passed into range function from the faces variable in line 14 

    total_faces, block_sum = analyzer.get_block_sum()
    #At this point, BlockList List have been created with block estimates for all the faces. We now sum up data in the list using the sum() function and now have the total sum in a new variable called grand_total

    print(f"Grand Total of {block_sum[0]} faces \nis: {block_sum[1]} blocks")
    #Now Show the User the Total Sum calculated with a custom note. Code Above will produce "Total of [200, 430, 1000, 20] Blocks is: 1450 block"

    printDoc = str(input("*******************************\nCreate Document? Y/N: "))

    if printDoc.upper() == 'Y':
    
        title = input("Document Title: ")
        filename = input("document filename: ")

        records = (analyzer.results)

        export = export_to_word(title, filename, import_folder, export_folder, records, block_sum[1])

        print(export)

    running = str(input("*******************************\nTry Again? Y/N: "))
    #Now we ask the user if he wants to try again? Remember that code will repeat as long as the variable running is 'y', 'Yes', 'Y' etc (as specified in line 12 above). When User types Y, code repeat for a new calculation while if user types any other value, code end
    
input("Thank you for using my app, Press ENTER to exit")
#After code ends, user is Appreciated for using the App and would be required to Press ENTER to finally exit the application
