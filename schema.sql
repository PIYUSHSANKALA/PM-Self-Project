CREATE TABLE users (
user_id INTEGER PRIMARY KEY, variant TEXT, device TEXT, channel TEXT, customer_segment TEXT,
ctr INTEGER, product_view INTEGER, add_to_cart INTEGER, checkout INTEGER, purchase INTEGER,
repeat_purchase INTEGER, engaged INTEGER, order_value REAL, repeat_order_value REAL, total_revenue REAL);
CREATE TABLE events (user_id INTEGER, variant TEXT, event_name TEXT);
