def resolve_voice_intent(text):
    text = (text or "").strip().lower()
    route_map = {
        "sales invoice": "/app/sales-invoice",
        "sales order": "/app/sales-order",
        "purchase order": "/app/purchase-order",
        "lead": "/app/lead",
        "project": "/app/project",
    }
    for key, route in route_map.items():
        if key in text:
            return {"intent": "open_route", "route": route, "spoken_text": text}
    if "report" in text:
        return {"intent": "open_report_area", "route": "/app/query-report", "spoken_text": text}
    return {"intent": "unknown", "route": "/app/neotec-ai-hub", "spoken_text": text}
