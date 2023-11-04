# Copyright (c) 2023, Douglas Nkubitu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from mvim.qr_code import get_qr_code

class MotorVehicleInsuranceCertificate(Document):
	def validate(self):
		self.qr_code = get_qr_code(
			self.vehicle_registration_no,
			# self.policy_type,
			# self.chasis_no
		)