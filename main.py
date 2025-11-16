def sort(width: float, height: float, length: float, mass: float) -> str:
    volume = width * height * length
    bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    heavy = mass >= 20
    return (
        "REJECTED" if bulky and heavy
        else "SPECIAL" if bulky or heavy
        else "STANDARD"
    )


if __name__ == "__main__":
    test_cases = [
        {"args": (10, 10, 10, 5), "expected": "STANDARD"},
        {"args": (100, 100, 100, 5), "expected": "SPECIAL"},
        {"args": (150, 10, 10, 5), "expected": "SPECIAL"},
        {"args": (10, 10, 10, 20), "expected": "SPECIAL"},
        {"args": (150, 10, 10, 20), "expected": "REJECTED"},
        {"args": (100, 100, 100, 25), "expected": "REJECTED"},
        {"args": (150, 150, 150, 20), "expected": "REJECTED"},
        {"args": (149.9, 149.9, 44.5, 19.99), "expected": "STANDARD"},
    ]

    for i, case in enumerate(test_cases, start=1):
        result = sort(*case["args"])
        status = "OK" if result == case["expected"] else "FAIL"
        print(f"Test {i}: {status} (got {result}, expected {case['expected']})")
