import frappe


STARTER_TEMPLATES = [
    {
        "title": "Sales Summary Today",
        "prompt_text": "Show today sales summary with key KPIs and next actions.",
        "module_scope": "Selling",
        "prompt_type": "Insight",
        "is_system": 1,
    },
    {
        "title": "Receivables Risk",
        "prompt_text": "Summarize overdue receivables, collection risk, and suggested follow-ups.",
        "module_scope": "Accounts",
        "prompt_type": "Insight",
        "is_system": 1,
    },
    {
        "title": "Inventory Exceptions",
        "prompt_text": "Show shortages, fast movers, slow movers, and replenishment suggestions.",
        "module_scope": "Stock",
        "prompt_type": "Insight",
        "is_system": 1,
    },
    {
        "title": "HR Variance Review",
        "prompt_text": "Summarize attendance, leave, and payroll anomalies requiring attention.",
        "module_scope": "HR",
        "prompt_type": "Insight",
        "is_system": 1,
    },
]


def _doctype_ready(doctype: str) -> bool:
    try:
        if not frappe.db.exists("DocType", doctype):
            return False
        return bool(frappe.db.table_exists(f"tab{doctype}"))
    except Exception:
        frappe.log_error(frappe.get_traceback(), f"Neotec AI readiness check failed: {doctype}")
        return False


def _ensure_single_settings():
    doctype = "Neotec AI Settings"
    if not _doctype_ready(doctype):
        return

    try:
        if not frappe.db.exists(doctype, doctype):
            doc = frappe.get_doc({"doctype": doctype})
            doc.flags.ignore_mandatory = True
            doc.save(ignore_permissions=True)
            frappe.db.commit()
    except Exception:
        frappe.log_error(frappe.get_traceback(), "Neotec AI settings bootstrap failed")


def _ensure_templates():
    doctype = "Neotec AI Prompt Template"
    if not _doctype_ready(doctype):
        return

    for row in STARTER_TEMPLATES:
        try:
            if not frappe.db.exists(doctype, row["title"]):
                doc = frappe.get_doc({"doctype": doctype, **row})
                doc.insert(ignore_permissions=True)
        except Exception:
            frappe.log_error(
                frappe.get_traceback(),
                f"Neotec AI template insert failed: {row.get('title')}",
            )

    frappe.db.commit()


def after_install():
    # Keep install phase lightweight and safe.
    # Do not assume all tables are immediately queryable on every environment.
    pass


def after_migrate():
    _ensure_single_settings()
    _ensure_templates()
