import textwrap
questions = [
    {
        "question": "Which of the following statements describe a valid test objective?",
        "options": [
            "A. To prove there are no unfixed defects in the system under test",
            "B. To prove that there will be no failures after the implementation of the system into production",
            "C. To reduce the risk level of the test object and to build confidence in the quality level",
            "D. To verify that there are no untested combinations of inputs",
        ],
        "answer": "C",

    },
    {
        "question": "Which of the following options shows an example of test activities that contribute to success?",
        "options": [
            "A. Having testers involved during various software development lifecycle (SDLC) activities will help detect defects in work products",
            "B. Testers try not to disturb the developers while coding, so that the developers write better code",
            "C. Testers collaborating with end users help to improve the quality of defect reports during component integration and system testing",
            "D. Certified testers will design much better test cases than non-certified testers",
        ],
        "answer": "A",

    },
    {
        "question": "You have been assigned as a tester to a team producing a new system incrementally. You have noticed that no changes have been made  to the existing regression test cases for several iterations and no new regression defects were identified. Your manager is happy, but you are not. Which testing principle explains your skepticism?",
        "options": [
            "A. Tests wear out",
            "B. Absence-of-defects fallacy",
            "C. Defects cluster together",
            "D. Exhaustive testing is impossible",
        ],
        "answer": "A",

    },
    {
        "question": "You work in a team that develops a mobile application for food ordering. In the current iteration the team decided to implement the payment functionality.\nWhich of the following activities is a part of test analysis?",
        "options": [
            "A. Estimating that testing the integration with the payment service will take 8-person days",
            "B. Deciding that the team should test if it is possible to properly share payment between many users",
            "C. Using boundary value analysis (BVA) to derive the test data for the test cases that check the correct payment processing for the minimum allowed amount to be paid",
            "D. Analyzing the discrepancy between the actual result and expected result after executing a test case that checks the process of payment with a credit card, and reporting a defect",
        ],
        "answer": "B",

    },
    {
        "question": "Which of the following factors are a SIGNIFICANT influence on the test approach?\ni. The SDLC\nii. The number of defects detected in previous projects\niii. The identified product risks\niv. New regulatory requirements forcing formal white-box testing\nv. The test environment setup",
        "options": [
            "A. i, ii have significant influence",
            "B. i, iii, iv have significant influence",
            "C. ii, iv, v have significant influence",
            "D. iii, v have significant influence",
        ],
        "answer": "B",

    },
]


def play_quiz():
    score = 0

    print("================================")
    print("       QA QUEST")
    print("   The Testing Challenge")
    print("================================")

    for number, item in enumerate(questions, start=1):
        print(f"\nQuestion {number}:")

        for line in item["question"].splitlines():
            print(textwrap.fill(line, width=70))

        print()  # Blank line before the choices

        for option in item["options"]:
            print(option)

        print()  # Blank line before the answer prompt

        answer = input("Your answer (A, B, C or D): ").strip().upper()

        if answer == item["answer"]:
            print("Correct! +1 point")
            score += 1
        else:
            print(f"Not quite. Correct answer: {item['answer']}")

    print(f"\nGame over! Your score: {score}/{len(questions)}")


if __name__ == "__main__":
    play_quiz()
    input("\nPress Enter to exit...")




