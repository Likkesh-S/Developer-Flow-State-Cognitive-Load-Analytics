-- CogniStream: Developer Flow-State & Cognitive Load Analytics
-- File 11: Create the developer activity table

CREATE TABLE IF NOT EXISTS developer_activity (
    activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    developer_id TEXT NOT NULL,

    coding_minutes INTEGER NOT NULL DEFAULT 0
        CHECK (coding_minutes >= 0),

    interruption_count INTEGER NOT NULL DEFAULT 0
        CHECK (interruption_count >= 0),

    context_switches INTEGER NOT NULL DEFAULT 0
        CHECK (context_switches >= 0),

    task_complexity INTEGER NOT NULL
        CHECK (task_complexity BETWEEN 1 AND 5),

    break_minutes INTEGER NOT NULL DEFAULT 0
        CHECK (break_minutes >= 0),

    focus_score REAL NOT NULL
        CHECK (focus_score BETWEEN 0 AND 100),

    cognitive_load_score REAL NOT NULL
        CHECK (cognitive_load_score BETWEEN 0 AND 100)
);

-- Improve searches by developer and timestamp.
CREATE INDEX IF NOT EXISTS idx_activity_developer
ON developer_activity (developer_id);

CREATE INDEX IF NOT EXISTS idx_activity_timestamp
ON developer_activity (timestamp);

CREATE INDEX IF NOT EXISTS idx_activity_developer_timestamp
ON developer_activity (developer_id, timestamp);
