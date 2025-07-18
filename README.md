<h1>Automação de Cobranças</h1>
<p>Este projeto automatiza o processo de cobrança de dívidas, lendo dados de um arquivo Excel (.xlsx), registrando-os em um banco MySQL e enviando mensagens de cobrança via WhatsApp e E-mail.</p>

## O que ele faz?

- Lê os dados de clientes e títulos vencidos do Devedores.xlsx

- Insere/atualiza automaticamente as informações no banco de dados

- Calcula juros com base nos dias de atraso

- Envia mensagens de cobrança personalizadas

- Registra o histórico das cobranças no banco

## Tecnologias
-- Python

-- MySQL

## Bibliotecas:

- **pandas** → leitura do Excel

- **mysql-connector-python** → conexão com o banco

- **pywhatkit** → envio no WhatsApp

- **smtplib** e email → envio de e-mails

## Como usar
- Configurar o banco

- Crie o banco Cobrancas e as tabelas usando os scripts SQL.

## Instalar dependências
- bash
- Copiar
- Editar
- pip install pandas mysql-connector-python pywhatkit
- Colocar o arquivo Excel

O Devedores.xlsx deve ter as abas Perfil_Cliente e Titulo_Vencido.

Rodar os scripts

bash
Copiar
Editar
python inserir_dados.py   # Lê o Excel e registra no banco
python cobranca.py        # Envia mensagens e registra histórico
📄 Estrutura do banco
Perfil_Cliente → Dados dos clientes

Titulo_Vencido → Contratos em atraso

Cobranca → Histórico de mensagens enviadas

📸 Exemplos e Comprovações
✅ Diagramas do Banco de Dados
Conceitual:

Lógico:

✅ Registro de Dados no Banco
Dados de Clientes:

Títulos Vencidos:

Histórico de Cobrança:

✅ Comprovação do Envio
Log de Mensagens Enviadas:


Registro no Banco via Python:

<h2>📄 Licença</h2>
<p>Este projeto está licenciado sob a <a href="LICENSE">MIT License</a>.</p>
    
<h2>🤝 Contribuição</h2>

<p>Fique à vontade para abrir issues e enviar pull requests para melhorias no projeto!</p>
    
<h2>📞 Contato</h2>
<p>Caso tenha dúvidas ou sugestões, entre em contato:</p>
<ul>
    <li>📧 Email: <a href="mailto:santossilvahenrygabriel58@gmail.com">Meu email de contato</a></li>
    <li>🔗 LinkedIn: <a href="www.linkedin.com/in/henry-gabriel-santos-silva-6ba776209">Meu Perfil linkedin</a></li>
</ul>
    
<hr>
    
<p>⭐ Se gostou do projeto, deixe um star no repositório!</p>
