import frappe


def run_due_jobs():
    try:
        # Placeholder for future connector execution.
        # Safe no-op for install and scheduler stability.
        return []
    except Exception:
        frappe.log_error(frappe.get_traceback(), "Neotec AI CRM social scheduler failed")
        return []
