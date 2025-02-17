-- Create Department Table
CREATE TABLE department (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL UNIQUE
);

-- Create Employee Table
CREATE TABLE employee (
    emp_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    dept_id INT REFERENCES department(dept_id) ON DELETE SET NULL,
    hire_date DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Create Salary Table
CREATE TABLE salary (
    salary_id SERIAL PRIMARY KEY,
    emp_id INT REFERENCES employee(emp_id) ON DELETE CASCADE,
    salary_month DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    UNIQUE (emp_id, salary_month)
);
CREATE INDEX idx_salary_emp_id ON salary(emp_id);
CREATE INDEX idx_salary_month ON salary(salary_month);

