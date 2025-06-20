from main import *

run_cases = [
    ([0, 20, 30], [20, 30]),
    ([10, 0, 40, 0], [10, 40]),
]

submit_cases = run_cases + [
    ([], []),
    ([3, 2, 0, 3, 0, 0], [3, 2, 3]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input:     {input1}")
    print(f"Expected: {expected_output}")
    try:
        result = destroy_walls(input1)
        print(f"Actual:   {result}")
        if str(result) != str(expected_output):
            return False
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
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
