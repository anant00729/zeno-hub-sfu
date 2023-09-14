"""Types for Zeno reports."""
from enum import Enum

from zeno_backend.classes.base import CamelModel


class ReportElementType(Enum):
    """Enumeration of possible report types in Zeno.

    Attributes:
        CHART: Chart element for a report.
        TEXT: Text element for a report.
    """

    CHART = "CHART"
    TEXT = "TEXT"


class Report(CamelModel):
    """Representation of a report in Zeno.

    Attributes:
        id (int): ID of the report.
        name (str): name of the report.
        owner_name (str): name of the creater of the report
        linked_projects (list[str]): all projects that can be used with the report.
        editor (bool): whether the current user can edit the report.
        public (bool): whether the report is publically visible.
    """

    id: int
    name: str
    owner_name: str
    linked_projects: list[str]
    editor: bool
    public: bool = False


class ReportElement(CamelModel):
    """Representation of an element of a Zeno report.

    Attributes:
        type (ReportElementType): what type of element this represents.
        data (str | None): any data that the element holds.
        chart_id (int | None): id of the chart this element is linked to.
    """

    id: int | None = None
    type: ReportElementType
    position: int
    data: str | None = None
    chart_id: int | None = None


class ReportResponse(CamelModel):
    """Response for a report in Zeno.

    Attributes:
        report (Report): the report itself.
        report_elements (list[ReportElement]): all elements of the report.
    """

    report: Report
    report_elements: list[ReportElement]
