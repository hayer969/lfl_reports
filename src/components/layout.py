from dash import Dash, html

from . import nomenclature


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="upload_nomenclature_container",
                children=[
                    nomenclature.render(app),
                ],
            ),
        ],
    )
