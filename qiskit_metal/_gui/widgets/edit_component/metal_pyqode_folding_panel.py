from pyqode.core.panels.folding import FoldingPanel
from pyqode.core.api.folding import FoldScope
from pyqode.core.api import TextBlockHelper, folding, TextDecoration, \
    DelayJobRunner
from pyqode.qt import QtCore, QtWidgets, QtGui, PYQT5_API
from qiskit_metal.toolbox_metal.exceptions import IncorrectQtException
import os


class MetalPyqodeFoldingPanel(FoldingPanel):
    """Hacky, temporary solutions to PyQode.core.panels.FoldingPanel
    not calling the correct function when PySide2 is being used.
    The _draw_fold_indicator threw:
    AttributeError: module 'pyqode.qt.QtGui' has no attribute 'QStyleOptionViewItemV2'
    when opt = QtGui.QStyleOptionViewItemV2() was called.

    Args:
        panels ([type]): [description]
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _draw_fold_indicator(self, top, mouse_over, collapsed, painter):
        """
        Draw the fold indicator/trigger (arrow).

        :param top: Top position
        :param mouse_over: Whether the mouse is over the indicator
        :param collapsed: Whether the trigger is collapsed or not.
        :param painter: QPainter
        """
        rect = QtCore.QRect(0, top,
                            self.sizeHint().width(),
                            self.sizeHint().height())
        self._native = False