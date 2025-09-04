"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average

Show statistics: sum, average, min, max
"""

def number_operations():
    numbers = []

    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        while True:
            try:
                num = float(input(f"Number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Please enter a valid number.")

    # Display original list
    print(f"\nOriginal numbers: {numbers}")

    # Create filtered lists
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    # Calculate average
    total = sum(numbers)
    average = total / len(numbers)

    # Numbers greater than average
    above_average = [num for num in numbers if num > average]

    # Display results
    print(f"\nEven numbers: {even_numbers}")
    print(f"Odd numbers: {odd_numbers}")
    print(f"Numbers greater than the average ({average:.2f}): {above_average}")

    print("\nStatistics:")
    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")
    print(f"Minimum: {min(numbers)}")
    print(f"Maximum: {max(numbers)}")

if __name__ == "__main__":
    number_operations()
