def main() -> None:
    user_input = input("Enter a number: ")

    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    result = number * 10

    if result.is_integer():
        print(f"Result: {int(result)}")
    else:
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
