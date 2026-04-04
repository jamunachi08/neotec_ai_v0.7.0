import frappe

@frappe.whitelist()
def register_job(source_type, title=None, payload_reference=None):
    if not frappe.db.exists("DocType", "Neotec AI Ingestion Job"):
        return {"ok": False, "message": "Ingestion Job DocType not available"}
    doc = frappe.get_doc({
        "doctype": "Neotec AI Ingestion Job",
        "source_type": source_type,
        "title": title or f"{source_type} intake",
        "status": "Queued",
        "payload_reference": payload_reference,
    })
    doc.flags.ignore_permissions = True
    doc.insert(ignore_permissions=True)
    return {"ok": True, "name": doc.name}
