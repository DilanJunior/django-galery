/* Practicar la creaci�n de una base de datos con un dise�o que permita 
organizar los productos de una tienda, asoci�ndolos con la ubicaci�n geogr�fica de las sucursales en diferentes cantones. 
Esto facilitar� que los usuarios puedan acceder a los productos disponibles en la tienda m�s cercana a su ubicaci�n. */ 

CREATE DATABASE ecome_jp_db;
USE ecome_jp_db;


CREATE TABLE Producto
(
producto_id INT PRIMARY KEY IDENTITY,
nombre NVARCHAR(300) NOT NULL,
descripcion NVARCHAR(500) NOT NULL,
precio DECIMAL(10, 2) NOT NULL,
descuento DECIMAL(5, 2) NULL 
);


CREATE TABLE Producto_Variante(

variante_id INT PRIMARY KEY IDENTITY,
producto_id INT,
cantidad INT NOT NULL,
tallas VARCHAR(255), -- Ejemplo: 'S,M,L,XL'
imagen_url NVARCHAR(200) NULL,
CONSTRAINT Fk_producto_id FOREIGN KEY (producto_id) REFERENCES Producto(producto_id)


);

CREATE TABLE Sucursales
(
sucursal_id INT PRIMARY KEY IDENTITY,  
nombre_canton NVARCHAR(300) NOT NULL,  
direccion VARCHAR(255) NOT NULL,  
contacto VARCHAR(25) NOT NULL 
);

CREATE TABLE Producto_Sucursal
(
id INT PRIMARY KEY IDENTITY,
sucursal_id INT,
variante_id INT,
CONSTRAINT fk_sucursal_id FOREIGN KEY (sucursal_id) REFERENCES Sucursales(sucursal_id) ON DELETE CASCADE,
CONSTRAINT fk_id_variante FOREIGN KEY (variante_id) REFERENCES Producto_Variante(variante_id) ON DELETE CASCADE


);


INSERT INTO Producto (nombre, descripcion, precio, descuento)
VALUES 
('Camiseta B�sica', 'Camiseta de algod�n 100%', 19.99, 2.00),
('Pantal�n Jeans', 'Pantal�n de mezclilla cl�sico', 49.99, 5.00),
('Zapatos Deportivos', 'Zapatos c�modos para correr', 79.99, NULL);


INSERT INTO Producto_Variante (producto_id, cantidad, tallas, imagen_url)
VALUES 
(1, 50, 'S,M,L', 'https://ejemplo.com/camiseta.jpg'),
(1, 30, 'XL,XXL', 'https://ejemplo.com/camiseta-xl.jpg'),
(2, 20, '28,30,32', 'https://ejemplo.com/jeans.jpg'),
(3, 15, '38,39,40', 'https://ejemplo.com/zapatos.jpg');

INSERT INTO Sucursales (nombre_canton, direccion, contacto)
VALUES 
('San Jos�', 'Calle 123, Avenida Central', '+506 2222 3333'),
('Heredia', 'Calle 456, Barrio Flores', '+506 2444 5555'),
('Alajuela', 'Calle 789, Plaza Real', '+506 2666 7777');

INSERT INTO Producto_Sucursal (sucursal_id, variante_id)
VALUES 
(1, 1),  -- Sucursal San Jos� tiene la variante 1 (Camiseta B�sica, tallas S,M,L)
(1, 3),  -- Sucursal San Jos� tiene la variante 3 (Pantal�n Jeans, tallas 28,30,32)
(2, 2),  -- Sucursal Heredia tiene la variante 2 (Camiseta B�sica, tallas XL,XXL)
(3, 4);  -- Sucursal Alajuela tiene la variante 4 (Zapatos Deportivos, tallas 38,39,40)





SELECT 
    p.nombre AS Producto,
    pv.tallas AS Tallas,
    pv.cantidad AS Cantidad,
	pv.imagen_url AS ImagenUrl,
    s.nombre_canton AS Sucursal,
    s.direccion AS Direccion_Sucursal,
    s.contacto AS Contacto_Sucursal
FROM 
    Producto_Variante pv
INNER JOIN 
    Producto_Sucursal ps ON pv.variante_id = ps.variante_id
INNER JOIN 
    Sucursales s ON ps.sucursal_id = s.sucursal_id
INNER JOIN 
    Producto p ON pv.producto_id = p.producto_id;