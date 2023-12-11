# 326-Final-Project

class  Water_Calculator():

    def __init__(self):
        """Initialize the Calculator class."""
        self.get_user_input()
        self.bmr = None
        self.TDEE = None

    def get_user_input(self):
        """Get user input for age, sex, weight, height, and activity level."""
        self.age = int(input("Enter your age: "))
        self.sex = input("Enter your sex (m/f): ").lower()
        self.weight = float(input("Enter your weight in pounds: "))
        self.height = float(input("Enter your height in inches: "))
        self.activity_level = int(input("Enter your activity level from 1-5: "))

    '''def get_user_input(self):
        """Get user input for age, sex, weight, height, and activity level."""
        self.age = simpledialog.askinteger("Input", "Enter your age: ")
        self.sex = simpledialog.askstring("Input", "Enter your sex (m/f): ").lower()
        self.weight = simpledialog.askfloat("Input", "Enter your weight in pounds: ")
        self.height = simpledialog.askfloat("Input", "Enter your height in inches: ")
        self.activity_level = simpledialog.askinteger("Input", "Enter your activity level from 1-5: ")
    '''

    def calc_BMR(self):
        """Calculate BMR based on the Harris-Benedict equation."""
        if self.sex == "m":
            self.bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
        elif self.sex == "f":
            self.bmr = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age)
        else:
            raise ValueError("Invalid value for 'sex'. Please use 'm' or 'f'.")
        return self.bmr

    def adjust_for_activity_level(self):
        """Adjust BMR based on the user's activity level."""
        activity_multipliers = {
            1: 1.2,
            2: 1.375,
            3: 1.55,
            4: 1.725,
            5: 1.9
        }

        if self.activity_level in activity_multipliers:
            self.TDEE = self.bmr * activity_multipliers[self.activity_level]
        else:
            raise ValueError("Invalid value for 'activity_level'. Please use values 1-5.")
        return self.TDEE

    def final_intake(self):
        """Calculate and print the final water intake."""
        water_intake_oz = self.TDEE * 0.03
        water_intake_cups = water_intake_oz * 0.125
        print(f"Your daily water goal is {water_intake_oz:.2f} ounces, or {water_intake_cups:.2f} cups!")



calculator = Water_Calculator()
calculator.calc_BMR()
calculator.adjust_for_activity_level()
calculator.final_intake()



class WaterTracker:
  class WaterTracker(Water_Calculator):
    def __init__(self, water_goal):
        """Initialize the WaterTracker class."""
        self.water_goal = water_goal
      

    def check_water_intake(water_goal):
        """
        Check the water intake for the user.

        Parameters:
        water_intake (float): The target water intake for the user.
        """
        # Initialize the user's water intake to zero
        user_water_intake = 0
        # Loop until the user's water intake is equal or greater than the target water intake
        while user_water_intake < water_goal:
            # Ask the user how much water they have drank today
           # user_water_intake += float(input("How much water have you drank today? : "))
            # Compare the user's water intake with the target water intake
            percentage = round((user_water_intake / water_goal) * 100, -1)
            if user_water_intake >= water_goal:
                print("Congratulations! You have met your daily water goal.")
            
            #else: print(f"You need to drink {water_goal - user_water_intake} more ounces of water to reach your goal.")



    #def update_terrarium_water_level(self, amount):
        """
        Update the water level in the terrarium.

        Parameters:
        amount (float): The amount of water to update the terrarium water level with.
        """
