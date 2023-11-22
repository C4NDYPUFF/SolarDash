import plotly.express as px
import pandas as pd

def plot_ast_return():
    data_to_plot = { 
    'Evento' : ['2019'],
    'Asistentes que se registraron para 2023' : [3818],
    'Asistentes que regresaron en 2023' : [157],
    'Asistentes que no regresaron' : [3661],
    }
    plot_df = pd.DataFrame(data_to_plot)
    # Reshape the DataFrame
    melted_df = plot_df.melt(id_vars='Evento', var_name='Categoria', value_name='Cantidad')
    # Create a bar plot
    fig = px.bar(melted_df, x='Evento', y='Cantidad', color='Categoria', barmode='group')
    # Customize the plot
    fig.update_layout(
        title='Asistencia y Visitantes por Evento',
        xaxis_title='Evento',
        yaxis_title='Cantidad',
        legend_title='Categoria'
    )
    return fig

def plot_pie_chart_medio(df):
    value_counts = df['ComoSeEntero'].value_counts().reset_index()
    value_counts.columns = ['Medio', 'Cantidad']
    fig_pie = px.pie(value_counts, names='Medio', values='Cantidad', title='Distribución de Medios 2023')
    return fig_pie

def plot_pie_chart_empresa(df):
    value_counts = df['Empresa'].value_counts().reset_index()
    value_counts.columns = ['Categoria', 'Cantidad']
    fig_pie = px.pie(value_counts, names='Categoria', values='Cantidad', title='Distribución de Categoria 2019-2023')
    return fig_pie