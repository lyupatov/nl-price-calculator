## Вопрос №1
...

## Вопрос №2
...

## Практическое задание
III. Написать один SQL-запрос, который возвращает 10 последних расчётов отсортированных по дате
""
SELECT 
   total_cost_rub
FROM calc_results
ORDER BY created_at desc
LIMIT 10;
""

#### Вызов API для получения результата:
URL: http://localhost:8000/costs_list
METHOD: GET

