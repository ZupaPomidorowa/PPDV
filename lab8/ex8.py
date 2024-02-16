from dash import Dash, callback, html, Input, Output, dcc, State
import dash
import pandas as pd
import requests

df = pd.read_csv('Salaries.csv')

#data = requests.get('https://isod.ee.pw.edu.pl/isod-portal/wapi?q=dissertations_offers&orgunit=ISEP&fromrow=10&maxrows=4&active=true&format=json&lang=en&datefrom=23.02.2010')
#df = pd.DataFrame(data.json()['list'])

def create_table(mdf):
    return html.Table (
        [
            html.Tr(
                [html.Td(col, style ={'border': '1px solid gray'}) for col in mdf.loc[idx]]
            ) for idx in mdf.index
        ]
    )

app = Dash(__name__)

app.layout = html.Div(children=[
    dcc.Store('memory'),
    html.H1(children='Paging table'),
    html.Div([
        html.Button('Top Left <<', id='cmd-top-left', disabled=True),
        html.Button('Left <', id='cmd-left', disabled=True),
        dcc.Input(id='nrows', value='10', size='3'),
        html.Button('Right >', id='cmd-right'),
        html.Button('Top Right >>', id='cmd-top-right'),
    ]),
    html.Div(id='output')
])

@callback(Output('output', 'children'),
          Output('memory', 'data'),
          Output('cmd-top-left', 'disabled'),
          Output('cmd-left', 'disabled'),
          Output('cmd-top-right', 'disabled'),
          Output('cmd-right', 'disabled'),
          Input('nrows', 'value'),
          Input('cmd-top-left', 'n_clicks'),
          Input('cmd-left', 'n_clicks'),
          Input('cmd-right', 'n_clicks'),
          Input('cmd-top-right', 'n_clicks'),
          State('memory', 'data'))
        
def update_table(nrows, clicks_tl, clicks_l, clicks_n, clicks_tr, data):
    data = data or {
        'start': 0
    }
    try:
        nrows = int(nrows)
    except:
        nrows = 0
    
    if dash.ctx.triggered_id == 'cmd-top-right':
        data['start'] = (len(df) // nrows) * (nrows)
    if dash.ctx.triggered_id == 'cmd-right':
        data['start'] = data['start'] + nrows
    if dash.ctx.triggered_id == 'cmd-left':
        data['start'] = data['start'] - nrows
    if dash.ctx.triggered_id == 'cmd-top-left':
        data['start'] = 0

    tlDisabled = data['start'] <= 0
    lDisabled = data['start'] <= 0

    trDisabled = data['start'] + nrows > len(df)
    rDisabled = data['start'] + nrows > len(df)

    return create_table(df.iloc[data['start']: data['start'] + nrows, :]), data, tlDisabled, lDisabled, rDisabled, trDisabled 

if __name__ == '__main__':
    app.run_server(debug=True)

