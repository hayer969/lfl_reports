from dash import Dash, html

from src.components.layout import create_layout


def main() -> None:
    app = Dash()
    app.title = "Create LFL"
    app.layout = create_layout(app)
    app.run(debug=True)


if __name__ == "__main__":
    main()
