import frappe
from frappe.model.document import Document
from datetime import datetime
from frappe.model.naming import make_autoname


# def generate_batch_number(item):
#     previous_month =0

#     now = datetime.now()
#     month=now.strftime("%m")
#     year=now.strftime("%y")
#     previous_month = month
#     counter=0
#     for i in range (1000):
#         if month != previous_month:
#             counter=1
#             previous_month = month

#         formatted_number = str(i).zfill(2)
#         counter+=1

#         return f"{item}-{formatted_number}{month}{year}"


def set_batch_number(doc, method):
    if doc.is_new():
        now = datetime.now()
        month=now.strftime("%m")
        year=now.strftime("%y")
        #doc.batch_id = generate_batch_number(doc.item)
        doc.name= make_autoname(f"{doc.item}.{month}.{year}.##.")
        doc.batch_id = doc.name






