from dash import Dash, html

from . import nomenclature, options_table


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="upload",
                children=[
                    nomenclature.render(app),
                    options_table.render(app),
                ],
            ),
        ],
    )
