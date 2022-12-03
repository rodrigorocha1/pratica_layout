import dash
from dash import html, dcc


app = dash.Dash(__name__, title='Pratica Layout')

app.layout = html.Div(
    [
        html.Header(
            html.Div([
                html.Img(src='assets/logo.svg', alt="DsMeta"),
                html.H1('DsMeta'),
                html.P(
                    [
                        "Desenvolvido por ",
                        html.A("@rodrigosilvarocha14",
                               href="https://www.instagram.com/rodrigosilvarocha14/")
                    ]
                )

            ], className='dsmeta-logo-container')
        ),
        html.Main(
            html.Section(
                html.Div(
                    html.Div([
                        html.H2("Vendas", className='dsmeta-sales-title'),
                        html.Div(
                            [
                                html.Div([
                                    dcc.Input(type='text', className="ds-meta-form-control"),
                                ], className='ds-meta-form-control-container'),
                                html.Div([
                                    dcc.Input(type='text', className="ds-meta-form-control"),
                                ], className='ds-meta-form-control-container'),
                            ], className='ds-meta-form-control-container'
                        ),
                        html.Div([
                            html.Table(
                                [
                                    html.Thead(
                                        html.Tr(
                                            [
                                                html.Th("ID", className="show992"),
                                                html.Th("Data", className="show576"),
                                                html.Th("Vendedor"),
                                                html.Th("Visitas", className="show992"),
                                                html.Th("Vendas", className="show992"),
                                                html.Th("Total"),
                                                html.Th("Notificar")
                                            ]

                                        )
                                    ),
                                    html.Tbody([
                                        html.Tr([
                                            html.Td(i, className="show992"),
                                            html.Td("01/08/22", className="show576"),
                                            html.Td("Anakin"),
                                            html.Td("15", className="show992"),
                                            html.Td("11", className="show992"),
                                            html.Td("R$ 5300"),
                                            html.Td(
                                                html.Div(
                                                    html.Div(
                                                        html.Img(src='assets/avatar-icon_1.svg', alt="notificar"),
                                                        className="ds-meta-red-btn"),
                                                    className="ds-meta-red-btn-container"
                                                )
                                            )
                                        ]) for i in range(1, 10)
                                    ])
                                ], className='dsmeta-sales-table'
                            )
                        ])
                    ], className="dsmeta-card"),
                    className='dsmeta-container'
                ), id='sales'
            )
        )
    ],
)

if __name__ == '__main__':
    app.run_server(debug=True, port=804)
