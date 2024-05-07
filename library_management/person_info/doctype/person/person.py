# Copyright (c) 2024, Partho Protim Sarkar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class person(Document):


	def a_time_taking_process(self):
		import math
		var = math.factorial(20000)
		print("working............")
		frappe.publish_realtime("msgprint", "time taking precess completed", user=frappe.session.user)
		

	def before_save(self):
		# # get an existing document
		# doc = frappe.get_doc('Task', 'Task-00002')
		# doc.title = 'Test'
		# doc.save()	

		# # get a single doctype
		# doc = frappe.get_doc('System Settings')
		# doc.timezone
  
		# doc = frappe.get_doc({
		# 	'doctype': 'Task',
		# 	'title': 'New Task'
		# })
		# doc.insert()

		# user = frappe.get_doc(doctype='Task', title='test@example.com')
		# user.insert() 
  
		# get the last Task created
		task = frappe.get_last_doc('Task')
		

		# frappe.enqueue(
		# 	self.a_time_taking_process(), queue='short')
		# frappe.msgprint('start the enqueue processes',alert=True)
		
		

