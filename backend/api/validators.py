from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from croniter import croniter


def validate_cron(value):
    try:
        croniter(value)
        return True
    except:
        raise ValidationError(
            _("cron expression is not valid"),
            params={'value':value},
        )