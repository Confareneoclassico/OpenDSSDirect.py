# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import codec, CheckForError, api_util, Base


class IPDElements(Base):
    __slots__ = []
    _api_prefix = "PDElements"
    _columns = [
        "Name",
        "AccumulatedL",
        "ParentPDElement",
        "FromTerminal",
        "IsShunt",
        "NumCustomers",
        "SectionID",
        "FaultRate",
        "RepairTime",
        "TotalMiles",
        "TotalCustomers",
        "PctPermanent",
        "Lambda",
    ]

    def AccumulatedL(self):
        """(read-only) accummulated failure rate for this branch on downline"""
        return self._lib.PDElements_Get_AccumulatedL()

    def Count(self):
        """(read-only) Number of PD elements (including disabled elements)"""
        return self._lib.PDElements_Get_Count()

    def FaultRate(self, *args):
        """Get/Set Number of failures per year. For LINE elements: Number of failures per unit length per year."""
        # Getter
        if len(args) == 0:
            return self._lib.PDElements_Get_FaultRate()

        # Setter
        Value, = args
        self._lib.PDElements_Set_FaultRate(Value)
        self.CheckForError()

    def First(self):
        """(read-only) Set the first enabled PD element to be the active element.  Returns 0 if none found."""
        return self._lib.PDElements_Get_First()

    def FromTerminal(self):
        """(read-only) Number of the terminal of active PD element that is on the "from" side. This is set after the meter zone is determined."""
        return self._lib.PDElements_Get_FromTerminal()

    def IsShunt(self):
        """(read-only) Boolean indicating of PD element should be treated as a shunt element rather than a series element. Applies to Capacitor and Reactor elements in particular."""
        return self._lib.PDElements_Get_IsShunt() != 0

    def Lambda(self):
        """(read-only) Failure rate for this branch. Faults per year including length of line."""
        return self._lib.PDElements_Get_Lambda()

    def Name(self, *args):
        """Get/Set name of active PD Element. Returns null string if active element is not PDElement type."""
        # Getter
        if len(args) == 0:
            return self._get_string(self._lib.PDElements_Get_Name())

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self._lib.PDElements_Set_Name(Value)
        self.CheckForError()

    def Next(self):
        """(read-only) Advance to the next PD element in the circuit. Enabled elements only. Returns 0 when no more elements."""
        return self._lib.PDElements_Get_Next()

    def NumCustomers(self):
        """(read-only) Number of customers, this branch"""
        return self._lib.PDElements_Get_Numcustomers()

    def ParentPDElement(self):
        """(read-only) Sets the parent PD element to be the active circuit element.  Returns 0 if no more elements upline."""
        return self._lib.PDElements_Get_ParentPDElement()

    def RepairTime(self, *args):
        """Average repair time for this element in hours"""
        # Getter
        if len(args) == 0:
            return self._lib.PDElements_Get_RepairTime()

        # Setter
        Value, = args
        self._lib.PDElements_Set_RepairTime(Value)
        self.CheckForError()

    def SectionID(self):
        """(read-only) Integer ID of the feeder section that this PDElement branch is part of"""
        return self._lib.PDElements_Get_SectionID()

    def TotalMiles(self):
        """(read-only) Total miles of line from this element to the end of the zone. For recloser siting algorithm."""
        return self._lib.PDElements_Get_TotalMiles()

    def TotalCustomers(self):
        """(read-only) Total number of customers from this branch to the end of the zone"""
        return self._lib.PDElements_Get_Totalcustomers()

    def PctPermanent(self, *args):
        """Get/Set percent of faults that are permanent (require repair). Otherwise, fault is assumed to be transient/temporary."""
        # Getter
        if len(args) == 0:
            return self._lib.PDElements_Get_pctPermanent()

        # Setter
        Value, = args
        self._lib.PDElements_Set_pctPermanent(Value)
        self.CheckForError()


_PDElements = IPDElements(api_util)

# For backwards compatibility, bind to the default instance
AccumulatedL = _PDElements.AccumulatedL
Count = _PDElements.Count
FaultRate = _PDElements.FaultRate
First = _PDElements.First
FromTerminal = _PDElements.FromTerminal
IsShunt = _PDElements.IsShunt
Lambda = _PDElements.Lambda
Name = _PDElements.Name
Next = _PDElements.Next
NumCustomers = _PDElements.NumCustomers
ParentPDElement = _PDElements.ParentPDElement
RepairTime = _PDElements.RepairTime
SectionID = _PDElements.SectionID
TotalMiles = _PDElements.TotalMiles
TotalCustomers = _PDElements.TotalCustomers
PctPermanent = _PDElements.PctPermanent
_columns = _PDElements._columns
__all__ = [
    "AccumulatedL",
    "Count",
    "FaultRate",
    "First",
    "FromTerminal",
    "IsShunt",
    "Lambda",
    "Name",
    "Next",
    "NumCustomers",
    "ParentPDElement",
    "RepairTime",
    "SectionID",
    "TotalMiles",
    "TotalCustomers",
    "PctPermanent",
]
