import Water_Calculator

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



    def update_terrarium_water_level(self, amount):
        """
        Update the water level in the terrarium.

        Parameters:
        amount (float): The amount of water to update the terrarium water level with.
        """