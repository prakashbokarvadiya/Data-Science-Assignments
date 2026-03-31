// ─────────────────────────────────────────────────────────────────────────────
// NoSQL Task 2 — Find employees who work in the IT department
// Database   : company_db
// Collection : employees
// ─────────────────────────────────────────────────────────────────────────────

use company_db;

// ── Query: All employees in the 'IT' department ───────────────────────────
db.employees.find(
    { department: "IT" }
).pretty();

// ── With projection — show only relevant fields ───────────────────────────
db.employees.find(
    { department: "IT" },
    { name: 1, department: 1, salary: 1, job_id: 1, _id: 0 }
).pretty();

// ── Count of IT employees ─────────────────────────────────────────────────
db.employees.countDocuments({ department: "IT" });

// ── Sorted by name ────────────────────────────────────────────────────────
db.employees.find(
    { department: "IT" }
).sort({ name: 1 }).pretty();

// Explanation:
// { department: "IT" } is the filter — MongoDB performs an equality match.
// Field names are case-sensitive; "IT" must match the stored value exactly.
// .sort({ name: 1 }) sorts results by name in ascending (A-Z) order.
// Projection limits the fields returned, improving query efficiency.
