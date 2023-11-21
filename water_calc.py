class  Water_Calculator:
     
    def __init__(self, age, sex, weight, height activity_level):
        """Initialize the Calculator class."""
        self.age = age
        self.sex = sex.lower() 
        self.weight = weight
        self.height = height
        self.activity_level = activity_level.lower()  # 'inactive', 'lightly_active', 'moderately_active', 'very_active', 'extra_active'

    
    def user_data (self,age, sex, weight, height activity_level):
        """Collect user data .
         We need to collect age, sex, weight in punds, height in inches, activity level. The activity level optons are:
             sedentary, lightly active, moderatly active, very active, extra active"""


    def calc_BMR(self,age, sex, weight, height):
        """BMR is aBasal Metabolic Rate based off of the Harris-Benedict equation """
       
        if sex=="male":
            BMR_f= 66+(6.23(weight))+(12.7(height))-(6.8(age))
        
        elif sex== "female":
            BMR_m= 655+(4.35(weight))+ (4.7(height))-(4.7(age))
        else:
            raise ValueError("Invalid value for 'sex'. Please use 'male' or 'female'.")

    
    def adjust_for_activity_level(bmr, activity_level):
        # adjust BMR based off of how active you are
        activity_multipliers = {
        'inactive': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'extra_active': 1.9
        }

        if activity_level.lower() in activity_multipliers:
           TDEE=bmr * activity_multipliers[activity_level.lower()] # TDEE is total daily energy expenditure
        else:
            raise ValueError("Invalid value for 'activity_level'. Please use one of: 'inactive', 'lightly_active', 'moderately_active', 'very_active', 'extra_active'.")
    
    def final_intake(self, TDEE,):
        water_intake_oz= TDEE(0.5)
        water_intake_cups=water_intake_oz(0.125)
        print(" Your daily water goal is {water_intake_oz} ounces, or {water_intake_cups} cups!")
        


