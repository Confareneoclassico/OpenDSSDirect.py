# -*- coding: utf-8 -*-
from __future__ import absolute_import

from ._utils import CheckForError, api_util, Iterable


class IWireData(Iterable):
    """Experimental API extension exposing part of the WireData objects"""

    _api_prefix = "WireData"
    __slots__ = []
    _columns = [
        "Name",
        "Idx",
        "NormAmps",
        "EmergAmps",
        "Rdc",
        "Rac",
        "ResistanceUnits",
        "GMRac",
        "GMRUnits",
        "Radius",
        "Diameter",
        "RadiusUnits",
    ]

    def EmergAmps(self, *args):
        """Emergency ampere rating"""
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_EmergAmps()

        # Setter
        Value, = args
        self._lib.WireData_Set_EmergAmps(Value)
        self.CheckForError()

    def NormAmps(self, *args):
        """Normal Ampere rating"""
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_NormAmps()

        # Setter
        Value, = args
        self._lib.WireData_Set_NormAmps(Value)
        self.CheckForError()

    def Rdc(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_Rdc()

        # Setter
        Value, = args
        self._lib.WireData_Set_Rdc(Value)
        self.CheckForError()

    def Rac(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_Rac()

        # Setter
        Value, = args
        self._lib.WireData_Set_Rac(Value)
        self.CheckForError()

    def GMRac(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_GMRac()

        # Setter
        Value, = args
        self._lib.WireData_Set_GMRac(Value)
        self.CheckForError()

    def GMRUnits(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_GMRUnits()

        # Setter
        Value, = args
        self._lib.WireData_Set_GMRUnits(Value)
        self.CheckForError()

    def Radius(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_Radius()

        # Setter
        Value, = args
        self._lib.WireData_Set_Radius(Value)
        self.CheckForError()

    def RadiusUnits(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_RadiusUnits()

        # Setter
        Value, = args
        self._lib.WireData_Set_RadiusUnits(Value)
        self.CheckForError()

    def ResistanceUnits(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_ResistanceUnits()

        # Setter
        Value, = args
        self._lib.WireData_Set_ResistanceUnits(Value)
        self.CheckForError()

    def Diameter(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.WireData_Get_Diameter()

        # Setter
        Value, = args
        self._lib.WireData_Set_Diameter(Value)
        self.CheckForError()


_WireData = IWireData(api_util)

# For backwards compatibility, bind to the default instance
EmergAmps = _WireData.EmergAmps
NormAmps = _WireData.NormAmps
Rdc = _WireData.Rdc
Rac = _WireData.Rac
GMRac = _WireData.GMRac
GMRUnits = _WireData.GMRUnits
Radius = _WireData.Radius
RadiusUnits = _WireData.RadiusUnits
ResistanceUnits = _WireData.ResistanceUnits
Diameter = _WireData.Diameter
Idx = _WireData.Idx
First = _WireData.First
Next = _WireData.Next
AllNames = _WireData.AllNames
Count = _WireData.Count
Name = _WireData.Name
_columns = _WireData._columns
__all__ = [
    "EmergAmps",
    "NormAmps",
    "Rdc",
    "Rac",
    "GMRac",
    "GMRUnits",
    "Radius",
    "RadiusUnits",
    "ResistanceUnits",
    "Diameter",
    "Idx",
    "First",
    "Next",
    "AllNames",
    "Count",
    "Name",
]
