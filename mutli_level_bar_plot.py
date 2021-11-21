def multi_level_bar_plot(df):

    col = ['darkcyan','mistyrose']*len(df[['level1','level2']].drop_duplicates())
    fig = go.Figure()
    fig.update_layout(
        template="simple_white",
        barmode="stack"
    )
    fig.add_trace(
            go.Bar(x=[df.level1, df.level2], y=df['%'].round(2) , text=df['total'], marker_color= col,
                   textposition='inside', texttemplate='%{y}%',
                   marker=dict(color='rgba(58, 71, 80, 0.6)',line=dict(color='rgba(58, 71, 80, 1.0)', width=3)), 
                   name='Class' ))
    for i in range(len(df.total.unique())):
        fig.add_annotation(x=i, y=105,text=str(df.total.unique()[i]),showarrow=False, font=dict(size=30) )
    fig.layout.update(barmode='group')
    fig.update_layout(
        font=dict(size=18),
        font_family="Courier New",
        xaxis=dict(title=' Level1',gridcolor='white',tickmode='linear',gridwidth=1),
        yaxis=dict(title=' (%)', gridwidth=1 ))

    fig.show()
