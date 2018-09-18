# proj/app.py
import faust
import sys
sys.path.append('/opt/capture')

app = faust.App(
    'proj',
    version=1,
    autodiscover=True,
    origin='proj.capture'   # imported name for this project (import proj -> "proj")
)

def main() -> None:
    app.main()
