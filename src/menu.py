# src/menu.py

def flatten_menu(node):
    """
    Flatten a nested menu structure into a list of item names.
    Node can be:
      - {"type": "item", "name": str}
      - {"type": "category", "name": str, "children": [nodes]}
      - otherwise, ignored
    """
    if not isinstance(node, dict):
        return []

    node_type = node.get("type")

    if node_type == "item":
        name = node.get("name")
        return [name] if isinstance(name, str) else []

    if node_type == "category":
        children = node.get("children", [])
        items = []
        if isinstance(children, list):
            for child in children:
                items.extend(flatten_menu(child))
        return items

    # any unknown/malformed node
    return []
