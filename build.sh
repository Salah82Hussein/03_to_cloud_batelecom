#!/usr/bin/env bash
#!/usr/bin/env python

# exit on error
set -o errexit

import os
retval = os.getcwd()

poetry install

cd batelecom

python manage.py collectstatic --no-input
python manage.py migrate

os.chdir( retval )
