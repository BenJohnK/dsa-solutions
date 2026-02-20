# A sample snippet to demonstrate how to acheive idempotency in a webhook api that might trigger more than one time for "succes"

from app.database.models import Transaction
from app.database.db_connection import get_db

def handle_webhook(request, db: get_db()):
    event = request.event_type
    order_id = request.data.order_id
    if event == "payment.success":
        transaction = db.query(Transaction).filter_by(order_id=order_id).with_for_update().first() # Lock the transaction row for race conditions between requests.
        if transaction.status == "success":
            return "already processed"
        else:
            transaction.status = "success"
            db.commit()
            db.refresh()
            # Allocate the resource to the user by calling an async celery task
        
        

