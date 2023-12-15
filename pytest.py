import terrarium as tm 

def test_terrarium():
    """
    tests all the outputs of terrarium
    """

    water_calc = tm.WaterCalculator
    age = water_calc.get_user_input.age
    sex = water_calc.get_user_input.sex
    weight = water_calc.get_user_input.weight
    height = water_calc.get_user_input.height
    activity_level = water_calc.get_user_input.activity_level

    assert water_calc.get_user_input(age, int) and age > 0, "Test failed: Age input is not INT or greater than 0."
    assert water_calc.get_user_input(sex, str) and (sex == "m" or sex == "f"), """Test failed: Sex input is not STR or "m" or "f"."""
    assert water_calc.get_user_input(weight, int) and weight > 0, "Test failed: Weight input is not INT or greater than 0."
    assert water_calc.get_user_input(height, int) and height > 0, "Test failed: Height input is not INT or greated than 0."
    assert water_calc.get_user_input(activity_level, int) and (activity_level >= 1 or activity_level <= 5), "Test failed: Activity Level input is not INT or in betweem 1 to 5."

    bmr = water_calc.calc_BMR.bmr
    assert water_calc.calc_BMR(bmr, int), "Test failed: BMR is not INT."
    assert water_calc.calc_BMR(sex = "m", weight = 180, height = 70, age = 35) == 1838.4, "Test failed: Formula should equal 1838.4 BMR"
    assert water_calc.calc_BMR(sex = "f", weight = 130, height = 64, age = 25) == 1403.8, "Test failed: Formula should equal 1404.8 BMR"
    assert water_calc.calc_BMR(sex = "m", weight = 150, height = 65, age = 25) == 1656, "Test failed: Formula should equal 1656 BMR"
    assert water_calc.calc_BMR(sex = "f", weight = 140, height = 69, age = 40) == 1400.3, "Test failed: Formula should equal 1400.3 BMR"

    adjust = water_calc.adjust_for_activity_level.TDEE
    assert water_calc.adjust_for_activity_level(adjust, int), "Test failed: TDEE is not INT."
    assert water_calc.adjust_for_activity_level(bmr = 1403.8, activity_multipliers = 1) == 1684.56, "Test failed: Formula should equal 1684.56 TDEE."
    assert water_calc.adjust_for_activity_level(bmr = 1403.8, activity_multipliers = 2) == 1930.225, "Test failed: Formula should equal 1930.225 TDEE."
    assert water_calc.adjust_for_activity_level(bmr = 1403.8, activity_multipliers = 3) == 2175.89, "Test failed: Formula should equal 2175.89 TDEE."
    assert water_calc.adjust_for_activity_level(bmr = 1403.8, activity_multipliers = 4) == 2421.555, "Test failed: Formula should equal 2421.555 TDEE."
    assert water_calc.adjust_for_activity_level(bmr = 1403.8, activity_multipliers = 5) == 2667.22, "Test failed: Formula should equal 2667.22 TDEE."

    water_tracker = tm.WaterTracker
    percentage = water_tracker.check_water_intake(percentage, float) and percentage > 0, "Test failed: Percentage is not a FLOAT or greater than 0."

    ounces = water_calc.final_intake.water_intake_goal_oz
    assert water_calc.final_intake(ounces, int), "Test failed: Water Intake in Ounces is not INT."
    assert water_calc.final_intake(TDEE = 1684.56) == 50.5368, "Test failed: Formula should equal 50.5368 ounces."
    assert water_calc.final_intake(TDEE = 1930.225) == 57.90675, "Test failed: Formula should equal 57.90675 ounces."
    assert water_calc.final_intake(TDEE = 2175.89) == 65.2767, "Test failed: Formula should equal 65.2767 ounces."
    assert water_calc.final_intake(TDEE = 2421.555) == 72.64665, "Test failed: Formula should equal 72.64665 ounces."
    assert water_calc.final_intake(TDEE = 2667.22) == 80.0166, "Test failed: Formula should equal 80.0166 ounces."

    
    