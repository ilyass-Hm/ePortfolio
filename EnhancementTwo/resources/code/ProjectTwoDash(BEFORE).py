# Setup the Jupyter version of Dash
from jupyter_dash import JupyterDash

# Configure the necessary Python module imports for dashboard components
import dash
import dash_leaflet as dl
from dash import dcc
from dash import html
import plotly.express as px
from dash import dash_table as dt
from dash.dependencies import Input, Output, State
import base64

# Configure OS routines
import os

# Configure the plotting routines
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from animalShelter import AnimalShelter

###########################
# Data Manipulation / Model
###########################

username = "accuser"
password = "SNHU1234"

# Connect to database via CRUD Module
db = AnimalShelter(username, password)

# class read method must support return of list object and accept projection json input
# sending the read method an empty document requests all documents be returned
df = pd.DataFrame.from_records(db.readAll({}))

# MongoDB v5+ is going to return the '_id' column and that is going to have an 
# invlaid object type of 'ObjectID' - which will cause the data_table to crash - so we remove
# it in the dataframe here. The df.drop command allows us to drop the column. If we do not set
# inplace=True - it will reeturn a new dataframe that does not contain the dropped column(s)
#df.drop(columns=['_id'],inplace=True)

## Debug
#print(len(df.to_dict(orient='records')))
#print(df.columns)


# In[2]:


#########################
# Dashboard Layout / View
#########################
app = JupyterDash(__name__)

#Add in Grazioso Salvare’s logo
image_filename = 'Grazioso Salvare Logo.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())


# In[3]:


app.layout = html.Div([
        html.Center(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))),
    html.Center(html.B(html.H1('[Ilyass Hmamou] - CS-340 Dashboard'))),
    html.Hr(),
    html.Div(
        #Radio Items to select the rescue filter options
        dcc.RadioItems(
            id='filter-type',
            # created the labels and keys based on the Grazioso requirements
            options=[
            {'label': 'Water Rescue', 'value': 'WR'},
            {'label': 'Mountain/Wilderness Rescue', 'value': 'MWR'},
            {'label': 'Disaster Rescue/Individual Tracking', 'value': 'DRIT'},
            {'label': 'Show All', 'value': 'All'}
            ],
            value='All',
            labelStyle={'display': 'inline-block'}
        )
    ),
    html.Hr(),
    dt.DataTable(
        id='datatable-id',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns
        ],
        data=df.to_dict('records'),
        #Set up the features for your interactive data table to make it user-friendly for your client
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable=False,
        row_selectable="single",
        row_deletable=False,
        selected_columns=[],
        selected_rows=[0],
        page_action="native",
        page_current=0,
        page_size=10,
    ),
    html.Br(),
    html.Hr(),
    #This sets up the dashboard so that your chart and your geolocation chart are side-by-side
    html.Div(className='row',
         style={'display' : 'flex'},
             children=[
        html.Div(
            #dcc.Graph(id='graph-id'),
            id='graph-id',
            className='col s12 m6',

            ),
        html.Div(
            id='map-id',
            className='col s12 m6',
            )
        ])
])


# In[4]:


#############################################
# Interaction Between Components / Controller
#############################################
    
@app.callback([Output('datatable-id','data'),
               Output('datatable-id','columns')],
              [Input('filter-type', 'value')])
def update_dashboard(filter_type):
        #filter interactive data table with MongoDB queries
        if filter_type == 'WR':
            df = pd.DataFrame(list(db.readAll({
                "breed" : {"$in": ["Labrador Retriever Mix", "Chesapeake Bay Retriever", "Newfoundland"]}, 
                "sex_upon_outcome" : "Intact Female", 
                "age_upon_outcome_in_weeks": {"$lte": 156, "$gte": 26}})))
        elif filter_type == 'MWR':
            df = pd.DataFrame(list(db.readAll({
                "breed" : {"$in": ["German Shephard", "Alaskan Malamute", "Old English Sheepdog", 
                                   "Siberian Husky", "Rottweiler"]}, 
                "sex_upon_outcome" : "Intact Male", 
                "age_upon_outcome_in_weeks": {"$lte": 156, "$gte": 26}})))
        elif filter_type == 'DRIT':
            df = pd.DataFrame(list(db.readAll({
                "breed" : {"$in": ["Doberman Pinscher", "German Shephard", "Golden Retriever", 
                                   "Bloodhound", "Rottweiler"]}, 
                "sex_upon_outcome" : "Intact Male", 
                "age_upon_outcome_in_weeks": {"$lte": 300, "$gte": 20}})))
        elif filter_type == 'All':
            df = pd.DataFrame.from_records(db.readAll({}))

        
        columns=[{"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns]
        data=df.to_dict('records')
        
        return (data,columns)


# In[5]:


#This callback will highlight a cell on the data table when the user selects it
@app.callback(
    Output('datatable-id', 'style_data_conditional'),
    [Input('datatable-id', 'selected_columns')]
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]


# In[6]:


#function to update the pie chart
@app.callback(
    Output('graph-id', "children"),
    [Input('datatable-id', "derived_viewport_data")])
def update_graphs(viewData):
    # imports the currently displayed data
    dff = pd.DataFrame.from_dict(viewData)
    #creates the values needed for the names (breed) and values (recurring counts)
    names = dff['breed'].value_counts().keys().tolist()
    values = dff['breed'].value_counts().tolist()
    #creates a pie chart based on the data above
    return [
        dcc.Graph(            
            figure = px.pie(
                data_frame=dff, 
                values = values, 
                names = names, 
                color_discrete_sequence=px.colors.sequential.RdBu,
                width=800, 
                height=500   
            )
        )
    ]


# In[7]:


@app.callback(
    Output('map-id', "children"),
    [Input('datatable-id', "derived_virtual_data"),
     Input('datatable-id', "derived_virtual_selected_rows")])
def update_map(viewData, index):
    
    #Add geolocation chart
    dff = pd.DataFrame.from_dict(viewData)
    # Because we only allow single row selection, the list can 
    # be converted to a row index here
    if index is None:
       row = 0
    else: 
       row = index[0]
    # Austin TX is at [30.75,-97.48]
    return [
        dl.Map(style={'width': '1000px', 'height': '500px'},
           center=[30.75,-97.48], zoom=10, children=[
           dl.TileLayer(id="base-layer-id"),
           # Marker with tool tip and popup
           # Column 13 and 14 define the grid-coordinates for 
           # the map
           # Column 4 defines the breed for the animal
           # Column 9 defines the name of the animal
           dl.Marker(position=[dff.iloc[row,13],dff.iloc[row,14]],children=[
                dl.Tooltip(dff.iloc[row,4]),
                dl.Popup([
                    html.H1("Animal Name"),
                    html.P(dff.iloc[row,9])
                ])
            ])
        ])
    ]
app.run_server(debug=True)
