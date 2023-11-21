class WaterTracker:
    def __init__(self, water_intake):
        """Initialize the WaterTracker class."""
        self.water_intake = water_intake
      

def check_water_intake(water_intake):
    """
    Check the water intake for the user.

    Parameters:
    water_intake (float): The target water intake for the user.
    """
    # Initialize the user's water intake to zero
    user_water_intake = 0
    # Loop until the user's water intake is equal or greater than the target water intake
    while user_water_intake < water_intake:
        # Ask the user how much water they have drank today
        user_water_intake += float(input("How much water have you drank today? : "))
        # Compare the user's water intake with the target water intake
        if user_water_intake >= water_intake:
            print("Congratulations! You have met your daily water intake goal.")
        else:
            print(f"You need to drink {water_intake - user_water_intake} more liters of water to reach your goal.")



    def update_terrarium_water_level(self, amount):
        """
        Update the water level in the terrarium.

        Parameters:
        amount (float): The amount of water to update the terrarium water level with.
        """