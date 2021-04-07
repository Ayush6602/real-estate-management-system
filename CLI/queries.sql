-- Q1
SELECT DISTINCT address
FROM property
WHERE rent BETWEEN 20000 AND 40000;
-- Q2
select contact_no,
	dl.name
from dealer dl,
	property_dealer prp_dl,
	property prp,
	description des,
	locality loc
where dl.username = prp_dl.d_username
	and prp.id = prp_dl.p_id
	and prp.id = des.id
	and prp.locality_id = loc.id
	and bedroom >= 2
	and rent < 10000
	and loc.name = 'G.S. Road';
-- Q3
with dealer_sale AS(
	SELECT SUM(price) s,
		dealer
	FROM transaction
	WHERE year(date) = 2021
	GROUP BY dealer
)
SELECT name
FROM dealer_sale
	JOIN dealer
WHERE dealer_sale.dealer = dealer.username
	AND s =(
		SELECT MAX(s)
		FROM dealer_sale
	);
-- Q4
SELECT name as locality_name,
	type,
	bedroom,
	bathroom,
	kitchen,
	hall,
	address,
	size,
	price
from locality,
	description,
	property
WHERE description.id = property.id
	and locality.id = property.locality_id
	and description.bedroom >= 2
	and description.status != 'sold';
-- Q5
SELECT *
FROM property
	NATURAL JOIN description
WHERE price = (
		SELECT MAX(price)
		FROM property
	)
	OR rent = (
		SELECT MAX(rent)
		FROM property
	);