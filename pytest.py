import terrarium as tm 

def test_terrarium():
    """
    tests all the outputs of terrarium
    """

    water = tm.Water_Calculator
    age = water.get_user_input.age
    sex = water.get_user_input.sex
    weight = water.get_user_input.weight
    height = water.get_user_input.height
    activity_level = water.get_user_input.activity_level

    assert water.get_user_input(age, int) and age > 0
    assert water.get_user_input(sex, str) and (sex == "m" or sex == "f")
    assert water.get_user_input(weight, int) and weight > 0
    assert water.get_user_input(height, int) and height > 0
    assert water.get_user_input(activity_level, int) and (activity_level >= 1 or activity_level <= 5)
    