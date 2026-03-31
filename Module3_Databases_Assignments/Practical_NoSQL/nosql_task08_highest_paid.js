// ─────────────────────────────────────────────────────────────────────────────
// NoSQL Task 8 — Find the highest-paid employee
// Database   : company_db
// Collection : employees
// ─────────────────────────────────────────────────────────────────────────────

use company_db;

// ── Method 1: Sort descending + limit 1 (simplest) ────────────────────────
db.employees.find(
    {},
    { name: 1, department: 1, salary: 1, _id: 0 }
).sort({ salary: -1 }).limit(1).pretty();

// ── Method 2: Aggregation pipeline ───────────────────────────────────────
db.employees.aggregate([
    {
        $sort: { salary: -1 }           // sort by salary descending
    },
    {
        $limit: 1                        // keep only the top record
    },
    {
        $project: {                      // shape the output
            _id        : 0,
            name       : 1,
            department : 1,
            salary     : 1,
            emp_id     : 1
        }
    }
]);

// ── Method 3: Using $group to find the global MAX salary ─────────────────
// (Returns max salary value — good for then fetching the matching employee)
db.employees.aggregate([
    {
        $group: {
            _id       : null,
            max_salary: { $max: "$salary" }
        }
    }
]);

// ── Method 4: Highest-paid employee PER DEPARTMENT ───────────────────────
db.employees.aggregate([
    {
        $sort: { salary: -1 }
    },
    {
        $group: {
            _id            : "$department",
            top_employee   : { $first: "$name" },
            highest_salary : { $first: "$salary" }
        }
    },
    {
        $sort: { highest_salary: -1 }
    },
    {
        $project: {
            _id            : 0,
            department     : "$_id",
            top_employee   : 1,
            highest_salary : 1
        }
    }
]);

// Explanation:
// Method 1 — .sort({ salary: -1 }) descending + .limit(1) is the most concise
//   and efficient way to find the single top-earning employee.
// Method 2 — Aggregation pipeline gives more control over output shape.
// Method 3 — $group with $max is ideal when you only need the maximum value.
// Method 4 — $group by department with $first (after sorting) finds the
//   highest-paid employee in EACH department in one pipeline.
