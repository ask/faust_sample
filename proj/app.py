# proj/app.py
import faust

app = faust.App(
    'proj',
    version=1,
    autodiscover=True,
    origin='proj'   # imported name for this project (import proj -> "proj")
)

def main() -> None:
    app.main()
