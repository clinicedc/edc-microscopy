from clinicedc_constants import MICROSCOPY, NO, NOT_APPLICABLE, PRESENT, YES
from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_microscopy.form_validators import MalariaTestFormValidator


class Test(TestCase):
    def test_ok(self):
        pass

    def test_form_validator(self):
        options = {
            "performed": YES,
            "diagnostic_type": MICROSCOPY,
            "not_performed_reason": "",
            "result": PRESENT,
        }
        form_validator = MalariaTestFormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f"ValidatinError unexpectedly rasise. Got {e}")

        options = {
            "performed": NO,
            "diagnostic_type": NOT_APPLICABLE,
            "not_performed_reason": "Did not feel like it",
            "result": NOT_APPLICABLE,
        }
        form_validator = MalariaTestFormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f"ValidatinError unexpectedly rasise. Got {e}")
