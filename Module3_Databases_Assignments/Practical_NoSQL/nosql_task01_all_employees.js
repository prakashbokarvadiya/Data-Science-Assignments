// ─────────────────────────────────────────────────────────────────────────────
// NoSQL Task 1 — Retrieve all employee records
// Database   : company_db
// Collection : employees
// ─────────────────────────────────────────────────────────────────────────────

// Sample document structure in 'employees' collection:
// {
//   "_id"        : ObjectId("..."),
//   "emp_id"     : 1,
//   "name"       : "Alice Johnson",
//   "department" : "IT",
//   "salary"     : 75000,
//   "age"        : 32,
//   "join_year"  : 2019
// }

// ── Switch to the database ────────────────────────────────────────────────
use company_db;

// ── Query: Retrieve ALL employee records ──────────────────────────────────
db.employees.find({});

// ── Pretty-printed output ─────────────────────────────────────────────────
db.employees.find({}).pretty();

// ── Retrieve with selected fields only (projection) ───────────────────────
// Show all employees but only name, department, salary (exclude _id)
db.employees.find(
    {},                                         // filter  — empty = all documents
    { name: 1, department: 1, salary: 1, _id: 0 }  // projection
);

// ── Count total number of employees ──────────────────────────────────────
db.employees.countDocuments({});

// Explanation:
// find({}) with an empty filter document matches every document in the collection.
// .pretty() formats the JSON output for readability in the shell.
// Projection { field: 1 } includes a field; { field: 0 } excludes it.
// countDocuments({}) returns the total count without fetching all documents.
