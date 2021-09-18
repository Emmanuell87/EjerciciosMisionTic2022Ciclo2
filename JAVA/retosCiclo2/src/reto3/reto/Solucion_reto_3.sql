--Cuáles son los materiales de construcción de construcción importados con su respectivo precio por
--unidad, ordenados por precio de mayor a menor. No. Registros = 10.

SELECT Nombre_Material, Precio_Unidad 
FROM MaterialConstruccion mc 
WHERE Importado = 'Si'
ORDER BY Precio_Unidad DESC 


--Cuales son los proveedores que importan materiales para la construcción, mostrando además el material
--que importan. No. Registros = 50, Ordenar por Proveedor y Nombre_Material.

SELECT DISTINCT c.Proveedor, mc.Nombre_Material, mc.Importado 
FROM Compra c
NATURAL JOIN MaterialConstruccion mc
WHERE mc.Importado = 'Si'
GROUP BY c.Proveedor, mc.Nombre_Material 



--Cual es la cantidad de todas las unidades de material para construcción vendidas, que han sido importados
--por ‘Homecenter’, especificando nombre de material. Así mismo debe ser ordenado por nombre de material y
--proveedor. No. Registros = 10.

SELECT c.Proveedor, mc.Nombre_Material, mc.Importado, mc.Precio_Unidad, SUM(Cantidad) Cantidad
FROM Compra c 
NATURAL JOIN MaterialConstruccion mc 
WHERE c.Proveedor = 'Homecenter' 
AND mc.Importado = 'Si'
GROUP BY c.Proveedor, mc.Nombre_Material
ORDER BY c.proveedor, mc.Nombre_material



--Cuales son todas las empresas constructoras, que se encuentren en ciudades que su nombre empiece con la
--letra ’B’, mostrar tanto el nombre de la constructora como la ciudad donde se encuentran. No. Registros = 15.
--Ordenar por Ciudad y resolver utilizando Distinct.

SELECT DISTINCT Constructora, Ciudad 
FROM Proyecto p 
WHERE ciudad LIKE 'B%'
ORDER BY ciudad



--Teniendo en cuenta la consulta 3, muestre los productos para ‘Homecenter’ de los cuales se hayan vendido
--mas de 100 unidades. No. Registros = 7.

SELECT c.Proveedor, mc.Nombre_Material, mc.Importado, mc.Precio_Unidad, SUM(Cantidad) Cantidad
FROM Compra c 
NATURAL JOIN MaterialConstruccion mc 
WHERE c.Proveedor = 'Homecenter' 
AND mc.Importado = 'Si'
GROUP BY c.Proveedor, mc.Nombre_Material
HAVING SUM(c.Cantidad) > 100
ORDER BY c.proveedor, mc.Nombre_material




















