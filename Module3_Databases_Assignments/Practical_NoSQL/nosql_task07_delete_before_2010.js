// ─────────────────────────────────────────────────────────────────────────────
// NoSQL Task 7 — Delete employees who joined before 2010
// Database   : company_db
// Collection : employees
// ─────────────────────────────────────────────────────────────────────────────

use company_db;

// ── Step 1: Preview records that WILL be deleted ──────────────────────────
db.employees.find(
    { join_year: { $lt: 2010 } },
    { name: 1, department: 1, join_year: 1, _id: 0 }
).sort({ join_year: 1 }).pretty();

// ── Step 2: Count records to be deleted ──────────────────────────────────
db.employees.countDocuments({ join_year: { $lt: 2010 } });

// ── Step 3: Delete all employees who joined before 2010 ──────────────────
db.employees.deleteMany(
    { join_year: { $lt: 2010 } }
);

// ── Step 4: Verify deletion ───────────────────────────────────────────────
// This should return 0 after the delete
db.employees.countDocuments({ join_year: { $lt: 2010 } });

// ── Alternative: If join_date is stored as ISODate ────────────────────────
// db.employees.deleteMany(
//     { join_date: { $lt: ISODate("2010-01-01T00:00:00Z") } }
// );

// ── Safe pattern: Delete only one (for testing) ───────────────────────────
// db.employees.deleteOne({ join_year: { $lt: 2010 } });

// Explanation:
// deleteMany() removes ALL documents that match the given filter.
// { join_year: { $lt: 2010 } } matches join_year values 2009, 2008, 2007, etc.
// Always preview (find + count) before deleting to avoid accidental data loss.
// deleteOne() is safer when you want to remove just a single document.
// MongoDB deletes are permanent — consider a soft-delete pattern
//   (adding an { active: false } flag) for production systems.
