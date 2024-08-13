def heating_cooling(actual_temp, desired_temp):
    actual_temp = int(input("Enter the current temperature: "))
    desired_temp = int(input("Enter the desired temperature: "))
    print(f"Current Temp: {actual_temp}")
    print(f"Desired Temp: {desired_temp}")

    if actual_temp > desired_temp:
        print("Run A/C")
    elif actual_temp < desired_temp:
        print("Run heat")
    elif actual_temp == desired_temp:
        print("Standby")

heating_cooling(71,80)
