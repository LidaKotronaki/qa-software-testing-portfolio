# SQL QA Reporting Portfolio Project

## Overview

This project demonstrates how SQL can be used to analyse software test execution results in SQLite. It contains seven reporting queries covering test outcomes, priorities, tests that need attention, and a summary pass rate.

## Dataset

The sample `test_cases` table contains five fictional test cases.

| Column | Description |
|---|---|
| `id` | Unique test-case identifier |
| `test_name` | Test-case description |
| `status` | Execution outcome: Passed, Failed, or Blocked |
| `priority` | Test priority: High, Medium, or Low |

## Project Files

- `setup.sql` — creates and populates the sample table. Run it once in a fresh SQLite database.
- `qa_reports.sql` — contains the seven reporting queries.

## Reports Included

1. Test-case counts by status
2. Test-case counts by priority, ordered High to Low
3. Failed and blocked tests requiring attention
4. Overall QA summary and pass rate
5. Statuses with more than one test case
6. Search test cases by keyword
7. High-priority tests that have not passed

## Example Results

### Test results by status

| Status | Total tests |
|---|---:|
| Passed | 3 |
| Failed | 1 |
| Blocked | 1 |

### Test results by priority

| Priority | Total tests |
|---|---:|
| High | 2 |
| Medium | 2 |
| Low | 1 |

### Overall QA summary

| Metric | Result |
|---|---:|
| Total test cases | 5 |
| Passed | 3 |
| Failed | 1 |
| Blocked | 1 |
| Pass rate | 60.0% |

Two test cases require attention: one failed high-priority test and one blocked medium-priority test.

## How to Run

1. Open a fresh SQLite database.
2. Run `setup.sql` once to create and populate the table.
3. Run the queries in `qa_reports.sql`.

All data is fictional and intended for portfolio demonstration and practice.
