from main import *

run_cases = [
    (10, 5, 20),
    (20, 5, 40),
]

submit_cases = run_cases + [
    (320, 5, 640),
    (640, 5, 1280),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * armor:  {input1}")
    print(f" * height: {input2}")
    print(f"Expected: {expected_output}")
    wall = Wall()
    wall.armor = input1
    wall.height = input2
    wall.fortify()
    result = wall.armor
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()