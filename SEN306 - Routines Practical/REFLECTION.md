# REFLECTION

## 1. How did you achieve functional cohesion?

Functional cohesion means a routine performs exactly one well-defined task.

The original processCustomer routine performed several unrelated tasks:

- Validation
- Order summation
- Discount calculation
- Total calculation
- Message creation
- Displaying output
- Sending email

To improve cohesion, I extracted the following routines:

- validate_customer()
- validate_customer_type()
- validate_orders()
- order_total()
- discount_rate()
- final_total()
- customer_message()
- display_message()
- send_email()

Each routine now has a single responsibility, making the design functionally cohesive.

## 2. What parameter-passing issues did you encounter?

The original routine contained:

    d = total

The intention appears to be updating the caller's variable.

However, this does not work.

In Python, numbers (int and float) are immutable and behave like pass-by-value. Assigning:

    d = total

only changes the local parameter inside the routine.

The caller's variable remains unchanged.

To solve this, I stored the result in:

    customer.total

inside the Customer object.

This makes the updated total available after the routine finishes.

## 3. How would the d update behave differently if the language used pass-by-value-result?

Pass-by-value-result uses:

1. Copy-in
2. Execute locally
3. Copy-out

When the routine begins, the value of d is copied into the parameter.

The routine modifies the local copy:

    d = total

When the routine finishes, the final value of d is copied back to the caller.

Therefore, under pass-by-value-result, the caller's variable would be updated automatically at the end of the call.

This differs from Python, where assigning to a parameter only changes the local variable and does not affect the caller.