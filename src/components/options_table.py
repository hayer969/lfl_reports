from dash import Dash, dash_table, html, Input, Output, State
from dash.exceptions import PreventUpdate
from . import ids
import base64


def render(app: Dash) -> html.Div:
    data = [
        {
            "filename": None,
            "sheet_name": "TDSheet",
            "data_columns": "'Выручка'|'Валовая прибыль расчетная'",
            "merge_by_column": "Код",
            "first_row": None,
            "last_row": None,
        }
    ]
    columns = [
        {"id": "filename", "name": "Имя файла", "presentation": "dropdown"},
        {"id": "sheet_name", "name": "Таблица"},
        {"id": "data_columns", "name": "Столбцы данных"},
        {"id": "merge_by_column", "name": "Общий признак"},
        {"id": "first_row", "name": "Первая строка"},
        {"id": "last_row", "name": "Последняя строка"},
    ]

    @app.callback(
        Output(ids.OPTIONS_TABLE, "dropdown"),
        Input(ids.UPLOAD_NOMENCLATURE, "contents"),
        State(ids.UPLOAD_NOMENCLATURE, "filename"),
    )
    def update_filenames_dropdown(_: base64, filename: str) -> list:
        if filename is None:
            raise PreventUpdate
        else:
            filenames = [filename]
            return {
                "filename": {
                    "options": [{"label": i, "value": i} for i in filenames],
                },
            }

    return html.Div(
        className="options_table_container",
        children=[
            dash_table.DataTable(
                id=ids.OPTIONS_TABLE,
                data=data,
                columns=columns,
                editable=True,
            ),
        ],
    )
