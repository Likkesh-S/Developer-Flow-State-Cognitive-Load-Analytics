-- CogniStream
-- File 12: Developer Activity Analysis Queries

-- Query 1: View all developer activity records
SELECT *
FROM developer_activity
ORDER BY timestamp;


-- Query 2: Total coding time for each developer
SELECT
    developer_id,
    SUM(coding_minutes) AS total_coding_minutes,
    ROUND(SUM(coding_minutes) / 60.0, 2) AS total_coding_hours
FROM developer_activity
GROUP BY developer_id
ORDER BY total_coding_minutes DESC;


-- Query 3: Average focus score by developer
SELECT
    developer_id,
    ROUND(AVG(focus_score), 2) AS average_focus_score
FROM developer_activity
GROUP BY developer_id
ORDER BY average_focus_score DESC;


-- Query 4: Total interruptions and context switches
SELECT
    developer_id,
    SUM(interruption_count) AS total_interruptions,
    SUM(context_switches) AS total_context_switches
FROM developer_activity
GROUP BY developer_id
ORDER BY total_interruptions DESC;


-- Query 5: Average cognitive-load indicator by developer
SELECT
    developer_id,
    ROUND(AVG(cognitive_load_score), 2)
        AS average_cognitive_load_indicator
FROM developer_activity
GROUP BY developer_id
ORDER BY average_cognitive_load_indicator DESC;


-- Query 6: Focus category for each activity record
SELECT
    developer_id,
    timestamp,
    focus_score,
    CASE
        WHEN focus_score >= 80 THEN 'High'
        WHEN focus_score >= 60 THEN 'Moderate'
        ELSE 'Low'
    END AS focus_category
FROM developer_activity
ORDER BY developer_id, timestamp;


-- Query 7: Compare average focus with interruptions
SELECT
    developer_id,
    ROUND(AVG(focus_score), 2) AS average_focus,
    ROUND(AVG(interruption_count), 2) AS average_interruptions
FROM developer_activity
GROUP BY developer_id;


-- Query 8: Average activity metrics by task complexity
SELECT
    task_complexity,
    ROUND(AVG(coding_minutes), 2) AS average_coding_minutes,
    ROUND(AVG(focus_score), 2) AS average_focus_score,
    ROUND(AVG(cognitive_load_score), 2)
        AS average_cognitive_load_indicator
FROM developer_activity
GROUP BY task_complexity
ORDER BY task_complexity;


-- Query 9: Daily developer summary
SELECT
    developer_id,
    DATE(timestamp) AS activity_date,
    SUM(coding_minutes) AS daily_coding_minutes,
    SUM(interruption_count) AS daily_interruptions,
    SUM(context_switches) AS daily_context_switches,
    ROUND(AVG(focus_score), 2) AS daily_average_focus
FROM developer_activity
GROUP BY developer_id, DATE(timestamp)
ORDER BY activity_date, developer_id;


-- Query 10: Find activity records with frequent interruptions
SELECT
    developer_id,
    timestamp,
    interruption_count,
    context_switches,
    focus_score
FROM developer_activity
WHERE interruption_count >= 3
ORDER BY interruption_count DESC;
