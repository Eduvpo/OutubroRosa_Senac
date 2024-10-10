import streamlit as st
# import mysql.connector
# import openpyxl 

# conexao = mysql.connector.connect(
#     host='127.0.0.1',
#     user='root',
#     password='',
#     database='evento'
# )

# cursor = conexao.cursor()

def main():
    st.set_page_config(page_title='Outubro Rosa', page_icon='icone.jpg')
    st.title("Avalie Nosso Evento!")
    st.image('outubro_rosa.jpg', width=700)      
    opcoes = ['Péssimo', 'Ruim', 'Bom', 'Excelente']
    sexos = ['M', 'F']

    nome = st.text_input('NOME:')
    telefone = st.text_input('TELEFONE:', max_chars=14)
    email = st.text_input('EMAIL:')
    sexo = st.selectbox('SEXO:', sexos)
    data_nascimento = st.date_input('DATA DE NASCIMENTO:')

    exame = st.radio('Você realiza o auto-exame?', ('Sim', 'Não'))

    st.title('Como você avalia nosso evento?')

    col1,col2,col3,col4 = st.columns(4)

    with col1: aval_pes = st.checkbox(opcoes[0])
    with col2: aval_ru = st.checkbox(opcoes[1])
    with col3: aval_bo = st.checkbox(opcoes[2])
    with col4: aval_ex = st.checkbox(opcoes[3])

    avaliacao = st.text_area(label= 'Sua Opinião', placeholder= 'Conte-nos o que você achou')

    if aval_pes:
        nota = 2
    elif aval_ru:
        nota = 3
    elif aval_bo:
        nota = 4
    elif aval_ex:
        nota = 5
   
    if st.button('ENVIAR'):
   

       if nome and email and sexo and data_nascimento and telefone !='':
            
            comando = f'INSERT INTO cadastro (nome, telefone, email, sexo, data_nascimento, auto_exame, nota, avaliacao) VALUES ("{nome}", "{telefone}", "{email}", "{sexo}", "{data_nascimento}", "{exame}", "{nota}", "{avaliacao}")'
            cursor.execute(comando)
            conexao.commit()
            st.success('Obrigado pela Presença! Ame-se Realize o Auto Exame')
       else:
            st.error("Por favor, insira dados válidos")

    if nome == 'Final':
        comando2 = f'Select * from cadastro'
        cursor.execute(comando2)
        resultado = cursor.fetchall()
        
        workbook = openpyxl.Workbook()
        sheet = workbook.active


        for col_num, column_name in enumerate(cursor.column_names, start=1):
            sheet.cell(row=1, column= col_num, value= column_name)

        row_num = 2
        for registro in resultado:
            for col_num, cell_value in enumerate(registro, start=1):
                sheet.cell(row= row_num, column= col_num, value= cell_value)
            row_num +=1

        workbook.save('dados.xlsx')
         
if __name__ == '__main__':
    main()
