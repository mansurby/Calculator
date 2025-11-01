"""
Calculator
Features: Basic operations, memory storage, calculation history, and power/root operations
"""


class SmartCalculator:
    def __init__(self):
        self.memory = 0
        self.history = []
        self.last_result = 0

    def add(self, a, b):
        """Add two numbers"""
        result = a + b
        self._save_to_history(f"{a} + {b}", result)
        return result

    def subtract(self, a, b):
        """Subtract b from a"""
        result = a - b
        self._save_to_history(f"{a} - {b}", result)
        return result

    def multiply(self, a, b):
        """Multiply two numbers"""
        result = a * b
        self._save_to_history(f"{a} × {b}", result)
        return result

    def divide(self, a, b):
        """Divide a by b"""
        if b == 0:
            return "Error: Cannot divide by zero!"
        result = a / b
        self._save_to_history(f"{a} ÷ {b}", result)
        return result

    def power(self, base, exponent):
        """Raise base to the power of exponent"""
        result = base ** exponent
        self._save_to_history(f"{base} ^ {exponent}", result)
        return result

    def square_root(self, num):
        """Calculate square root"""
        if num < 0:
            return "Error: Cannot calculate square root of negative number!"
        result = num ** 0.5
        self._save_to_history(f"√{num}", result)
        return result

    def percentage(self, num, percent):
        """Calculate percentage of a number"""
        result = (num * percent) / 100
        self._save_to_history(f"{percent}% of {num}", result)
        return result

    def _save_to_history(self, operation, result):
        """Save calculation to history"""
        self.history.append(f"{operation} = {result}")
        self.last_result = result

    def store_memory(self, value):
        """Store value in memory"""
        self.memory = value
        print(f"✓ Stored {value} in memory")

    def recall_memory(self):
        """Recall value from memory"""
        return self.memory

    def clear_memory(self):
        """Clear memory"""
        self.memory = 0
        print("✓ Memory cleared")

    def show_history(self):
        """Display calculation history"""
        if not self.history:
            print("\nNo calculations yet!")
            return

        print("\n" + "="*40)
        print("CALCULATION HISTORY")
        print("="*40)
        for i, calc in enumerate(self.history[-10:], 1):  # Show last 10
            print(f"{i}. {calc}")
        print("="*40)

    def clear_history(self):
        """Clear calculation history"""
        self.history = []
        print("✓ History cleared")


def display_menu():
    """Display calculator menu"""
    print("\n" + "="*40)
    print("     SMART CALCULATOR")
    print("="*40)
    print("1.  Add (+)")
    print("2.  Subtract (-)")
    print("3.  Multiply (×)")
    print("4.  Divide (÷)")
    print("5.  Power (^)")
    print("6.  Square Root (√)")
    print("7.  Percentage (%)")
    print("8.  Store in Memory (M+)")
    print("9.  Recall Memory (MR)")
    print("10. Clear Memory (MC)")
    print("11. Show History")
    print("12. Clear History")
    print("13. Use Last Result")
    print("0.  Exit")
    print("="*40)


def get_number(prompt="Enter number: ", allow_last=False, calc=None):
    """Get number input from user with validation"""
    while True:
        try:
            if allow_last and calc and calc.history:
                user_input = input(
                    f"{prompt} (or 'L' for last result {calc.last_result}): ")
                if user_input.upper() == 'L':
                    return calc.last_result
            else:
                user_input = input(prompt)

            return float(user_input)
        except ValueError:
            print("⚠ Invalid input! Please enter a valid number.")


def main():
    """Main calculator program"""
    calc = SmartCalculator()

    print("\n🔢 Welcome to Smart Calculator!")
    print("This calculator has memory and keeps your calculation history.")

    while True:
        display_menu()
        choice = input("\nSelect operation (0-13): ").strip()

        if choice == '0':
            print("\n👋 Thank you for using Smart Calculator!")
            break

        elif choice == '1':  # Add
            a = get_number("First number: ", True, calc)
            b = get_number("Second number: ", True, calc)
            result = calc.add(a, b)
            print(f"\n✓ Result: {a} + {b} = {result}")

        elif choice == '2':  # Subtract
            a = get_number("First number: ", True, calc)
            b = get_number("Second number: ", True, calc)
            result = calc.subtract(a, b)
            print(f"\n✓ Result: {a} - {b} = {result}")

        elif choice == '3':  # Multiply
            a = get_number("First number: ", True, calc)
            b = get_number("Second number: ", True, calc)
            result = calc.multiply(a, b)
            print(f"\n✓ Result: {a} × {b} = {result}")

        elif choice == '4':  # Divide
            a = get_number("First number: ", True, calc)
            b = get_number("Second number: ", True, calc)
            result = calc.divide(a, b)
            print(f"\n✓ Result: {result}")

        elif choice == '5':  # Power
            base = get_number("Base: ", True, calc)
            exp = get_number("Exponent: ")
            result = calc.power(base, exp)
            print(f"\n✓ Result: {base} ^ {exp} = {result}")

        elif choice == '6':  # Square Root
            num = get_number("Number: ", True, calc)
            result = calc.square_root(num)
            print(f"\n✓ Result: √{num} = {result}")

        elif choice == '7':  # Percentage
            num = get_number("Number: ", True, calc)
            percent = get_number("Percentage: ")
            result = calc.percentage(num, percent)
            print(f"\n✓ Result: {percent}% of {num} = {result}")

        elif choice == '8':  # Store Memory
            value = get_number("Value to store: ", True, calc)
            calc.store_memory(value)

        elif choice == '9':  # Recall Memory
            mem_value = calc.recall_memory()
            print(f"\n💾 Memory: {mem_value}")

        elif choice == '10':  # Clear Memory
            calc.clear_memory()

        elif choice == '11':  # Show History
            calc.show_history()

        elif choice == '12':  # Clear History
            calc.clear_history()

        elif choice == '13':  # Use Last Result
            if calc.history:
                print(f"\n📋 Last result: {calc.last_result}")
            else:
                print("\n⚠ No previous calculations!")

        else:
            print("\n⚠ Invalid choice! Please select 0-13.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
