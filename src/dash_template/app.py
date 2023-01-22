from dash import Dash, dcc, html, Input, Output

from dash_bootstrap_components.themes import BOOTSTRAP
from loader import load_data
from layout import create_layout


app = Dash(__name__)


def main() -> None:

    data = load_data()
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Dash Demo"
    app.layout = create_layout(app, data)
    app.run()


if __name__ == "__main__":
    app.run_server(debug=True)