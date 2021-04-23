


#function for finding BMR of adult male
def maleBmr(weight, height, age):#pounds, inches, years
    weight = (int(weight) * 6.3)
    height = (int(height) * 12.9)
    age = (int(age) * 6.8)
    calculation = ((66 + weight) + (height) - age)
    return (round(calculation, 2))



#function for finding female BMR 
def femaleBmr(weight, height, age):#pounds, inches, years
    weight = (int(weight) * 4.3)
    height = (int(height) * 4.7)
    age = (int(age) * 4.7)
    calculation = ((655 + weight) + (height) - age)
    return (round(calculation, 2))





#this function gathers all necessary information from the user 
def calorieFinder():
     
    weight = int(input("Please enter your weight(pounds): "))#pounds
    height = int(input("Please enter your height(inches): "))#inches
    age = int(input("Please enter your age(years): "))#years
    
    
    value = False 
    
    
    """
       Finding general information about the user
    """


    while not value:
        gender_choice = input("Please enter if you are a male or female: ")#asks the user for their gender
        
        if gender_choice == "male" or gender_choice == "Male":
        
            male = maleBmr(weight, height, age)
        
            activity_level = int(input("How many days a week do you exercise: "))
            
            if activity_level == 0:
                maintenence = int(male * 1.2)
                final_calories = input("Do you want to lose, gain, or maintain weight?: ")
    
                if final_calories == "lose" or final_calories == "Lose":
                    maintenence -= 500
                    print(maintenence, "is your calories in order to lose weight")
                    value = True
                    
                if final_calories == "gain" or final_calories == "Gain":
                    maintenence += 500
                    print(maintenence, "is your calories in order to gain weight")
                    value = True 

        
                if final_calories == "maintain" or final_calories == "Maintain":
                    print(maintenence, "is your calories in order to maintain weight")
                    value = True
                    
             


            if activity_level >= 1 and activity_level <= 2:
                maintenence = int(male * 1.375)
            
            
                final_calories = input("Do you want to lose, gain, or maintain weight?: ")
    
                if final_calories == "lose" or final_calories == "Lose":
                    maintenence -= 500
                    print(maintenence, "is your calories in order to lose weight")
                    value = True 
        
                if final_calories == "gain" or final_calories == "Gain":
                    maintenence += 500
                    print(maintenence, "is your calories in order to gain weight")
                    value = True 
        
                if final_calories == "maintain" or final_calories == "Maintain":
                    print(maintenence, "is your calories in order to maintain weight")
                    value = True
                    
             
            
            if activity_level >= 3 and activity_level <=5:
                maintenence = int(male * 1.55)

                final_calories = input("Do you want to lose, gain, or maintain weight?: ")
    
                if final_calories == "lose" or final_calories == "Lose":
                    maintenence -= 500
                    print(maintenence, "is your calories in order to lose weight")
                    value = True 
        
                if final_calories == "gain" or final_calories == "Gain":
                    maintenence += 500
                    print(maintenence, "is your calories in order to gain weight")
                    value = True 
        
                if final_calories == "maintain" or final_calories == "Maintain":
                    print(maintenence, "is your calories in order to maintain weight")
                    value = True
                    
             
           
            if activity_level >= 6 and activity_level <= 7:
                maintenence = int(male * 1.725)
            
            
                final_calories = input("Do you want to lose, gain, or maintain weight?: ")
    
                if final_calories == "lose" or final_calories == "Lose":
                    maintenence -= 500
                    print(maintenence, "is your calories in order to lose weight")
                    value = True
        
                if final_calories == "gain" or final_calories == "Gain":
                    maintenence += 500
                    print(maintenence, "is your calories in order to gain weight")
                    value = True 
        
                if final_calories == "maintain" or final_calories == "Maintain":
                    print(maintenence, "is your calories in order to maintain weight")
                    value = True 
                        

            
        
        if gender_choice == "female" or gender_choice == "Female":
        
            female = femaleBmr(weight, height, age)
        
            activity_level = int(input("How many days a week do you exercise: "))
        
            if activity_level == 0:

                maintenence = int(female * 1.2)

            
                final_calories = input("Do you want to lose, gain, or maintain weight?: ")
            
    
                if final_calories == "lose" or final_calories == "Lose":
                    maintenence -= 500
                    print(maintenence, "is your calories in order to lose weight")
                    value = True
        
                if final_calories == "gain" or final_calories == "Gain":
                    maintenence += 500
                    print(maintenence, "is your calories in order to gain weight")
                    value = True
        
                if final_calories == "maintain" or final_calories == "Maintain":
                    print(maintenence, "is your calories in order to maintain weight")
                    value = True
                    
            
        
            if activity_level >= 1 and activity_level <= 2:

                maintenence = int(female * 1.375)


            
                final_calories = input("Do you want to lose, gain, or maintain weight?: ")
    
                if final_calories == "lose" or final_calories == "Lose":
                    maintenence -= 500
                    print(maintenence, "is your calories in order to lose weight")
                    value = True
        
                if final_calories == "gain" or final_calories == "Gain":
                    maintenence += 500
                    print(maintenence, "is your calories in order to gain weight")
                    value = True
        
                if final_calories == "maintain" or final_calories == "Maintain":
                    print(maintenence, "is your calories in order to maintain weight")
                    value = True

            
        
            if activity_level >= 3 and activity_level <=5:

                maintenence = int(female * 1.55)

            
                final_calories = input("Do you want to lose, gain, or maintain weight?: ")
    
                if final_calories == "lose" or final_calories == "Lose":
                    maintenence -= 500
                    print(maintenence, "is your calories in order to lose weight")
                    value = True
        
                if final_calories == "gain" or final_calories == "Gain":
                    maintenence += 500
                    print(maintenence, "is your calories in order to gain weight")
                    value = True
        
                if final_calories == "maintain" or final_calories == "Maintain":
                    print(maintenence, "is your calories in order to maintain weight")
                    value = True

        
            if activity_level >= 6 and activity_level <= 7:
                maintenence = int(female * 1.725)

            
                final_calories = input("Do you want to lose, gain, or maintain weight?: ")
    
                if final_calories == "lose" or final_calories == "Lose":
                    maintenence -= 500
                    print(maintenence, "is your calories in order to lose weight")
                    value = True
        
                if final_calories == "gain" or final_calories == "Gain":
                    maintenence += 500
                    print(maintenence, "is your calories in order to gain weight")
                    value = True
        
                if final_calories == "maintain" or final_calories == "Maintain":
                    print(maintenence, "is your calories in order to maintain weight")
                    value = True
        else:
            print("Please enter your gender: male or female ")
    return gender_choice       
    
calorieFinder()
    
        

        


