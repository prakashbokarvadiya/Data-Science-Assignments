// ─────────────────────────────────────────────────────────────────────────────
// NoSQL Task 5 — Find employees between the ages of 30 and 40
// Database   : company_db
// Collection : employees
// ─────────────────────────────────────────────────────────────────────────────

use company_db;

// ── Query: age >= 30 AND age <= 40 ────────────────────────────────────────
db.employees.find(
    { age: { $gte: 30, $lte: 40 } }
).pretty();

// ── With projection ───────────────────────────────────────────────────────
db.employees.find(
    { age: { $gte: 30, $lte: 40 } },
    { name: 1, department: 1, age: 1, salary: 1, _id: 0 }
).sort({ age: 1 }).pretty();

// ── Count employees in this age range ────────────────────────────────────
db.employees.countDocuments({ age: { $gte: 30, $lte: 40 } });

// ── Combined filter: IT department AND age 30-40 ─────────────────────────
db.employees.find(
    {
        department : "IT",
        age        : { $gte: 30, $lte: 40 }
    },
    { name: 1, department: 1, age: 1, _id: 0 }
).sort({ age: 1 });

// ── Using $and explicitly (equivalent to above) ───────────────────────────
db.employees.find(
    {
        $and: [
            { age: { $gte: 30 } },
            { age: { $lte: 40 } }
        ]
    }
);

// Explanation:
// $gte (>=) and $lte (<=) on the same field create an inclusive range filter.
// Both operators inside one field object automatically form an implicit AND.
// The explicit $and array is useful when applying multiple conditions
//   to different fields or when conditions on the same field cannot be merged.
