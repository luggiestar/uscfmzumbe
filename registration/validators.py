from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'[0][6-9][0-9]{8}',
    message="Phone number must be entered in the format: '0.....'. Up to 10 digits allowed."
)

year_name = RegexValidator(
    regex=r'^\d{4}/\d{4}$',
    message="Invalid year format. Use 'YYYY/YYYY' format."
)


# validate that he left part is less that right part
def validate_year_order(value):
    part = value.split('/')
    if int(part[0]) > int(part[1]):
        raise ValidationError("Invalid year format. Left part must be less than right part.")
