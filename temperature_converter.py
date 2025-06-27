import sys
try:
    if len(sys.argv)>2:
        temperature_scales=sys.argv[1]
        temperature_value=float(sys.argv[2])

        if temperature_scales.lower()=='c':
            temperature_value=(temperature_value*float(1.8))+float(32)
            print(f"{sys.argv[2]} C = ",temperature_value," F")

        elif temperature_scales.lower()=='f' and 'F':
            input=sys.argv[2]
            temperature_value=(temperature_value-float(32))/float(1.8)
            print(f"{sys.argv[2]} F = ",temperature_value," C")

        else:
            print("Invalid temperature scale. Use 'c' or 'f'.")
    else:
        print("invalid temperature")

except ValueError:
    print("invalid temperature symbol")
