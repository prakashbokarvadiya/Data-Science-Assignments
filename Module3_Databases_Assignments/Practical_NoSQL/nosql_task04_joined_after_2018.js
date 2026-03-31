// ─────────────────────────────────────────────────────────────────────────────
// NoSQL Task 4 — Find employees who joined after 2018
// Database   : company_db
// Collection : employees
// ─────────────────────────────────────────────────────────────────────────────

use company_db;

// ── Approach A: join_year stored as a Number ──────────────────────────────
db.employees.find(
    { join_year: { $gt: 2018 } }
).pretty();

// ── Approach B: join_date stored as an ISODate ────────────────────────────
db.employees.find(
    { join_date: { $gt: ISODate("2018-12-31T23:59:59Z") } }
).pretty();

// ── With projection ───────────────────────────────────────────────────────
db.employees.find(
    { join_year: { $gt: 2018 } },
    { name: 1, department: 1, salary: 1, join_year: 1, _id: 0 }
).sort({ join_year: 1 }).pretty();

// ── Count employees who joined after 2018 ────────────────────────────────
db.employees.countDocuments({ join_year: { $gt: 2018 } });

// ── Employees who joined in a specific range: 2019 to 2023 ───────────────
db.employees.find(
    { join_year: { $gte: 2019, $lte: 2023 } },
    { name: 1, department: 1, join_year: 1, _id: 0 }
).sort({ join_year: 1 });

// Explanation:
// join_year: { $gt: 2018 } returns documents where join_year is 2019, 2020, etc.
// If dates are stored as ISODate objects, compare using ISODate("YYYY-MM-DDT...")
//   so MongoDB performs a proper date comparison rather than a string comparison.
// $gt: 2018 means strictly AFTER 2018, i.e., 2019 onwards.
