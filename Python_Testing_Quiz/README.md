# Python Testing Quiz — Manual QA Project

## Overview

QA QUEST is a command-line multiple-choice quiz developed in Python. It presents five questions about software testing. Users select an answer (A, B, C, or D), receive feedback, and see their final score at the end.

This project demonstrates practical work with Python and manual software testing documentation.

## Project Contents

- **`python_testing_quiz.py`** — the Python quiz application.
- **[Test Plan](PyTestQuiz_TestPlan_v1.0.docx)** — defines the test objectives, scope, approach, environment, and completion criteria.
- **[Test Cases and Results](PyTestQuiz_TestCases_v1.0.xlsx)** — contains 17 manual test cases, including expected and actual results, execution statuses, and retesting records.

## Testing Approach

The project uses manual functional testing with positive and negative test scenarios.

The documented testing scope includes:

- Application launch and initial display
- Questions and answer options
- Correct and incorrect answers
- Uppercase and lowercase input
- Leading and trailing spaces
- Blank and invalid input
- Feedback messages and final score
- Retesting after fixes

## Defect Tracking Evidence

Jira defect records for this project are documented in the screenshots below. Each issue is split into two screenshots to show the full issue details.

- **SCRUM-6:** [Part 1](evidence/SCRUM-6-1.png) · [Part 2](evidence/SCRUM-6-2.png)
- **SCRUM-7:** [Part 1](evidence/SCRUM-7-1.png) · [Part 2](evidence/SCRUM-7-2.png)

## Test Environment

- **Operating system:** Windows 10
- **Python:** Version 3.14 (64-bit)
- **Development environment:** PyCharm
- **Application type:** Command-line interface

## How to Run

1. Make sure Python is installed.
2. Open a terminal in the `Python_Testing_Quiz` folder.
3. Run:

   ```bash
   python python_testing_quiz.py
   ```

4. Answer each question by entering A, B, C, or D.
5. After the final score appears, press Enter to exit.

## Scope and Limitations

This project focuses on manual functional testing of a command-line application. Database, network, web, API, performance, security, and automated testing are outside the scope of the current test cycle.

## Project Purpose

This is a personal learning and portfolio project intended to demonstrate practical application of software testing concepts and QA documentation.
