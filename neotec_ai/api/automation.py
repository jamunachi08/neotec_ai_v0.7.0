import frappe

@frappe.whitelist()
def recipe_cards():
    return [
        {"title": "Create follow-up task", "description": "Draft a task from the current record context."},
        {"title": "Draft approval note", "description": "Summarize current record for approver review."},
        {"title": "Generate customer update", "description": "Create communication draft from order/invoice/project context."},
    ]
