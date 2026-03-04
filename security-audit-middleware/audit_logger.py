import logging
from functools import wraps

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def audit_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"AUDIT | Target: '{func.__name__}' | Payload: args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@audit_log
def process_payment(user_id, amount):
    print(f"Processing payment of R${amount} for user {user_id}")
@audit_log
def delete_user(user_id):
    print(f"User {user_id} deleted from database.")



def main():
    process_payment(99, 150.50)
    delete_user(99)

if __name__ == "__main__":
    main()
