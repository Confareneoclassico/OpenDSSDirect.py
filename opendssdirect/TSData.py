# -*- coding: utf-8 -*-
from __future__ import absolute_import

from ._utils import CheckForError, api_util, Iterable


class ITSData(Iterable):
    """Experimental API extension exposing TSData objects"""

    _api_prefix = "TSData"
    __slots__ = []
    _columns = [
        "Name",
        "Idx",
        "NormAmps",
        "EmergAmps",
        "Rdc",
        "Rac",
        "GMRac",
        "GMRUnits",
        "Radius",
        "RadiusUnits",
        "ResistanceUnits",
        "Diameter",
        "TapeLayer",
        "TapeLap",
        "DiaShield",
        "DiaCable",
        "DiaIns",
        "InsLayer",
        "EpsR",
    ]

    def EmergAmps(self, *args):
        """Emergency ampere rating"""
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_EmergAmps()

        # Setter
        Value, = args
        self._lib.TSData_Set_EmergAmps(Value)
        self.CheckForError()

    def NormAmps(self, *args):
        """Normal Ampere rating"""
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_NormAmps()

        # Setter
        Value, = args
        self._lib.TSData_Set_NormAmps(Value)
        self.CheckForError()

    def Rdc(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_Rdc()

        # Setter
        Value, = args
        self._lib.TSData_Set_Rdc(Value)
        self.CheckForError()

    def Rac(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_Rac()

        # Setter
        Value, = args
        self._lib.TSData_Set_Rac(Value)
        self.CheckForError()

    def GMRac(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_GMRac()

        # Setter
        Value, = args
        self._lib.TSData_Set_GMRac(Value)
        self.CheckForError()

    def GMRUnits(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_GMRUnits()

        # Setter
        Value, = args
        self._lib.TSData_Set_GMRUnits(Value)
        self.CheckForError()

    def Radius(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_Radius()

        # Setter
        Value, = args
        self._lib.TSData_Set_Radius(Value)
        self.CheckForError()

    def RadiusUnits(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_RadiusUnits()

        # Setter
        Value, = args
        self._lib.TSData_Set_RadiusUnits(Value)
        self.CheckForError()

    def ResistanceUnits(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_ResistanceUnits()

        # Setter
        Value, = args
        self._lib.TSData_Set_ResistanceUnits(Value)
        self.CheckForError()

    def Diameter(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_Diameter()

        # Setter
        Value, = args
        self._lib.TSData_Set_Diameter(Value)
        self.CheckForError()

    def EpsR(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_EpsR()

        # Setter
        Value, = args
        self._lib.TSData_Set_EpsR(Value)
        self.CheckForError()

    def InsLayer(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_InsLayer()

        # Setter
        Value, = args
        self._lib.TSData_Set_InsLayer(Value)
        self.CheckForError()

    def DiaIns(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_DiaIns()

        # Setter
        Value, = args
        self._lib.TSData_Set_DiaIns(Value)
        self.CheckForError()

    def DiaCable(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_DiaCable()

        # Setter
        Value, = args
        self._lib.TSData_Set_DiaCable(Value)
        self.CheckForError()

    def DiaShield(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_DiaShield()

        # Setter
        Value, = args
        self._lib.TSData_Set_DiaShield(Value)
        self.CheckForError()

    def TapeLayer(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_TapeLayer()

        # Setter
        Value, = args
        self._lib.TSData_Set_TapeLayer(Value)
        self.CheckForError()

    def TapeLap(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.TSData_Get_TapeLap()

        # Setter
        Value, = args
        self._lib.TSData_Set_TapeLap(Value)
        self.CheckForError()


_TSData = ITSData(api_util)

# For backwards compatibility, bind to the default instance
EmergAmps = _TSData.EmergAmps
NormAmps = _TSData.NormAmps
Rdc = _TSData.Rdc
Rac = _TSData.Rac
GMRac = _TSData.GMRac
GMRUnits = _TSData.GMRUnits
Radius = _TSData.Radius
RadiusUnits = _TSData.RadiusUnits
ResistanceUnits = _TSData.ResistanceUnits
Diameter = _TSData.Diameter
EpsR = _TSData.EpsR
InsLayer = _TSData.InsLayer
DiaIns = _TSData.DiaIns
DiaCable = _TSData.DiaCable
DiaShield = _TSData.DiaShield
TapeLayer = _TSData.TapeLayer
TapeLap = _TSData.TapeLap
Idx = _TSData.Idx
First = _TSData.First
Next = _TSData.Next
AllNames = _TSData.AllNames
Count = _TSData.Count
Name = _TSData.Name
_columns = _TSData._columns
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
    "EpsR",
    "InsLayer",
    "DiaIns",
    "DiaCable",
    "DiaShield",
    "TapeLayer",
    "TapeLap",
    "Idx",
    "First",
    "Next",
    "AllNames",
    "Count",
    "Name",
]
