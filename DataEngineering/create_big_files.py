import psycopg2
import random
import threading
from concurrent.futures import ThreadPoolExecutor
from faker import Faker
from datetime import datetime, timedelta
from tqdm import tqdm

# Database connection details (modify as per your DB)
DB_CONFIG = {
    "dbname": "bigdata",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}

# Constants
NUM_DEPARTMENTS = 50
NUM_EMPLOYEES = 50000000  # Large number for 10GB+
YEARS_OF_SALARY = 5  # 5 years of salary data
THREADS = 100  # Number of parallel threads

fake = Faker()

# Thread Lock for safe database insertions
lock = threading.Lock()

def get_db_connection():
    """Returns a new database connection."""
    return psycopg2.connect(**DB_CONFIG)

def insert_departments():
    """Insert random departments."""
    conn = get_db_connection()
    cur = conn.cursor()
    
    departments = [(fake.company(),) for _ in range(NUM_DEPARTMENTS)]
    cur.executemany("INSERT INTO department (dept_name) VALUES (%s) ON CONFLICT DO NOTHING;", departments)
    
    conn.commit()
    cur.close()
    conn.close()
    print("Inserted Departments")

def insert_employees():
    """Insert random employees into the database."""
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Fetch department IDs
    cur.execute("SELECT dept_id FROM department;")
    dept_ids = [row[0] for row in cur.fetchall()]
    
    employees = []
    for _ in tqdm(range(NUM_EMPLOYEES), desc="Inserting Employees"):
        employees.append((
            fake.first_name(),
            fake.last_name(),
            random.choice(dept_ids),
            fake.date_between(start_date="-10y", end_date="today"),
            fake.email()
        ))

        if len(employees) % 10000 == 0:  # Batch Insert
            cur.executemany("INSERT INTO employee (first_name, last_name, dept_id, hire_date, email) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;", employees)
            conn.commit()
            employees = []

    if employees:
        cur.executemany("INSERT INTO employee (first_name, last_name, dept_id, hire_date, email) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;", employees)
        conn.commit()

    cur.close()
    conn.close()
    print("Inserted Employees")

def insert_salary_data(emp_ids):
    """Insert salary data for a batch of employees."""
    conn = get_db_connection()
    cur = conn.cursor()

    salary_data = []
    start_date = datetime.today() - timedelta(days=YEARS_OF_SALARY * 365)
    
    for emp_id in emp_ids:
        for i in range(YEARS_OF_SALARY * 12):
            salary_month = (start_date + timedelta(days=i * 30)).strftime('%Y-%m-%d')
            salary_amount = round(random.uniform(3000, 15000), 2)
            salary_data.append((emp_id, salary_month, salary_amount))

            if len(salary_data) % 100000 == 0:  # Batch insert every 100K records
                with lock:
                    cur.executemany("INSERT INTO salary (emp_id, salary_month, amount) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING;", salary_data)
                    conn.commit()
                    salary_data = []

    if salary_data:
        with lock:
            cur.executemany("INSERT INTO salary (emp_id, salary_month, amount) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING;", salary_data)
            conn.commit()

    cur.close()
    conn.close()

def insert_salaries():
    """Distribute employee salary insertion across multiple threads."""
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT emp_id FROM employee;")
    emp_ids = [row[0] for row in cur.fetchall()]
    
    conn.close()
    
    chunk_size = len(emp_ids) // THREADS
    emp_chunks = [emp_ids[i:i + chunk_size] for i in range(0, len(emp_ids), chunk_size)]
    
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        list(tqdm(executor.map(insert_salary_data, emp_chunks), total=len(emp_chunks), desc="Inserting Salaries"))

if __name__ == "__main__":
    insert_departments()
    insert_employees()
    insert_salaries()
    print("Data Insertion Complete!")
