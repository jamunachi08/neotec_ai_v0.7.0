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

FEATURES = [
    {"feature_name": "Universal Document AI", "app_name": "ERPNext", "module_name": "Core", "feature_type": "Document AI", "enabled": 1},
    {"feature_name": "Prompt to Report", "app_name": "ERPNext", "module_name": "Analytics", "feature_type": "BI", "enabled": 1},
    {"feature_name": "Voice Navigation", "app_name": "ERPNext", "module_name": "Core", "feature_type": "Voice", "enabled": 1},
]


def _table_ready(doctype: str) -> bool:
    try:
        if not frappe.db.exists("DocType", doctype):
            return False
        return bool(frappe.db.table_exists(f"tab{doctype}"))
    except Exception:
        frappe.log_error(frappe.get_traceback(), f"Neotec AI readiness check failed: {doctype}")
        return False


def _ensure_settings():
    doctype = "Neotec AI Settings"
    if not _table_ready(doctype):
        return
    try:
        if not frappe.db.exists(doctype, doctype):
            doc = frappe.get_doc({"doctype": doctype})
            doc.flags.ignore_mandatory = True
            doc.insert(ignore_permissions=True)
    except Exception:
        frappe.log_error(frappe.get_traceback(), "Neotec AI settings bootstrap failed")


def _ensure_templates():
    doctype = "Neotec AI Prompt Template"
    if not _table_ready(doctype):
        return
    for row in STARTER_TEMPLATES:
        try:
            if not frappe.db.exists(doctype, {"title": row["title"]}):
                doc = frappe.get_doc({"doctype": doctype, **row})
                doc.insert(ignore_permissions=True)
        except Exception:
            frappe.log_error(frappe.get_traceback(), f"Neotec AI template insert failed: {row.get('title')}")


def _ensure_registry():
    doctype = "Neotec AI Feature Registry"
    if not _table_ready(doctype):
        return
    for row in FEATURES:
        try:
            if not frappe.db.exists(doctype, {"feature_name": row["feature_name"]}):
                doc = frappe.get_doc({"doctype": doctype, **row})
                doc.insert(ignore_permissions=True)
        except Exception:
            frappe.log_error(frappe.get_traceback(), f"Neotec AI feature registry insert failed: {row.get('feature_name')}")


def after_install():
    # Keep installation lightweight and do not seed child tables too early.
    pass


def after_migrate():
    _ensure_settings()
    _ensure_templates()
    _ensure_registry()
