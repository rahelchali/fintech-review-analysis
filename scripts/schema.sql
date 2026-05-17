-- Omega Consultancy: Relational Verification Queries --

-- 1. Review Counts Per Competitor
SELECT b.bank_name, COUNT(r.review_id) as total_scraped_reviews
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name;

-- 2. Performance Tracking: Average Rating Benchmarks
SELECT b.bank_name, ROUND(AVG(r.rating), 2) as average_star_rating
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name;

-- 3. Integrity Audit: Check for Null Constraints
SELECT 
    SUM(CASE WHEN review_id IS NULL THEN 1 ELSE 0 END) as missing_pks,
    SUM(CASE WHEN bank_id IS NULL THEN 1 ELSE 0 END) as missing_fks,
    SUM(CASE WHEN rating IS NULL THEN 1 ELSE 0 END) as missing_ratings
FROM reviews;