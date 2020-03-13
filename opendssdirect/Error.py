# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import api_util, Base


class IError(Base):
    __slots__ = []
    _api_prefix = "Error"
    _columns = ["Description", "Number", "EarlyAbort"]

    def Description(self):
        """(read-only) Description of error for last operation"""
        return self._get_string(self._lib.Error_Get_Description())

    def Number(self):
        """(read-only) Error Number (returns current value and then resets to zero)"""
        return self._lib.Error_Get_Number()

    def EarlyAbort(self, *args):
        """
    EarlyAbort controls whether all errors halts the DSS script processing (Compile/Redirect), defaults to True.
    """
        # Getter
        if len(args) == 0:
            return self._lib.Error_Get_EarlyAbort() != 0

        # Setter
        Value, = args
        self._lib.Error_Set_EarlyAbort(Value)


_Error = IError(api_util)

# For backwards compatibility, bind to the default instance
Description = _Error.Description
Number = _Error.Number
EarlyAbort = _Error.EarlyAbort
_columns = _Error._columns
__all__ = ["Description", "Number", "EarlyAbort"]
