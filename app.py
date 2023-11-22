import pandas as pd 
import streamlit as st 
import plotly.express as px 
from data_processing import load_data, renombrar_cargos, mapear_asistencia, categorize_empresa
from plot_chart import plot_ast_return, plot_pie_chart_medio, plot_pie_chart_empresa


df = load_data(st.secrets['EXCEL_FILE_PATH'])
df['Cargo'] = df['Cargo'].apply(renombrar_cargos)
df['Asistencia'] = df['Asistencia'].apply(mapear_asistencia)
df['Empresa'] = df['Empresa'].astype(str).apply(categorize_empresa)

def main_app():
    st.set_page_config(page_title='SOLAR DASHBOARD', page_icon=':bar')
    st.title(':chart_with_upwards_trend: SOLAR VISITANTES 2019-2023')
    st.markdown('##')
    data = {
    'EVENTO' : ['SOLAR 2019', 'SOLAR 2020', 'SOLAR 2021', 'SOLAR 2022', 'SOLAR2023'],
    'REGISTROS' : [11254, 5212, 4996, 7139, 10653]
}
    data = pd.DataFrame(data)
    fig = px.bar(data, x='EVENTO', y='REGISTROS', color='EVENTO' )
    st.plotly_chart(fig, use_container_width=True)
    # Your existing DataFrame
    data_ast = {
    'EVENTO': ['SOLAR 2019', 'SOLAR 2020', 'SOLAR 2021', 'SOLAR 2022', 'SOLAR 2023'],
    'SI': [3824, 0, 2685, 3412, 4350],
    'NO': [7430, 0, 2311, 3727, 6303]
}
    data_ast = pd.DataFrame(data_ast)
# Transform the DataFrame to long format
    data_ast_long = data_ast.melt(id_vars='EVENTO', value_vars=['SI', 'NO'], var_name='Asistencia', value_name='Cantidad')
# Create the bar plot
    fig_ast = px.bar(data_ast_long, x='EVENTO', y='Cantidad', color='Asistencia', barmode='group')
    st.plotly_chart(fig_ast, use_container_width=True)

    fig_ast = plot_ast_return()
    st.plotly_chart(fig_ast, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        fig_pie_medio = plot_pie_chart_medio(df)
        st.plotly_chart(fig_pie_medio, use_container_width=True)
    with col2:
        fig_pie_categoria= plot_pie_chart_empresa(df)
        st.plotly_chart(fig_pie_categoria, use_container_width=True)

    # table = df.groupby(['Cargo', 'Asistencia', 'Evento']).size().reset_index(name='Cantidad')
    # table = table[table['Asistencia'].str.contains('SI')]
    # fig_cargo = px.bar(table, x='Evento', y='Cantidad', color='Cargo', barmode='group', 
    #              title='Asistentes por Categoria para cada ITM')
    # st.altair_chart(fig_cargo,use_container_width=True, theme='streamlit')
main_app()