def generate_blueprint(prompt, source_name=None):
    return {
        "prompt": prompt,
        "source_name": source_name or "ERP Database",
        "kpis": ["Primary KPI", "Variance KPI", "Trend KPI"],
        "visuals": ["Trend line", "Category bar chart", "Exception table"],
        "filters": ["Company", "From Date", "To Date", "Business Dimension"],
        "notes": [
            "Review semantic mapping before production execution.",
            "Use approved query templates for external sources.",
        ]
    }
