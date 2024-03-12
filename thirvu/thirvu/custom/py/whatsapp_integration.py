
import os
import json
import requests
import frappe
from frappe.model.document import Document


class SalesInvoiceWhatsApp(Document):
	pass


@frappe.whitelist()
def sales_invoice_in_whatsapp(invoice , customer):
	doc = invoice
	
	if(isinstance(invoice, str)):
		doc = frappe.get_doc("Sales Invoice", invoice)
		
	fcontent = frappe.get_print(doc=doc, as_pdf=1, no_letterhead=0 , print_format='Standard')
	pdf_file_name = "{0}.pdf".format(doc.name)

	_file = frappe.get_doc(
		{
			"doctype": "File",
			"file_name": pdf_file_name,
			"content": fcontent,

		}
	)
	_file.insert()
	
	if(frappe.db.get_single_value('WhatsApp Settings', 'disable') == 0 ):
		return send_whatsapp(
					media_url=frappe.utils.get_url()+_file.file_url,
					number=customer,
					doc=doc,
					message=doc.name,
					invoice=doc.name )
	return 'Disabled'
			
	
	

	
def send_whatsapp(media_url , number, message, doc, invoice=None):
	response=""


	access = frappe.db.get_single_value('WhatsApp Settings', 'access') 
	instance = frappe.db.get_single_value('WhatsApp Settings', 'instance_id') 
	url = frappe.db.get_single_value('WhatsApp Settings', 'url') 
	url_message = f"{url}number=+91{number}&type=media&message={message}&media_url={media_url}&filename={invoice}&instance_id={instance}&access_token={access}"
	payload={}
	headers = {}
	res = requests.request('GET', url_message)
	frappe.log_error(title="Whatsapp Invoice Success", message=f""" {media_url}\n{response}\n{url_message}\n""")


	response_text = res.text
	response_json = json.loads(response_text)
	message = response_json.get('message')



	return message