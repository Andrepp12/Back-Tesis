use tesis;

INSERT INTO gestion_tipomovimiento (nombre, estado, descripcion) VALUES
('venta', 1, 'Movimiento relacionado con la venta de productos'),
('pedido', 1, 'Movimiento relacionado con el pedido de productos'),
('devolucion de venta', 1, 'Movimiento de devolución de productos de una venta'),
('devolucion de pedido', 1, 'Devolución de productos de un pedido recibido'),
('ajustes por inventarios ingreso', 1, 'Ingreso ajustado en inventario por inventario'),
('otro egreso', 1, 'Movimiento de egreso no clasificado en otras categorías'),
('donaciones recibidas', 1, 'Ingreso de productos mediante donaciones'),
('donaciones realizadas', 1, 'Egreso de productos donados a terceros'),
('ajuste de inventario egreso', 1, 'Egreso ajustado en inventario por ajuste'),
('otro ingreso', 1, 'Ingreso no clasificado en otras categorías'),
('Merma o deterioro', 1, 'Pérdida de inventario por merma o deterioro');

-- Inserts para la tabla Marca (marcas de zapatillas conocidas)
INSERT INTO gestion_marca (codigo, nombre, estado) VALUES
('NIKE', 'Nike', 1),
('ADIDAS', 'Adidas', 1),
('PUMA', 'Puma', 1),
('REEBOK', 'Reebok', 1),
('NEW_BALANCE', 'New Balance', 1),
('CONVERSE', 'Converse', 1),
('VANS', 'Vans', 1),
('UNDER_ARMOUR', 'Under Armour', 1),
('ASICS', 'Asics', 1),
('FILA', 'Fila', 1);

-- Inserts para la tabla Stand (ubicación de los stands)
INSERT INTO gestion_stand (ubicacion, nombre, estado) VALUES
('Primer Piso - Sector A', 'Stand 01', 1),
('Primer Piso - Sector B', 'Stand 02', 1),
('Primer Piso - Sector C', 'Stand 03', 1),
('Primer Piso - Sector D', 'Stand 04', 1),
('Segundo Piso - Sector E', 'Stand 05', 1);