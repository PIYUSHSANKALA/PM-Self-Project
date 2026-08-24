-- Experiment summary
SELECT variant, COUNT(*) users, ROUND(AVG(ctr)*100,2) ctr_pct,
ROUND(AVG(purchase)*100,2) conversion_pct, ROUND(AVG(repeat_purchase)*100,2) repeat_purchase_pct,
ROUND(AVG(engaged)*100,2) engagement_pct, ROUND(AVG(total_revenue),2) revenue_per_user
FROM users GROUP BY variant;

-- Funnel
SELECT variant, COUNT(*) users, ROUND(AVG(product_view)*100,2) view_pct,
ROUND(AVG(add_to_cart)*100,2) cart_pct, ROUND(AVG(checkout)*100,2) checkout_pct,
ROUND(AVG(purchase)*100,2) conversion_pct FROM users GROUP BY variant;

-- Segment analysis
SELECT variant, device, COUNT(*) users, ROUND(AVG(purchase)*100,2) conversion_pct
FROM users GROUP BY variant, device;
