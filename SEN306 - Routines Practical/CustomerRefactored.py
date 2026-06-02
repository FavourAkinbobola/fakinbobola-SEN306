VALID_CUSTOMER_TYPES = [1, 2]

class Customer:
    def __init__(self, name, address, customer_type,
                 email, is_vip, orders):
        self.name = name
        self.address = address
        self.customer_type = customer_type
        self.email = email
        self.is_vip = is_vip
        self.orders = orders
        self.total = 0.0

def validate_customer(customer):
    validate_customer_type(customer.customer_type)
    validate_orders(customer.orders)

def validate_customer_type(customer_type):
    if customer_type not in VALID_CUSTOMER_TYPES:
        raise ValueError(
            f"Invalid customer type: {customer_type}. "
            "Valid types are 1 and 2."
        )

def validate_orders(orders):
    for order in orders:
        if order < 0:
            raise ValueError(
                "Order values must be non-negative."
            )

def order_total(orders):
    return sum(orders)

def discount_rate(customer_type):
    if customer_type == 1:
        return 0.10
    elif customer_type == 2:
        return 0.20

    return 0.0

def final_total(total, rate):
    return total - (total * rate)

def customer_message(customer):
    message = (
        f"Hello {customer.name} of "
        f"{customer.address}, "
        f"your total is {customer.total:.2f}"
    )

    if customer.is_vip:
        message += " (VIP)"

    return message

def display_message(message):
    print(message)

def send_email(email, message):
    if email:
        print(f"Email sent to {email}")
        # Actual email logic would go here

def process_customer(customer):

    validate_customer(customer)

    total = order_total(customer.orders)

    rate = discount_rate(
        customer.customer_type
    )

    customer.total = final_total(
        total,
        rate
    )

    message = customer_message(customer)

    display_message(message)

    send_email(
        customer.email,
        message
    )

if __name__ == "__main__":

    customer = Customer(
        name="John",
        address="Lagos",
        customer_type=1,
        email="john@email.com",
        is_vip=True,
        orders=[100, 250, 150]
    )
    process_customer(customer)