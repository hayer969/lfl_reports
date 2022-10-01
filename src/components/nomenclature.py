from dash import Dash, dcc, html, Input, Output, State

from . import ids


def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.UPLOAD_NOMENCLATURE_PATH, "children"),
        Input(ids.UPLOAD_NOMENCLATURE_BUTTON, "contents"),
        State(ids.UPLOAD_NOMENCLATURE_BUTTON, "filename")
    )
    def update_output(_, filename: str) -> str:
        return f"Filename: {filename}"

    return html.Div(
        children=[
            dcc.Upload(
                html.Button(
                    className="upload_nomenclature_button",
                    children=["Загрузить номенклатуру"],
                ),
                id=ids.UPLOAD_NOMENCLATURE_BUTTON,
            ),
            html.Div(id=ids.UPLOAD_NOMENCLATURE_PATH),
        ],
    )
