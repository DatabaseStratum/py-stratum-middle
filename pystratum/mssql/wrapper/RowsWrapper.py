"""
PyStratum

Copyright 2015-2016 Set Based IT Consultancy

Licence MIT
"""
from pystratum.mssql.wrapper.MsSqlWrapper import MsSqlWrapper


# ----------------------------------------------------------------------------------------------------------------------
class RowsWrapper(MsSqlWrapper):
    """
    Wrapper method generator for stored procedures that are selecting 0, 1, or more rows.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def _write_result_handler(self, routine):
        self._write_line('return StaticDataLayer.execute_rows({0!s})'.format(self._generate_command(routine)))

# ----------------------------------------------------------------------------------------------------------------------
