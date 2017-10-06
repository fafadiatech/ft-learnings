CREATE TABLE issues (
    issue_no INTEGER PRIMARY KEY NOT NULL,
    title VARCHAR(255),
    create_by INTEGER, 
    closed NUMERIC
);

CREATE TABLE company (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    logo VARCHAR(255)
);

INSERT INTO issues VALUES(1, "Learn SQL", 1, 0);
INSERT INTO issues VALUES(2, "Learn Indexes", 1, 0);
INSERT INTO issues VALUES(3, "Learn SQL Optimization", 1, 0);
INSERT INTO issues VALUES(4, "Benchmark", 1, 0);

INSERT INTO company VALUES (1, "Fafadia Tech", "");
INSERT INTO company VALUES (2, "Fafadia Group", "");
