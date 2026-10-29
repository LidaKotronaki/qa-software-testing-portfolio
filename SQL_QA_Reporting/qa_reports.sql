-- QA Reporting Portfolio Project

-- Report 1: Count test cases by status

SELECT status, COUNT(*) AS total_tests
FROM test_cases
GROUP BY status
ORDER BY total_tests DESC, status ASC;


-- Report 2: Count test cases by priority

SELECT priority, COUNT(*) AS total_tests
FROM test_cases
GROUP BY priority
ORDER BY
    CASE priority
        WHEN 'High' THEN 1
        WHEN 'Medium' THEN 2
        WHEN 'Low' THEN 3
        ELSE 4
    END;


-- Report 3: Tests that need attention

SELECT id, test_name, priority, status
FROM test_cases
WHERE status IN ('Failed', 'Blocked')
ORDER BY
    CASE priority
        WHEN 'High' THEN 1
        WHEN 'Medium' THEN 2
        WHEN 'Low' THEN 3
        ELSE 4
    END;


-- Report 4: Overall QA summary

SELECT
    COUNT(*) AS total_tests,
    SUM(CASE WHEN status = 'Passed' THEN 1 ELSE 0 END) AS passed_tests,
    SUM(CASE WHEN status = 'Failed' THEN 1 ELSE 0 END) AS failed_tests,
    SUM(CASE WHEN status = 'Blocked' THEN 1 ELSE 0 END) AS blocked_tests,
    ROUND(
        100.0 * SUM(CASE WHEN status = 'Passed' THEN 1 ELSE 0 END)
        / COUNT(*),
        1
    ) AS pass_rate_pct
FROM test_cases;


-- Report 5: Statuses with multiple test cases

SELECT status, COUNT(*) AS total_tests
FROM test_cases
GROUP BY status
HAVING COUNT(*) > 1;


-- Report 6: Search test cases by keyword

SELECT id, test_name, priority, status
FROM test_cases
WHERE test_name LIKE '%login%';


-- Report 7: High-priority tests that have not passed

SELECT id, test_name, priority, status
FROM test_cases
WHERE priority = 'High'
  AND status <> 'Passed'
ORDER BY id ASC;
