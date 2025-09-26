for i in range(5):
    temp_air = int(input('введите температуру воздуха'))
    if temp_air < 10:
        print(f"прохладно {temp_air}")
    elif temp_air >= 10 and temp_air <= 21:
        print(f"норм {temp_air}")
    else:
        # temp_air > 21:
        print(f"жарковато {temp_air}")

for i in range(5):
    temp_air = int(input('введите температуру воздуха'))
    if temp_air < 10:
        print(f"прохладно {temp_air}")
    if temp_air >= 10 and temp_air <= 21:
        print(f"норм {temp_air}")

    if temp_air > 21:
        print(f"жарковато {temp_air}")