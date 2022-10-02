from dash import Dash, dcc, html, Input, Output, State
import base64

from . import ids


def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.OPTIONS_TABLE, "data"),
        Input(ids.UPLOAD_NOMENCLATURE, "contents"),
        State(ids.UPLOAD_NOMENCLATURE, "filename"),
    )
    def update_nomenclature(_: base64, filename: str) -> list:
        options_data = [
            {
                "filename": filename,
                "sheet_name": "TDSheet",
                "data_columns": "('Наименование')",
                "merge_by_column": "Код",
                "first_row": None,
                "last_row": None,
            }
        ]
        return options_data

    return html.Div(
        className="upload_nomenclature_button_container",
        children=[
            dcc.Upload(
                id=ids.UPLOAD_NOMENCLATURE,
                children=[
                    html.Button(
                        className="upload_nomenclature_button",
                        children=["Загрузить номенклатуру"],
                    ),
                ],
            ),
        ],
    )
