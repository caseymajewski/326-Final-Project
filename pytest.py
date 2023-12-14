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
    assert water_calc.calc_BMR(sex = "m", weight = 180, height = 70, age = 35) == 1838.4
    assert water_calc.calc_BMR(sex = "f", weight = 130, height = 64, age = 25) == 1403.8

    adjust = water_calc.adjust_for_activity_level.TDEE
    assert water_calc.adjust_for_activity_level(adjust, int)

    water_tracker = tm.WaterTracker
    percentage = water_tracker.check_water_intake(percentage, float) and percentage > 0
    