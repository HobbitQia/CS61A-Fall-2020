.read data.sql


CREATE TABLE average_prices AS
  SELECT category, avg(MSRP) as average_price
      from products
          group by category;


CREATE TABLE lowest_prices AS
  SELECT store, item, min(price)
      from inventory
          group by item;

CREATE TABLE best_deals AS
  SELECT name as best_deal, min(MSRP / rating)
      from products
          group by category;

CREATE TABLE shopping_list AS
  SELECT best_deal, store
      from best_deals, lowest_prices
          where best_deal = item;


CREATE TABLE total_bandwidth AS
  SELECT sum(b.Mbs) 
      from shopping_list as a, stores as b
          where a.store = b.store;

