SELECT 
	thc_data.product_name,
	thc_data.productid,
	SUM(order_history.quantity) AS total_quantity_ordered,
	SUM(order_history.total_price) as total_revenue,
	thc_data.thca_percentage,
	thc_data.total_cbd,
	thc_data.cbga,
	thc_data.total_cbg,
	thc_data.delta_nine_thc
	
FROM 
	thc_data
INNER JOIN 
	order_history ON TRUE
CROSS JOIN LATERAL
	UNNEST(order_history.productid) AS order_productid(productid)
WHERE
	thc_data.productid = order_productid.productid
GROUP BY 
	thc_data.product_name,
	thc_data.productid;