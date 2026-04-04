frappe.pages['neotec-ai-hub'].on_page_load = function(wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Neotec AI Hub',
        single_column: true
    });
    neotec_ai.renderHub(page.main);
};
