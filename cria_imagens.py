import altair as alt

def criar_grafico_horizontal(data, x, y, titulo, altura_personalizada=False, altura=None):
    # Criar o gráfico
    base = alt.Chart(data).encode(
        x=alt.X(x),
        y=alt.Y(y).sort('-x').title(""),
        text=x
    )

    # Adicionar o título centralizado usando properties
    base = base.properties(
        title={
            "text": titulo,
            "anchor": 'middle'  # Centralizar o título
        }
    )

    fig = (base.mark_bar(cornerRadiusTopRight=10, cornerRadiusBottomRight=10, color="#153B8A") + base.mark_text(align='left', dx=2))
    
    if altura_personalizada:
        # Atribuir a propriedade height diretamente ao objeto de gráfico
        fig = fig.properties(height=altura)

    # Configurar o fundo transparente
    fig = fig.configure(background="transparent").configure_axis(labelLimit=180)
  

    return fig

range_ = ['#FFDD00','#289048', '#009DE1', '#153B8A', '#FF4500','#289048', '#009688', '#FF1493', '#4B0082', '#00CED1', '#FF8C00']

def cria_grafico_pizza(dados, valor, legenda, titulo, rad, orient):
    base = alt.Chart(dados).mark_arc(innerRadius=rad).encode(
        theta=valor,
        color=alt.Color(legenda).scale(range=range_) 
    )

    base = base.properties(
         title={
            "text": titulo,
            "anchor": orient  # Centralizar o título
        }
    )
    base = base.properties(height=400)
    base = base.configure(background="transparent")  # Corrected the property name
    return base

def criar_grafico_linhas(data, x, y, titulo, tamanho):
    # Criar o gráfico
    grafico = alt.Chart(data).mark_line(point=True).encode(
        x=x,
        y=y
    )

    # Adicionar o título centralizado usando properties
    grafico = grafico.properties(
        title={
            "text": titulo,
            "anchor": 'middle'  # Centralizar o título
        }
    )
    grafico=grafico.properties(height=tamanho)
    grafico=grafico.configure(background="transparent")
    return grafico

def criar_grafico_vertical(data, x, y, titulo, altura_personalizada=False, altura=None):
    # Criar o gráfico
    base = alt.Chart(data).encode(
        x=x,
        y=alt.Y(y).sort('-x'),
        text=y
    )

    # Adicionar o título centralizado usando properties
    base = base.properties(
        title={
            "text": titulo,
            "anchor": 'middle'  # Centralizar o título
        }
    )

    fig = (base.mark_bar(cornerRadiusTopRight=10, cornerRadiusTopLeft=10, color="#153B8A") + base.mark_text(align='center', dy=-10))
    
    if altura_personalizada:
        # Atribuir a propriedade height diretamente ao objeto de gráfico
        fig = fig.properties(height=altura)

    # Configurar o fundo transparente
    fig = fig.configure(background="transparent").configure_axis(labelLimit=1000)
  

    return fig
range_2 = ['#00CED1','#FFDD00','#289048', '#009DE1', '#153B8A', '#FF4500','#289048', '#009688', '#FF1493', '#4B0082', '#00CED1', '#FF8C00']
def criar_grafico_horizontal_segmento(data, x, y, titulo, segmento, titulosegmento):
    # Criar o gráfico
    base = alt.Chart(data).encode(
        x=alt.X(x),
        y=alt.Y(y).sort('-x'),
        text=x,
        color=alt.Color(segmento, title=titulosegmento).scale(range=range_2) 
    )

    # Adicionar o título centralizado usando properties
    base = base.properties(
        title={
            "text": titulo,
            "anchor": 'middle'  # Centralizar o título
        }
    )

    fig=base.mark_bar(cornerRadiusTopRight=10, cornerRadiusBottomRight=10) + base.mark_text(align='center', dx=2, color='black')
    fig = fig.configure(background="transparent").configure_axis(labelLimit=180)

    return fig