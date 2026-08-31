from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.mysql.features import DatabaseFeatures

# Disable version check
BaseDatabaseWrapper.check_database_version_supported = lambda self: None

# Completely disable RETURNING for older MariaDB (10.4)
DatabaseFeatures.can_return_rows_from_bulk_insert = False
DatabaseFeatures.has_insert_returning = False
DatabaseFeatures.can_return_columns_from_insert = False