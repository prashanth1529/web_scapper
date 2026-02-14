-- Create a high-value summary table (Gold Layer)
CREATE OR REPLACE TABLE `market_data.daily_price_summary` AS
SELECT
  symbol,
  AVG(price) as avg_price,
  MAX(price) as peak_price,
  MIN(price) as floor_price,
  DATE(ingested_at) as trade_date
FROM
  `market_data.raw_prices`
GROUP BY
  1, 5;