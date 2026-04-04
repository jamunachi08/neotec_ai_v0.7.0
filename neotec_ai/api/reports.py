import frappe
from neotec_ai.services.report_designer import generate_blueprint

@frappe.whitelist()
def design(prompt, source_name=None):
    return generate_blueprint(prompt, source_name=source_name)
