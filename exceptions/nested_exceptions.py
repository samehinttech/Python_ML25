"""
Script for learning nested exception handling.
The idea is to observe the flow and how exceptions are propagated and handled in nested try-except blocks.
The code itself does not perform any meaningful computation.
"""


def nested_exceptions():
    try:
        print("This is the outer try block.")
        try:
            print("This is the inner try block.")
            x = 1 / 0  # This will raise a ZeroDivisionError
        except ZeroDivisionError:
            print("Caught a ZeroDivisionError in the inner except block.")
            # This will raise a ValueError but is not caught here as the ZeroDivisionError was
            # already caught first
            y = int("not_a_number")
        except ValueError:
            print("Caught a ValueError in the inner except block.")
            # This will raise a generic Exception as the ZeroDivisionError was already caught
        else:
            print("No exceptions occurred in the inner try block.")
        finally:
            print("This is the inner finally block.")
    except Exception as e:
        print(f"Caught an exception in the outer except block: {e}")
    else:
        print("No exceptions occurred in the outer try block.")
    finally:
        print("This is the outer finally block.")

    print("End of nested_exceptions function.")


nested_exceptions()