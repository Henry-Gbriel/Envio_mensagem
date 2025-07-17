import mysql.connector
import pywhatkit
import smtplib
from email.message import EmailMessage
from datetime import datetime, timedelta
import time

# Conexão com o banco
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',  
    database='Cobrancas'
)
cursor = conexao.cursor(dictionary=True)

# Buscar devedores
cursor.execute("""
               
    SELECT pc.id_cliente, pc.nome_empresa, pc.cnpj, pc.email, pc.telefone,
           tv.id_titulo, tv.valor_contrato, tv.valor_juros, tv.dias_atrasado
    FROM Perfil_Cliente pc
    JOIN Titulo_Vencido tv ON pc.cnpj = tv.cnpj
    WHERE tv.dias_atrasado > 10
""")
devedores = cursor.fetchall()

def formatar_numero(numero_bruto):
    numero_formatado = (
        numero_bruto.replace("(", "")
        .replace(")", "")
        .replace(" ", "")
        .replace("-", "")
    )
    if not numero_formatado.startswith("+"):
        numero_formatado = "+55" + numero_formatado
    if len(numero_formatado) not in [13, 14]:
        print(f"Número inválido: {numero_bruto} formatado: {numero_formatado}")
        return None
    return numero_formatado

def enviar_whatsapp(numero, mensagem):
    try:
        print(f"Enviando WhatsApp para {numero} imediatamente...")
        pywhatkit.sendwhatmsg_instantly(numero, mensagem, wait_time=20, tab_close=True)
        time.sleep(5)  # espera para garantir o envio e fechamento da aba
        print(f"WhatsApp enviado para {numero}")
        return True
    except Exception as e:
        print(f"Erro ao enviar WhatsApp para {numero}: {e}")
        return False

def enviar_email(nome, email, mensagem):
    msg = EmailMessage()
    msg['Subject'] = 'Aviso de Pendência Financeira'
    msg['From'] = 'henryautomationprojects@gmail.com'  # seu e-mail
    msg['To'] = email
    msg.set_content("Você possui um saldo pendente. Visualize o e-mail em HTML para mais detalhes.")
    msg.add_alternative(mensagem, subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('henryautomationprojects@gmail.com', 'ncyv ubzi rgaj omps')  # senha app
            smtp.send_message(msg)
            print(f"E-mail enviado para {nome} ({email})")
            return True
    except Exception as e:
        print(f"Erro ao enviar e-mail para {nome} ({email}): {e}")
        return False

# Loop principal para enviar mensagens e registrar
for d in devedores:
    total_divida = float(d['valor_contrato']) + float(d['valor_juros'])

    mensagem = (
        f"Prezado(a) {d['nome_empresa']},\n\n"
        "Espero que esteja bem!\n\n"
        f"Identificamos um atraso de {d['dias_atrasado']} dias no pagamento do contrato\n\n"
        f"no valor de R$ {d['valor_contrato']:.2f}, com juros acumulados de R$ {d['valor_juros']:.2f}.\n\n"
        f" Total atualizado: R$ {total_divida:.2f}\n\n"
        f"Por favor, regularize até {datetime.now().strftime('%d/%m/%Y')}.\n\n"
        f"Esta é uma mensagem automática."
    )

    numero_formatado = formatar_numero(d['telefone'])
    if not numero_formatado:
        continue  # pula este cliente se telefone inválido

    enviado_wpp = enviar_whatsapp(numero_formatado, mensagem)
    enviado_email = enviar_email(d['nome_empresa'], d['email'], mensagem)

    # Registrar no banco se enviou ao menos uma mensagem
    if enviado_wpp or enviado_email:
        cursor.execute("""
            INSERT INTO Cobranca (id_cliente, id_titulo, data_envio, historico_mensagem)
            VALUES (%s, %s, %s, %s)
        """, (
            d['id_cliente'],
            d['id_titulo'],
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            mensagem
        ))
        conexao.commit()
        print(f"Registro salvo no banco para {d['nome_empresa']}")

conexao.close()
print("Processo concluído!")
