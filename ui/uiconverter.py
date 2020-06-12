
import glob
import sys
import subprocess


def convert_qtdesigner_files(ui_files=[]):
    if ui_files == []:
        ui_files = glob.glob("*.ui")

    for ui_file in ui_files:
        try:
            ui_py = "ui_%s.py" % ui_file.split(".")[0]
            print("converting: %s to %s" % (ui_file, ui_py))
            subprocess.call([".\\..\\venv\\Scripts\\pyside2-uic.exe", ui_file, "-o", ui_py])
        except Exception as e:
            print(e)

    qrc_files = glob.glob("*.qrc")
    for qrc_file in qrc_files:
        rc_py = "%s_rc.py" % qrc_file.split(".")[0]
        print("converting: %s" % qrc_file)
        subprocess.call([".\\..\\venv\\Scripts\\pyside2-rcc.exe", qrc_file, "-o", rc_py])

if __name__ == "__main__":
    # inputFiles =
    convert_qtdesigner_files(sys.argv[1:])

