# -*- coding: utf-8 -*-
from __future__ import absolute_import

from ._utils import codec, CheckForError, api_util, Iterable


class ILines(Iterable):
    __slots__ = []
    _api_prefix = "Lines"
    _columns = [
        "Name",
        "Idx",
        "Phases",
        "Bus1",
        "Bus2",
        "LineCode",
        "Geometry",
        "Length",
        "IsSwitch",
        "Parent",
        "Spacing",
        "EmergAmps",
        "NormAmps",
        "SeasonRating",
        "Yprim",
        "NumCust",
        "TotalCust",
        "Rho",
        "R0",
        "R1",
        "X0",
        "X1",
        "Rg",
        "Xg",
        "C0",
        "C1",
        "RMatrix",
        "XMatrix",
        "CMatrix",
        "Units",
    ]

    def New(self, Name):
        if type(Name) is not bytes:
            Name = Name.encode(self._api_util.codec)
        return self._lib.Lines_New(Name)

    def Bus1(self, *args):
        """Name of bus for terminal 1."""
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.Lines_Get_Bus1())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.Lines_Set_Bus1(Value)
        self.CheckForError()

    def Bus2(self, *args):
        """Name of bus for terminal 2."""
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.Lines_Get_Bus2())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.Lines_Set_Bus2(Value)
        self.CheckForError()

    def C0(self, *args):
        """Zero Sequence capacitance, nanofarads per unit length."""
        # Getter
        if len(args) == 0:
            return self._lib.Lines_Get_C0()

        # Setter
        Value, = args
        self._lib.Lines_Set_C0(Value)
        self.CheckForError()

    def C1(self, *args):
        """Positive Sequence capacitance, nanofarads per unit length."""
        # Getter
        if len(args) == 0:
            return self._lib.Lines_Get_C1()

        # Setter
        Value, = args
        self._lib.Lines_Set_C1(Value)
        self.CheckForError()

    def CMatrix(self, *args):
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.Lines_Get_Cmatrix)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Lines_Set_Cmatrix(ValuePtr, ValueCount)
        self.CheckForError()

    def EmergAmps(self, *args):
        """Emergency (maximum) ampere rating of Line."""
        # Getter
        if len(args) == 0:
            return self._lib.Lines_Get_EmergAmps()

        # Setter
        Value, = args
        self._lib.Lines_Set_EmergAmps(Value)
        self.CheckForError()

    def Geometry(self, *args):
        """Line geometry code"""
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.Lines_Get_Geometry())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.Lines_Set_Geometry(Value)
        self.CheckForError()

    def Length(self, *args):
        """Length of line section in units compatible with the LineCode definition."""
        # Getter
        if len(args) == 0:
            return self._lib.Lines_Get_Length()

        # Setter
        Value, = args
        self._lib.Lines_Set_Length(Value)
        self.CheckForError()

    def LineCode(self, *args):
        """Name of LineCode object that defines the impedances."""
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.Lines_Get_LineCode())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.Lines_Set_LineCode(Value)
        self.CheckForError()

    def NormAmps(self, *args):
        """Normal ampere rating of Line."""
        # Getter
        if len(args) == 0:
            return self._lib.Lines_Get_NormAmps()

        # Setter
        Value, = args
        self._lib.Lines_Set_NormAmps(Value)
        self.CheckForError()

    def NumCust(self):
        """(read-only) Number of customers on this line section."""
        return self._lib.Lines_Get_NumCust()

    def Parent(self):
        """(read-only) Sets Parent of the active Line to be the active line. Returns 0 if no parent or action fails."""
        return self._lib.Lines_Get_Parent()

    def Phases(self, *args):
        """Number of Phases, this Line element."""
        # Getter
        if len(args) == 0:
            return self._lib.Lines_Get_Phases()

        # Setter
        Value, = args
        self._lib.Lines_Set_Phases(Value)
        self.CheckForError()

    def R0(self, *args):
        """Zero Sequence resistance, ohms per unit length."""
        # Getter
        if len(args) == 0:
            return self._lib.Lines_Get_R0()

        # Setter
        Value, = args
        self._lib.Lines_Set_R0(Value)
        self.CheckForError()

    def R1(self, *args):
        """Positive Sequence resistance, ohms per unit length."""
        # Getter
        if len(args) == 0:
            return self._lib.Lines_Get_R1()

        # Setter
        Value, = args
        self._lib.Lines_Set_R1(Value)
        self.CheckForError()

    def Rg(self, *args):
        """Earth return resistance value used to compute line impedances at power frequency"""
        # Getter
        if len(args) == 0:
            return self._lib.Lines_Get_Rg()

        # Setter
        Value, = args
        self._lib.Lines_Set_Rg(Value)
        self.CheckForError()

    def Rho(self, *args):
        """Earth Resistivity, m-ohms"""
        # Getter
        if len(args) == 0:
            return self._lib.Lines_Get_Rho()

        # Setter
        Value, = args
        self._lib.Lines_Set_Rho(Value)
        self.CheckForError()

    def RMatrix(self, *args):
        """Resistance matrix (full), ohms per unit length. Array of doubles."""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.Lines_Get_Rmatrix)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Lines_Set_Rmatrix(ValuePtr, ValueCount)
        self.CheckForError()

    def Spacing(self, *args):
        """Line spacing code"""
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.Lines_Get_Spacing())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.Lines_Set_Spacing(Value)
        self.CheckForError()

    def TotalCust(self):
        """(read-only) Total Number of customers served from this line section."""
        return self._lib.Lines_Get_TotalCust()

    def Units(self, *args):
        # Getter
        if len(args) == 0:
            return self._lib.Lines_Get_Units()

        # Setter
        Value, = args
        self._lib.Lines_Set_Units(Value)
        self.CheckForError()

    def X0(self, *args):
        """Zero Sequence reactance ohms per unit length."""
        # Getter
        if len(args) == 0:
            return self._lib.Lines_Get_X0()

        # Setter
        Value, = args
        self._lib.Lines_Set_X0(Value)
        self.CheckForError()

    def X1(self, *args):
        """Positive Sequence reactance, ohms per unit length."""
        # Getter
        if len(args) == 0:
            return self._lib.Lines_Get_X1()

        # Setter
        Value, = args
        self._lib.Lines_Set_X1(Value)
        self.CheckForError()

    def Xg(self, *args):
        """Earth return reactance value used to compute line impedances at power frequency"""
        # Getter
        if len(args) == 0:
            return self._lib.Lines_Get_Xg()

        # Setter
        Value, = args
        self._lib.Lines_Set_Xg(Value)
        self.CheckForError()

    def XMatrix(self, *args):
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.Lines_Get_Xmatrix)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Lines_Set_Xmatrix(ValuePtr, ValueCount)
        self.CheckForError()

    def Yprim(self, *args):
        """Yprimitive: Does Nothing at present on Put; Dangerous"""
        # Getter
        if len(args) == 0:
            return self._get_float64_array(self._lib.Lines_Get_Yprim)

        # Setter
        Value, = args
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Lines_Set_Yprim(ValuePtr, ValueCount)
        self.CheckForError()

    def SeasonRating(self):
        """Delivers the rating for the current season (in Amps)  if the "SeasonalRatings" option is active"""
        return self._lib.Lines_Get_SeasonRating()

    def IsSwitch(self, *args):
        """Sets/gets the Line element switch status. Setting it has side-effects to the line parameters."""
        # Getter
        if len(args) == 0:
            return self._lib.Lines_Get_IsSwitch() != 0

        # Setter
        Value, = args
        self._lib.Lines_Set_IsSwitch(Value)


_Lines = ILines(api_util)

# For backwards compatibility, bind to the default instance
New = _Lines.New
AllNames = _Lines.AllNames
Bus1 = _Lines.Bus1
Bus2 = _Lines.Bus2
C0 = _Lines.C0
C1 = _Lines.C1
CMatrix = _Lines.CMatrix
Count = _Lines.Count
EmergAmps = _Lines.EmergAmps
First = _Lines.First
Geometry = _Lines.Geometry
Length = _Lines.Length
LineCode = _Lines.LineCode
Name = _Lines.Name
Next = _Lines.Next
NormAmps = _Lines.NormAmps
NumCust = _Lines.NumCust
Parent = _Lines.Parent
Phases = _Lines.Phases
R0 = _Lines.R0
R1 = _Lines.R1
Rg = _Lines.Rg
Rho = _Lines.Rho
RMatrix = _Lines.RMatrix
Spacing = _Lines.Spacing
TotalCust = _Lines.TotalCust
Units = _Lines.Units
X0 = _Lines.X0
X1 = _Lines.X1
Xg = _Lines.Xg
XMatrix = _Lines.XMatrix
Yprim = _Lines.Yprim
SeasonRating = _Lines.SeasonRating
IsSwitch = _Lines.IsSwitch
Idx = _Lines.Idx
_columns = _Lines._columns
__all__ = [
    "New",
    "AllNames",
    "Bus1",
    "Bus2",
    "C0",
    "C1",
    "CMatrix",
    "Count",
    "EmergAmps",
    "First",
    "Geometry",
    "Length",
    "LineCode",
    "Name",
    "Next",
    "NormAmps",
    "NumCust",
    "Parent",
    "Phases",
    "R0",
    "R1",
    "Rg",
    "Rho",
    "RMatrix",
    "Spacing",
    "TotalCust",
    "Units",
    "X0",
    "X1",
    "Xg",
    "XMatrix",
    "Yprim",
    "SeasonRating",
    "IsSwitch",
    "Idx",
]
