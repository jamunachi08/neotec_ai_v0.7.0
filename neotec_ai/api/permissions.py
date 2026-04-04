import frappe

@frappe.whitelist()
def has_app_permission():
    return frappe.has_permission("Neotec AI Settings", "read") or frappe.session.user != "Guest"
