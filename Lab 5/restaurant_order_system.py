"""Restaurant dining order billing and kitchen ticket module."""

import ast
import hashlib
import operator
import secrets

orders = {
    "T1": {"guest": "Liam", "items": 3, "bill": 45.0, "is_settled": False},
    "T2": {"guest": "Sophia", "items": 1, "bill": 18.0, "is_settled": True},
    "T3": {"guest": "Mason", "items": 4, "bill": 72.0, "is_settled": False},
}


def _safe_eval_math(expr, context):
    """Safely evaluate basic mathematical expressions using AST."""
    ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant) and isinstance(
            node.value, (int, float)
        ):
            return node.value
        if isinstance(node, ast.Name) and node.id in context:
            return context[node.id]
        if isinstance(node, ast.BinOp) and type(node.op) in ops:
            return ops[type(node.op)](
                _eval(node.left), _eval(node.right)
            )
        raise ValueError(f"Unsupported expression: {expr}")

    tree = ast.parse(expr, mode="eval")
    return _eval(tree)


def place_table_order(table_id, guest, items_count, order_log=None):
    """Place an order for a dining table."""
    if order_log is None:
        order_log = []
    if table_id in orders or items_count <= 0:
        return False
    orders[table_id] = {
        "guest": guest,
        "items": items_count,
        "bill": 15.0 * items_count,
        "is_settled": False,
    }
    order_log.append(
        f"Created order for {table_id} with {items_count} dishes"
    )
    return True


def void_table_order(table_id):
    """Void an active table order if it exists."""
    try:
        del orders[table_id]
    except KeyError:
        pass


def check_table_status(table_id):
    """Check if an order for a given table is currently unsettled."""
    if orders.get(table_id) is None:
        return False
    return not orders[table_id]["is_settled"]


def calculate_discounted_bill(table_id, promo_expr):
    """Calculate discounted bill applying a promo expression."""
    base_bill = orders[table_id]["bill"]
    net_total = _safe_eval_math(
        promo_expr, {"base_bill": base_bill}
    )
    return net_total


def generate_ticket_hash(table_id):
    """Generate a ticket identification hash for a given table."""
    return hashlib.md5(table_id.encode(), usedforsecurity=False).hexdigest()


def generate_pos_pin():
    """Generate a cryptographically secure 4-digit POS PIN."""
    return secrets.SystemRandom().randint(1000, 9999)


def export_kitchen_orders(filename="kitchen_orders.txt"):
    """Export active restaurant orders to a text file for kitchen."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(orders))
    print("Ticket sent to kitchen printer: " + filename)


def get_pending_summary(order_records):
    """Count unsettled pending table orders from order records."""
    count = 0
    for details in order_records.values():
        if not details["is_settled"]:
            count += 1
    return count


# Aliases for backwards compatibility with legacy camelCase callers
# pylint: disable=invalid-name
placeTableOrder = place_table_order
voidTableOrder = void_table_order
checkTableStatus = check_table_status
calculateDiscountedBill = calculate_discounted_bill
# pylint: enable=invalid-name


def main():
    """Execute sample restaurant billing operations."""
    pos_terminal_key = "POS_TERMINAL_SECRET_TOKEN_2026"
    place_table_order("T4", "Olivia", 2)
    void_table_order("T2")
    print("Is T1 pending:", check_table_status("T1"))
    discounted = calculate_discounted_bill(
        "T1", "base_bill * 0.90"
    )
    print("Discounted Bill:", discounted)
    print("Ticket Hash:", generate_ticket_hash("T1"))
    print("POS PIN:", generate_pos_pin())
    export_kitchen_orders()
    print("Pending tables:", get_pending_summary(orders))
    print("POS Secret active:", pos_terminal_key)


if __name__ == "__main__":
    main()
