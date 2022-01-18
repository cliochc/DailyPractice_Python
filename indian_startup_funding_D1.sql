-- Q1
SELECT AmountinUSD, CityLocation from indian_startup_funding
WHERE CityLocation = 'Bengaluru';

--Q2

SELECT * FROM indian_startup_funding
ORDER by StartupName DESC;

--Q3
SELECT AmountinUSD, CityLocation FROM indian_startup_funding
where CityLocation = 'Bengaluru'
and AmountinUSD > 380000 
ORDER by AmountinUSD DESC;

-- Q4
SELECT CityLocation from indian_startup_funding
where AmountinUSD>38000;

--Q5
SELECT CityLocation from indian_startup_funding
where AmountinUSD>38000
GROUP by CityLocation;

--Q6
SELECT StartupName from indian_startup_funding
WHERE AmountinUSD<38000;

--Q7
SELECT StartupName from indian_startup_funding
WHERE AmountinUSD<38000
ORDER by StartupName DESC;

--Q8
SELECT AmountinUSD, StartupName from indian_startup_funding
WHERE StartupName like 'A%'
GROUP by IndustryVertical
ORDER by AmountinUSD DESC;

--Q9
SELECT count (*)FROM indian_startup_funding
where IndustryVertical = 'Education';

--Q10
SELECT count (*)FROM indian_startup_funding
where IndustryVertical = 'E-Commerce';

--Q11
SELECT count(*) from indian_startup_funding
where IndustryVertical ='E-Commerce' and CityLocation = 'Bengaluru';