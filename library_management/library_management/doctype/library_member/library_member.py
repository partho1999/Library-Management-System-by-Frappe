# Copyright (c) 2024, Partho Protim Sarkar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

#this method will run every time a document is saved
class LibraryMember(Document):
	
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'
