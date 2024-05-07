
import frappe
from frappe import _


def get_tree_nodes(doctype, parent=None, is_root=True, user=None):
   
    filters = {"parent": parent}
    if not is_root:
        filters["is_group"] = 0

    
    nodes = frappe.get_all(doctype, filters=filters, fields=["name", "title", "is_group"])

    
    for node in nodes:
        node["children"] = get_tree_nodes(doctype, parent=node["name"], is_root=False, user=user)

    return nodes

@frappe.whitelist()
def get_tree_data(doctype):
    
    tree_data = get_tree_nodes(doctype)
    return tree_data
