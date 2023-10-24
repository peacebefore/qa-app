# first: pip install pysqlite3-binary
# then in settings.py:

# these three lines swap the stdlib sqlite3 lib with the pysqlite3 package
import os
import sys
__import__('pysqlite3')

sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname('/Users/sundaeblues/Developer/ztm/qa_app'), 'db.sqlite3'),
    }
}
