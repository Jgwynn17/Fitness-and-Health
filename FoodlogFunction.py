
from datetime import date


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
            

            
                           
















                     
