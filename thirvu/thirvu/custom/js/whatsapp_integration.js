
frappe.ui.form.on("Sales Invoice", {

    refresh(frm) {
        console.log("dsagdyga")
      add_whatsApp_button(frm)
      
    }
})
  
  function add_whatsApp_button(frm) {
    if (frm.doc.docstatus === 1) {
      frm.add_custom_button("Send WhatsApp", function () {
        frappe.call({
          method: 'thirvu.thirvu.custom.py.whatsapp_integration.sales_invoice_in_whatsapp',
          args: {
            "invoice": frm.doc.name,
            "customer": frm.doc.custom_mobile_number
          },
          freeze: true,
          freeze_message: 'Sending....',
          callback: function (r) {
            if (r.message == 'Success')
              frappe.show_alert({
                message: __("WhatsApp Message sent Successfully"),
                indicator: "green",
              });
  
            else if (r.message == 'Disabled')
              frappe.show_alert({
                message: __("Please enable whatsApp Messaging"),
                indicator: "orange",
              });
  
            else
              frappe.show_alert({
                message: __("Message Not Sent !", r.message),
                indicator: "red",
              });
  
  
          }
  
        })
  
  
      }
  
  
      )
    }
  } 