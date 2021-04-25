from datetime import date


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

            #calculates maintenence calories based off of activity level
            
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



                    



def foodlog():

    filename = input("What file would you like to create/open: ")
    with open(filename, "a+") as file:
        
        #Add data to file
        today = date.today()
        today_line = str(today) + "\n"
        file.write(today_line)
        file.write("\n")

        #What meal
        meal_number = input("What meal are you logging: ") + "\n"
        meal_title = "Meal: " + str(meal_number) + "\n"
        file.write(meal_title)
        file.write("\n")
        file.write("Food" + "\t" * 5 + "Calories" + "\t" + "Protein" + "\t" + "Carbs" + "\t" + "Fats" + "\n")
        file.write("\n")

        meal_total = 0
        protein_meal_total = 0
        carbs_meal_total = 0
        fats_meal_total = 0
        
        #Add Food
        done = False
        while not done:

            #Logging the food
            food = input("Please enter the name of the food: ")
            calories = float(input("How many calories per serving: "))
            serving_size = float(input("How many servings of the food: "))

            #Logging Macros
            macros = False
            while not macros:
                macros = input("Would you like to add the Macros of the food(i.e. Proteins, Fats, Carbs)? yes/no? ")

                if macros == "Yes" or macros == "yes":
                    #Calculating Macros per serving
                    proteins = float(input("How many grams of Protein per Serving: "))
                    protein_total = proteins * serving_size
                    protein_meal_total += protein_total
                    carbs = float(input("How many grams of Carbs per Serving: "))
                    carb_total = carbs * serving_size
                    carbs_meal_total += carb_total
                    fats = float(input("How many grams of Fats per Serving: "))
                    fat_total = fats * serving_size
                    fats_meal_total += fat_total
                    macros = True
                    
                elif macros == "No" or macros == "no":
                    macros = True
                    


            #Calculations and writing to the file
            serving = calories * serving_size

            #Spacing of indents 
            if len(food) > 16:
                food_line = str(food) + "\t" * 3 + str(serving) + "\t" * 2 + str(protein_total) + "\t" + str(carb_total) + "\t" + str(fat_total) + "\n"
                
            if len(food) > 8 and len(food) < 16:
                food_line = str(food) + "\t" * 4 + str(serving) + "\t" * 2 + str(protein_total) + "\t" + str(carb_total) + "\t" + str(fat_total) + "\n"
                
            else:
                food_line = str(food) + "\t" * 5 + str(serving) + "\t" * 2 + str(protein_total) + "\t" + str(carb_total) + "\t" + str(fat_total) + "\n"
                
            file.write(food_line)
            file.write("\n")

            #Total calories for the meal
            meal_total += serving
        
            
            #Would you like to add more food to the meal
            more = False
            while not more:
                more = input("Would you like to enter more food (yes/no). ")
                
                if more == "no" or more == "No":
                    file.write("-" * 100 + "\n")
                    total_meal_calories = "Total Calories For Meal: " + str(meal_total) + "\n"
                    total_meal_macros = "Total Protein For Meal: " + str(protein_meal_total) + "\t" + "Total Carbs For Meal: " + str(carbs_meal_total) + "\t" + "Total Fats For Meal: " + str(fats_meal_total)
                    file.write(total_meal_calories)
                    file.write(total_meal_macros)
                    file.write("-" * 100 + "\n")
                    done = True
                    
                elif more == "yes" or more == "Yes":
                    more = True

            

foodlog()
            

    
        

        


