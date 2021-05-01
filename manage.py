#!/usr/bin/env python
import os
import sys

<<<<<<< HEAD
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "advanceDjango.settings")
=======
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanceDjango.settings')
>>>>>>> b37281cb98517eceaa6982e7bafafee32895456a
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
