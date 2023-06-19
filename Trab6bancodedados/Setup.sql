CREATE DATABASE trabalho6;

USE trabalho6;

CREATE TABLE marca (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(50)
);

CREATE TABLE modelo (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_marca INT,
  nome VARCHAR(50),
  FOREIGN KEY (id_marca) REFERENCES marca(id)
);

CREATE TABLE carro (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_modelo INT,
  nome VARCHAR(50),
  renavam INT,
  placa VARCHAR(7),
  valor DECIMAL(10,2),
  ano YEAR,
  FOREIGN KEY (id_modelo) REFERENCES modelo(id)
);