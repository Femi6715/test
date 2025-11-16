Thoughtful Robotic Package Sorter

This project contains a Python function used in Thoughtful’s robotic automation factory. The function determines which stack a package should be dispatched to based on its dimensions and mass.

Objective

A package is classified using the following rules:

Bulky Package

A package is bulky if any of the following is true:

Its volume (width * height * length) is ≥ 1,000,000 cm³

Any dimension (width, height, or length) is ≥ 150 cm

Heavy Package

A package is heavy if:

Its mass is ≥ 20 kg

Dispatch Rules
Condition	Stack
Bulky and Heavy	REJECTED
Bulky or Heavy (only one)	SPECIAL
Neither Bulky nor Heavy	STANDARD
🧠 Function
def sort(width: float, height: float, length: float, mass: float) -> str:
    volume = width * height * length
    bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    heavy = mass >= 20
    return (
        "REJECTED" if bulky and heavy
        else "SPECIAL" if bulky or heavy
        else "STANDARD"
    )

🧪 Running Tests

Run the script to execute basic unit tests:

python main.py

📁 Project Structure
.
├── main.py        # Contains implementation and test cases
└── README.md      # Project documentation

🛠 Requirements

Python 3.8+

📍 Example Usage
print(sort(10, 10, 10, 5))           # STANDARD
print(sort(150, 10, 10, 5))          # SPECIAL
print(sort(100, 100, 100, 25))       # REJECTED

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss proposed updates.
