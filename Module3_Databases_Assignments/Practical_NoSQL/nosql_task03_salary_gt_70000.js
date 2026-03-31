// ─────────────────────────────────────────────────────────────────────────────
// NoSQL Task 3 — Find employees who have a salary greater than 70,000
// Database   : company_db
// Collection : employees
// ─────────────────────────────────────────────────────────────────────────────

use company_db;

// ── Query: salary > 70000 ─────────────────────────────────────────────────
db.employees.find(
    { salary: { $gt: 70000 } }
).pretty();

// ── With projection ───────────────────────────────────────────────────────
db.employees.find(
    { salary: { $gt: 70000 } },
    { name: 1, department: 1, salary: 1, _id: 0 }
).pretty();

// ── Sorted by salary descending (highest first) ───────────────────────────
db.employees.find(
    { salary: { $gt: 70000 } },
    { name: 1, department: 1, salary: 1, _id: 0 }
).sort({ salary: -1 }).pretty();

// ── Count employees earning above 70,000 ─────────────────────────────────
db.employees.countDocuments({ salary: { $gt: 70000 } });

// ── Range query: salary between 70,000 and 100,000 ───────────────────────
db.employees.find(
    { salary: { $gt: 70000, $lte: 100000 } },
    { name: 1, department: 1, salary: 1, _id: 0 }
).sort({ salary: -1 });

// Explanation:
// $gt  = greater than        (strictly >)
// $gte = greater than or equal (>=)
// $lt  = less than           (strictly <)
// $lte = less than or equal  (<=)
// Multiple comparison operators in one field object act as AND conditions.
// .sort({ salary: -1 }) → descending order; { salary: 1 } → ascending.
