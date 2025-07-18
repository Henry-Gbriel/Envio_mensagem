<h1>Automação de Cobranças</h1>
<p>Este projeto automatiza o processo de cobrança de dívidas, lendo dados de um arquivo Excel (.xlsx), registrando-os em um banco MySQL e enviando mensagens de cobrança via WhatsApp e E-mail.</p>

## O que ele faz?

- Lê os dados de clientes e títulos vencidos do Devedores.xlsx

- Insere/atualiza automaticamente as informações no banco de dados

- Calcula juros com base nos dias de atraso

- Envia mensagens de cobrança personalizadas

- Registra o histórico das cobranças no banco

## Tecnologias
- Python

- MySQL

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

## 📄 Estrutura do banco
- Perfil_Cliente → Dados dos clientes

- Titulo_Vencido → Contratos em atraso

- Cobranca → Histórico de mensagens enviadas

## Exemplos e Comprovações

✅ Diagramas do Banco de Dados
Conceitual:
<img width="787" height="311" alt="conceitual" src="https://github.com/user-attachments/assets/b4b07d91-7d2f-454b-bbc8-226f11047c3e" />

✅Lógico:
<img width="1105" height="560" alt="logico" src="https://github.com/user-attachments/assets/92d08af2-6b37-4268-9254-b551ddd631ea" />


✅ Registro de Dados no Banco
Dados de Clientes:
<img width="892" height="255" alt="Perfil_Cliente-regis" src="https://github.com/user-attachments/assets/2dbf9ca9-e30d-46fb-86e8-d2bcab1830cd" />

Títulos Vencidos:<br>
<img width="682" height="188" alt="Titulo_Vencido-regis" src="https://github.com/user-attachments/assets/cf2b2185-009a-4995-bdd5-4e3855794fee" />

Histórico de Cobrança:<br>
<img width="712" height="302" alt="registroCobranca" src="https://github.com/user-attachments/assets/706c2580-4ddf-41b6-90ad-6ffb63ba7b61" />


✅ Comprovação do Envio
Log de Mensagens Enviadas:
<img width="1463" height="456" alt="dados_enviados" src="https://github.com/user-attachments/assets/b7845ee2-471f-4920-bfd4-e356e1bf1864" />


Registro no Banco via Python:
<img width="1473" height="87" alt="registroBD-PY" src="https://github.com/user-attachments/assets/f1451e12-7251-46fc-804d-1969fa5946d0" />

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
