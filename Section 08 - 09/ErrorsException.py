while True:
    try:
        age=int(input("What is your age?"))
        if age < 1: 
            raise ZeroDivisionError("hey cut it down")
        print(f"your age is {age}")
    except (ValueError,ZeroDivisionError) as err:
        print(err)
        continue
    else: 
        print("thank you")
        break
    finally:
        print("OK, i am finaly done")