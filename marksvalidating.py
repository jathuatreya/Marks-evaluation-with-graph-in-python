# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# My name is jathushan Varnakulasingam
# Date: 11/12/2023


#importing library
from graphics import *


#define values for global variable into the functions
total_count_progresser = total_count_trailer = total_count_exclude = total_count_retriver = 0  #these are for counting total for creating histogram
pass_credit = defer_credit = fail_credit = 0        #define input values are 0 becaose of it will creating a list
i = 0  #variable for total_count list printing   indexing other lists



#creating empty string
result=""     #because 


#creating boolean variables
is_pass_credit_valid = is_defer_credit_valid = is_fail_credit_valid = True


#creating empty lists for storing value
# for create list and print a value in terminal after press q
result_list=[]
pass_credit_list=[]
defer_credit_list=[]
fail_credit_list=[]
total_count=[]

#file creating 
def file_creating():
 file = open("student results.txt", 'w')
 file.write("part 3")
 for x in total_count :
  file.write(f'\n{result_list[x]} - {pass_credit_list[x]},{defer_credit_list[x]},{fail_credit_list[x]} ')
 file.close() 

def credit_validating():  #main part of the program which validating entered number
   try : # if any other charector than integer it will show interger required
        global pass_credit,defer_credit,fail_credit
        global is_pass_credit_valid,is_defer_credit_valid,is_fail_credit_valid #ordering list form 0 to n numbers of input
        global total_count_progresser,total_count_trailer,total_count_exclude,total_count_retriver,result,i    #converting local variable to global variable for assign all value equal to use other functions
        
       #pass_crdeit validation for out of range
        pass_credit = int(input("Enter the Pass credit : "))
        if 0 > pass_credit or pass_credit > 120 or (pass_credit % 20) != 0:
            print ('Out of range')
            is_pass_credit_valid = False
            recalling()

        else:
            is_pass_credit_valid = True   #if the value is perfect then the value is_pass_credit_valid is true
            
        if is_pass_credit_valid == True:
    #defer_credit validation for out of range                
            defer_credit=int(input("Enter the Defer credit :" ))
            if 0 > defer_credit or defer_credit > 120 or (defer_credit % 20) != 0:
                print ('Out of range')
                is_defer_credit_valid = False
                recalling()
        
            else:
                    is_defer_credit_valid = True   
                    
        if is_defer_credit_valid == True:
    #fail_credit validation for out of range                       
            fail_credit=int(input("Enter the Fail credit :" ))
            if 0 > fail_credit or fail_credit > 120 or (fail_credit % 20) != 0:
                print ('Out of range')
                is_fail_credit_valid = False
                recalling()
        
            else:
                 is_fail_credit_valid = True   
            
            #checking  total = 120
            
        if is_fail_credit_valid== True:
             Total_credit = pass_credit + defer_credit + fail_credit  # calculate the total = 120
             if Total_credit !=120:
              print("Total incorrect")
              recalling()

        processing_result()      


   except ValueError : 
             print("Integer Required")
             recalling()
                                           
def processing_result():    #checking result for validating marks
        global total_count_progresser,total_count_trailer,total_count_exclude,total_count_retriver,result,i    #converting local variable to global variable for assign all value equal to use other functions
        if pass_credit == 120:
            total_count_progresser += 1
            result ="Progress"
            print(result)
            creating_list()
            i+=1
            file_creating()
            recalling()
            
            
        elif pass_credit == 100 and (defer_credit or fail_credit) == 20:
                total_count_trailer += 1
                result ="Progress (module trailer)"
                print(result)
                creating_list()
                i+=1
                file_creating()
                recalling()
                
                
        elif fail_credit >= 80:
                total_count_exclude += 1
                result ="Exclude"
                print(result)
                creating_list()
                i+=1
                file_creating()
                recalling()
                
                
        else:
                total_count_retriver += 1
                result ="Module retriever"
                print("Module retriever")
                creating_list()
                i+=1
                file_creating()
                recalling()
                
           
        
def recalling():  #ask to input another input                 
  After_choice = input("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view ressults : ") 
  if After_choice == "y": 
    credit_validating()
  elif After_choice == "q":
      printing_list()
      histogram()
      file.close()
      
  else:
       recalling()

def creating_list():    # this will create a list part 2 question
    total_count.append(i)
    result_list.append(result)
    pass_credit_list.append(pass_credit)
    defer_credit_list.append(defer_credit)
    fail_credit_list.append(fail_credit)
       
def printing_list ():  #print a list in terminal  after press q  for part 2 question
  global total_count
  print(" \n " )
  print("part 2")
  for x in total_count :
   print(f'{result_list[x]} - {pass_credit_list[x]},{defer_credit_list[x]},{fail_credit_list[x]}')

def histogram():   #create histogram
    counts=[total_count_progresser,total_count_trailer,total_count_exclude,total_count_retriver]
    # Create a window for the histogram
    win = GraphWin("Histogram", 400, 300)
    win.setBackground("white")

    # Define the categories, corresponding counts, and colors
    categories = ["Progresser", "Trailer", "Exclude", "Retriver"]
    colors = ["#aef8a0","#a0c689","#a8be77","#d1b6b4"]   
    

    # Draw bars in the window
    for i, category in enumerate(categories):
        bar = Rectangle(Point(i * 80, 300), Point((i + 1) * 80, 300 - counts[i] * 10))
        bar.setFill(colors[i])  # Set fill color for the bar
        bar.draw(win)

        text = Text(Point((i + 0.5) * 80, 280), f"{category}\n{counts[i]} ")
        text.setSize(10)
        text.draw(win)

    win.getMouse()
    win.close()
  
      
              
             
credit_validating()
