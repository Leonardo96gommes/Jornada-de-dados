-- Criação da tabela
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cidade TEXT NOT NULL,
    idade INTEGER
);

-- Inserindo dados
INSERT INTO clientes (nome, cidade, idade) VALUES 
('Ana Souza', 'São Paulo', 25),
('João Mendes', 'Rio de Janeiro', 30),
('Carla Lima', 'Belo Horizonte', 22),
('Pedro Silva', 'São Paulo', 35),
('Lucas Araújo', 'Curitiba', 28);
SELECT 
-- sql server, postegres, oracle, mysql
SELECT coluna1,coluna2
FROM tabela

SELECT * 
FROM tabela

SELECT FirstName, LastName