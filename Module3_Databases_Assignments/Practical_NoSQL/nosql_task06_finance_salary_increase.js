// ─────────────────────────────────────────────────────────────────────────────
// NoSQL Task 6 — Increase the salary of all employees in the Finance
//                department by 5%
// Database   : company_db
// Collection : employees
// ─────────────────────────────────────────────────────────────────────────────

use company_db;

// ── Step 1: Preview affected records BEFORE updating ──────────────────────
db.employees.find(
    { department: "Finance" },
    { name: 1, department: 1, salary: 1, _id: 0 }
).pretty();

// ── Step 2: Perform the 5% salary increase ────────────────────────────────
// $mul multiplies the field value by the given factor.
// 1.05 = original salary × (1 + 5/100)
db.employees.updateMany(
    { department: "Finance" },        // filter — all Finance employees
    { $mul: { salary: 1.05 } }        // update — multiply salary by 1.05
);

// ── Step 3: Verify updated records ───────────────────────────────────────
db.employees.find(
    { department: "Finance" },
    { name: 1, department: 1, salary: 1, _id: 0 }
).pretty();

// ── Alternative using $set with a calculated value ────────────────────────
// (Use when you need to explicitly set a rounded value)
// db.employees.find({ department: "Finance" }).forEach(function(emp) {
//     db.employees.updateOne(
//         { _id: emp._id },
//         { $set: { salary: Math.round(emp.salary * 1.05 * 100) / 100 } }
//     );
// });

// Explanation:
// updateMany() applies the update to EVERY document matching the filter.
// $mul operator: { $mul: { salary: 1.05 } }
//   → new_salary = current_salary * 1.05   (a 5% increase)
// This is safer and more concise than $set because you do not need to
//   know the current value — MongoDB computes it atomically.
// The forEach alternative is useful when custom rounding is required.
