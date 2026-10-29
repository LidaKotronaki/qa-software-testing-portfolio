-- QA Reporting Portfolio Project
-- Setup: Create and populate the test_cases table
-- Run this script once in a fresh SQLite database.

CREATE TABLE test_cases (
    id INTEGER PRIMARY KEY,
    test_name TEXT,
    status TEXT,
    priority TEXT
);

INSERT INTO test_cases (id, test_name, status, priority)
VALUES
    (1, 'Valid login', 'Passed', 'High'),
    (2, 'Invalid password', 'Failed', 'High'),
    (3, 'Empty username', 'Passed', 'Medium'),
    (4, 'Password reset', 'Blocked', 'Medium'),
    (5, 'Logout', 'Passed', 'Low');
