#function for finding BMR of adult male
def maleBmr(weight, height, age):#pounds, inches, years
    weight = (int(weight) * 6.3)
    height = (int(height) * 12.9)
    age = (int(age) * 6.8)
    calculation = ((66 + weight) + (height) - age)
    return (round(calculation, 2))




def femaleBmr(weight, height, age):#pounds, inches, years
    weight = (int(weight) * 4.3)
    height = (int(height) * 4.7)
    age = (int(age) * 4.7)
    calculation = ((655 + weight) + (height) - age)
    return (round(calculation, 2))




#this function gathers all necessary information from the user 
def gender():
    weight = int(input("Please enter your weight(pounds): "))#pounds
    height = int(input("Please enter your height(inches): "))#inches
    age = int(input("Please enter your age(years): "))#years
    gender_choice = input("Please enter whether you are a female or male: ")
    if gender_choice == "male" or gender_choice == "Male":
        male = maleBmr(weight, height, age)
        activity_level = int(input("How many days a week do you exercise: "))
        if activity_level == 0:
            maintenence = (male * 1.2)
            return int(maintenence)
        if activity_level >= 1 and activity_level <= 2:
            maintenence = (male * 1.375)
            return int(maintenence)
        if activity_level >= 3 and activity_level <=5:
            maintenence = (male * 1.55)
            return int(maintenence)
        if activity_level >= 6 and activity_level <= 7:
            maintenence = (male * 1.725)
            return int(maintenence)
    if gender_choice == "female" or gender_choice == "Female":
        female = femaleBmr(weight, height, age)
        activity_level = int(input("How many days a week do you exercise: "))
        if activity_level == 0:
            maintenence = (female * 1.2)
            return int(maintenence)
        if activity_level >= 1 and activity_level <= 2:
            maintenence = (female * 1.375)
            return int(maintenence)
        if activity_level >= 3 and activity_level <=5:
            maintenence = (female * 1.55)
            return int(maintenence)
        if activity_level >= 6 and activity_level <= 7:
            maintenence = (female * 1.725)
            return int(maintenence)
        


