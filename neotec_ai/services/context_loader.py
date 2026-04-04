import frappe

def load_doc_context(doctype=None, docname=None):
    if not doctype or not docname:
        return {}
    if not frappe.db.exists(doctype, docname):
        return {"doctype": doctype, "name": docname, "exists": False}
    doc = frappe.get_doc(doctype, docname)
    visible = {}
    for field in doc.meta.fields:
        if field.fieldtype in ("Section Break", "Column Break", "Tab Break", "Table", "Table MultiSelect", "HTML", "Button"):
            continue
        visible[field.fieldname] = doc.get(field.fieldname)
    return {"doctype": doctype, "name": docname, "exists": True, "fields": visible}
