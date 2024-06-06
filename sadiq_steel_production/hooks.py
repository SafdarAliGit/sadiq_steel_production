from . import __version__ as app_version

app_name = "sadiq_steel_production"
app_title = "Sadiq Steel Production"
app_publisher = "VUT"
app_description = "Sadiq Steel Production"
app_email = "safdar211@gamil.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sadiq_steel_production/css/sadiq_steel_production.css"
# app_include_js = "/assets/sadiq_steel_production/js/sadiq_steel_production.js"

# include js, css files in header of web template
# web_include_css = "/assets/sadiq_steel_production/css/sadiq_steel_production.css"
# web_include_js = "/assets/sadiq_steel_production/js/sadiq_steel_production.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sadiq_steel_production/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "sadiq_steel_production.utils.jinja_methods",
#	"filters": "sadiq_steel_production.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sadiq_steel_production.install.before_install"
# after_install = "sadiq_steel_production.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sadiq_steel_production.uninstall.before_uninstall"
# after_uninstall = "sadiq_steel_production.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sadiq_steel_production.utils.before_app_install"
# after_app_install = "sadiq_steel_production.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sadiq_steel_production.utils.before_app_uninstall"
# after_app_uninstall = "sadiq_steel_production.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sadiq_steel_production.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"sadiq_steel_production.tasks.all"
#	],
#	"daily": [
#		"sadiq_steel_production.tasks.daily"
#	],
#	"hourly": [
#		"sadiq_steel_production.tasks.hourly"
#	],
#	"weekly": [
#		"sadiq_steel_production.tasks.weekly"
#	],
#	"monthly": [
#		"sadiq_steel_production.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "sadiq_steel_production.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "sadiq_steel_production.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "sadiq_steel_production.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sadiq_steel_production.utils.before_request"]
# after_request = ["sadiq_steel_production.utils.after_request"]

# Job Events
# ----------
# before_job = ["sadiq_steel_production.utils.before_job"]
# after_job = ["sadiq_steel_production.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"sadiq_steel_production.auth.validate"
# ]
