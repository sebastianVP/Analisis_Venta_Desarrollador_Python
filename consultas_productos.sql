-- CONSULTA: 3 PRODUCTOS MÁS VENDIDOS, Selecciona los productos con mayor cantidad total vendida
SELECT 
    producto,
    SUM(cantidad) AS total_vendida
FROM ventas
GROUP BY producto
ORDER BY total_vendida DESC
LIMIT 3;

