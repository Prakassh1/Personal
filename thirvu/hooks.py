app_name = "thirvu"
app_title = "Thirvu"
app_publisher = "Prakash"
app_description = "Thirvu"
app_email = "prakasshprakassh65@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/thirvu/css/thirvu.css"
# app_include_js = "/assets/thirvu/js/thirvu.js"

# include js, css files in header of web template
# web_include_css = "/assets/thirvu/css/thirvu.css"
# web_include_js = "/assets/thirvu/js/thirvu.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "thirvu/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Sales Invoice" : "thirvu/custom/js/whatsapp_integration.js",
              "Item" : "thirvu/custom/js/batch_series.js"
              }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "thirvu.utils.jinja_methods",
# 	"filters": "thirvu.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "thirvu.install.before_install"
# after_install = "thirvu.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "thirvu.uninstall.before_uninstall"
# after_uninstall = "thirvu.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "thirvu.utils.before_app_install"
# after_app_install = "thirvu.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "thirvu.utils.before_app_uninstall"
# after_app_uninstall = "thirvu.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "thirvu.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Invoice": {
		"on_submit" : "thirvu.thirvu.custom.py.whatsapp_integration.sales_invoice_in_whatsapp"
	},
    "Batch":{
        "autoname": "thirvu.thirvu.custom.py.item_batch_series.set_batch_number"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"thirvu.tasks.all"
# 	],
# 	"daily": [
# 		"thirvu.tasks.daily"
# 	],
# 	"hourly": [
# 		"thirvu.tasks.hourly"
# 	],
# 	"weekly": [
# 		"thirvu.tasks.weekly"
# 	],
# 	"monthly": [
# 		"thirvu.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "thirvu.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "thirvu.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "thirvu.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["thirvu.utils.before_request"]
# after_request = ["thirvu.utils.after_request"]

# Job Events
# ----------
# before_job = ["thirvu.utils.before_job"]
# after_job = ["thirvu.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"thirvu.auth.validate"
# ]
