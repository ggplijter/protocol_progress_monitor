from PySide2 import QtCore, QtGui
from PySide2.QtCharts import QtCharts
from math import ceil

__all__ = ["QProtocolProgressChartView"]

PREPARE_TIME        = 15
MEASURE_TIME        = 5
REST_TIME           = 60

TIMEZONE0           = 0
TIMEZONE1           = TIMEZONE0 + PREPARE_TIME
TIMEZONE2           = TIMEZONE1 + MEASURE_TIME
TIMEZONE3           = TIMEZONE2 + REST_TIME
TIMEZONE4           = TIMEZONE3 + MEASURE_TIME
TIMEZONE5           = TIMEZONE4 + REST_TIME
TIMEZONE6           = TIMEZONE5 + MEASURE_TIME


FMT_1               = "Preparing for %i seconds"
FMT_2               = "Measuring for %i seconds"
FMT_3               = "Resting for %i seconds"

COLOR_PREPARE       = "#3c84a7"
COLOR_MEASURE       = "#7ac89c"
COLOR_REST          = "#eb8817"


class QProtocolProgressChartView(QtCharts.QChartView):
    updateInfo = QtCore.Signal(str)
    def __init__(self, parent = None):
        super(QProtocolProgressChartView, self).__init__(parent)

        self.drawBar()

    def startProtocol(self):
        self.sTime = QtCore.QDateTime.currentDateTime()
        self.timerID = self.startTimer(40, QtCore.Qt.PreciseTimer)

    def stopProtocol(self):
        self.killTimer(self.timerID)
        self.drawBar()

    def drawBar(self):
        axisX = QtCharts.QValueAxis()
        axisX.setRange(TIMEZONE0, TIMEZONE6)
        axisX.setTickCount(31)
        axisX.setLabelFormat("%i")
        axisX.setTitleText("→ Time (sec)")

        font = QtGui.QFont()
        font.setPointSize(12)
        # font.setFamily("Gothic")

        self.fases = dict((f"{x}", QtCharts.QBarSet(f"{x}") << 0) for x in range(6))

        series = QtCharts.QHorizontalStackedBarSeries()
        for x, v in self.fases.items():
            series.append(v)

        self.chart = QtCharts.QChart()
        self.chart.setTheme(QtCharts.QChart.ChartThemeHighContrast)
        self.chart.addSeries(series)
        self.chart.setAnimationOptions(QtCharts.QChart.NoAnimation)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(QtCore.Qt.AlignBottom)
        self.chart.legend().setFont(font)
        self.chart.setAxisX(axisX)

        series.attachAxis(axisX)

        self.fases["0"].setLabel("Preparation")
        self.fases["0"].setColor(COLOR_PREPARE)
        self.fases["1"].setLabel("Measurement 1")
        self.fases["1"].setColor(COLOR_MEASURE)
        self.fases["2"].setLabel("Rest Period 1")
        self.fases["2"].setColor(COLOR_REST)
        self.fases["3"].setLabel("Measurement 2")
        self.fases["3"].setColor(COLOR_MEASURE)
        self.fases["4"].setLabel("Rest Period 2")
        self.fases["4"].setColor(COLOR_REST)
        self.fases["5"].setLabel("Measurement 3")
        self.fases["5"].setColor(COLOR_MEASURE)

        self.setChart(self.chart)

    def timerEvent(self, ev):

        time_elapsed = self.sTime.msecsTo(QtCore.QDateTime.currentDateTime())
        time_elapsed_sec = time_elapsed/1000

        if time_elapsed_sec <= TIMEZONE1:
            self.updateInfo.emit(FMT_1 % ceil(TIMEZONE1 - time_elapsed_sec))
            self.fases['0'].replace(0, time_elapsed_sec)
        elif time_elapsed_sec <= TIMEZONE2:
            self.updateInfo.emit(FMT_2 % ceil(TIMEZONE2 - time_elapsed_sec))
            self.fases['1'].replace(0, time_elapsed_sec - TIMEZONE1)
        elif time_elapsed_sec <= TIMEZONE3:
            self.updateInfo.emit(FMT_3 % ceil(TIMEZONE3 - time_elapsed_sec))
            self.fases['2'].replace(0, time_elapsed_sec - TIMEZONE2)
        elif time_elapsed_sec <= TIMEZONE4:
            self.updateInfo.emit(FMT_2 % ceil(TIMEZONE4 - time_elapsed_sec))
            self.fases['3'].replace(0, time_elapsed_sec - TIMEZONE3)
        elif time_elapsed_sec <= TIMEZONE5:
            self.updateInfo.emit(FMT_3 % ceil(TIMEZONE5 - time_elapsed_sec))
            self.fases['4'].replace(0, time_elapsed_sec - TIMEZONE4)
        elif time_elapsed_sec <= TIMEZONE6:
            self.updateInfo.emit(FMT_2 % ceil(TIMEZONE6 - time_elapsed_sec))
            self.fases['5'].replace(0, time_elapsed_sec - TIMEZONE5)
        else:
            self.updateInfo.emit("Well done! Protocol finished.")
            self.fases['5'].replace(0, TIMEZONE6)





