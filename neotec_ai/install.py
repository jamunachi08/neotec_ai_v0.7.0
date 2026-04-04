import frappe

SAFE_PROMPTS = [
    {"title": "Sales Summary Today", "prompt_text": "Show today sales summary with key KPIs and next actions.", "module_scope": "Selling", "prompt_type": "Insight", "is_system": 1},
    {"title": "Receivables Risk", "prompt_text": "Summarize overdue receivables and collection priorities.", "module_scope": "Accounts", "prompt_type": "Insight", "is_system": 1},
    {"title": "Inventory Status", "prompt_text": "Show stock exceptions, low stock items, and replenishment priorities.", "module_scope": "Stock", "prompt_type": "Insight", "is_system": 1},
    {"title": "Payroll Variance", "prompt_text": "Explain payroll variance and unusual deductions.", "module_scope": "HR", "prompt_type": "Insight", "is_system": 1},
]

FEATURES = [
    {"feature_name": "Universal Document AI", "app_name": "ERPNext", "module_name": "Core", "feature_type": "Document AI", "enabled": 1},
    {"feature_name": "Prompt to Report", "app_name": "ERPNext", "module_name": "Analytics", "feature_type": "BI", "enabled": 1},
    {"feature_name": "Voice Navigation", "app_name": "ERPNext", "module_name": "Core", "feature_type": "Voice", "enabled": 1},
]

def _safe_get_or_create_single(doctype):
    try:
        return frappe.get_single(doctype)
    except Exception:
        if frappe.db.exists("DocType", doctype):
            doc = frappe.get_doc({"doctype": doctype})
            doc.flags.ignore_permissions = True
            doc.insert(ignore_permissions=True)
            return frappe.get_single(doctype)
        return None

def _ensure_settings():
    settings = _safe_get_or_create_single("Neotec AI Settings")
    if settings:
        defaults = {
            "default_mode": getattr(settings, "default_mode", None) or "AI Chat",
            "allow_draft_actions": getattr(settings, "allow_draft_actions", 0),
            "enable_voice": getattr(settings, "enable_voice", 1),
            "enable_bi_mode": getattr(settings, "enable_bi_mode", 1),
            "enable_document_ai": getattr(settings, "enable_document_ai", 1),
        }
        for k, v in defaults.items():
            setattr(settings, k, v)
        settings.flags.ignore_permissions = True
        settings.save(ignore_permissions=True)

def _ensure_templates():
    if not frappe.db.exists("DocType", "Neotec AI Prompt Template"):
        return
    for row in SAFE_PROMPTS:
        if not frappe.db.exists("Neotec AI Prompt Template", {"title": row["title"]}):
            doc = frappe.get_doc({"doctype": "Neotec AI Prompt Template", **row})
            doc.flags.ignore_permissions = True
            doc.insert(ignore_permissions=True)

def _ensure_registry():
    if not frappe.db.exists("DocType", "Neotec AI Feature Registry"):
        return
    for row in FEATURES:
        if not frappe.db.exists("Neotec AI Feature Registry", {"feature_name": row["feature_name"]}):
            doc = frappe.get_doc({"doctype": "Neotec AI Feature Registry", **row})
            doc.flags.ignore_permissions = True
            doc.insert(ignore_permissions=True)

def after_install():
    _ensure_settings()
    _ensure_templates()
    _ensure_registry()

def after_migrate():
    after_install()
