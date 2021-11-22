def multi_level_pie_chart(df, color_list, color_range):

    fig = px.sunburst(df, path=['level1', 'level2','level3'], values='values', color = 'level1',
                      color_discrete_sequence= color_list, #[ 'peachpuff', 'peru', 'pink', 'plum'.....
                      range_color= color_range#[1,20]
                     )
    fig.update_layout(title_text= "Multi level Pie")
    fig.show()
