create database Cobrancas;
USE Cobrancas;

-- Perfil do Cliente 
CREATE TABLE Perfil_Cliente (
	id_cliente INT PRIMARY KEY,
    nome_empresa VARCHAR(100),
	cnpj VARCHAR(20) UNIQUE,
	email VARCHAR(100),
    telefone VARCHAR(20)
);

-- Título Vencido
CREATE TABLE Titulo_Vencido (
    id_titulo INT PRIMARY KEY,
    cnpj VARCHAR(20),
    valor_contrato DECIMAL(10,2),
    data_pagamento DATE,
    dias_atrasado INT,
    valor_juros DECIMAL(10,2),
    FOREIGN KEY (cnpj) REFERENCES Perfil_Cliente(cnpj)
);

-- Tabela Cobrança
CREATE TABLE Cobranca (
    id_envio INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_titulo INT,
    data_envio DATE,
    historico_mensagem TEXT,
    FOREIGN KEY (id_cliente) REFERENCES Perfil_Cliente(id_cliente),
    FOREIGN KEY (id_titulo) REFERENCES Titulo_Vencido(id_titulo)
);
