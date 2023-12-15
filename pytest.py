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

    assert water_calc.get_user_input(age, int) and age > 0
    assert water_calc.get_user_input(sex, str) and (sex == "m" or sex == "f")
    assert water_calc.get_user_input(weight, int) and weight > 0
    assert water_calc.get_user_input(height, int) and height > 0
    assert water_calc.get_user_input(activity_level, int) and (activity_level >= 1 or activity_level <= 5)

    bmr = water_calc.calc_BMR.bmr
    assert water_calc.calc_BMR(bmr, int)
    assert water_calc.calc_BMR(sex = "m", weight = 180, height = 70, age = 35) == 1838.4, "Test failed: Formula should equal 1838.4 BMR"
    assert water_calc.calc_BMR(sex = "f", weight = 130, height = 64, age = 25) == 1403.8, "Test failed: Formula should equal 1404.8 BMR"
    assert water_calc.calc_BMR(sex = "m", weight = 150, height = 65, age = 25) == 1656, "Test failed: Formula should equal 1656 BMR"
    assert water_calc.calc_BMR(sex = "f", weight = 140, height = 69, age = 40) == 1400.3, "Test failed: Formula should equal 1400.3 BMR"

    adjust = water_calc.adjust_for_activity_level.TDEE
    assert water_calc.adjust_for_activity_level(adjust, int)
    assert water_calc.adjust_for_activity_level(activity_multipliers = 1)
    assert water_calc.adjust_for_activity_level(activity_multipliers = 2)
    assert water_calc.adjust_for_activity_level(bmr = 1403.8, activity_multipliers = 3) == 2175.89
    assert water_calc.adjust_for_activity_level(activity_multipliers = 4)
    assert water_calc.adjust_for_activity_level(activity_multipliers = 5)



    water_tracker = tm.WaterTracker
    percentage = water_tracker.check_water_intake(percentage, float) and percentage > 0
    