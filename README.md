# Рекомандательная система исполнителей

# Входные данные: 
Топ исполнителей пользователя в порядке от наимболее предпочитаемых к наименее через запятую. 

# Результат: 
Список рекомендуемых исполнителей в соответствии с заданным топом. 

# Датасет: 
Датасет состоит из id пользователя, id исполнителя и количества прослушшиваний данным пользователем этого исполнителя. Так же есть дополнительный словарь, состоящий из id исполнителя и наименования исполнителя. 

# Алгоритм: 
В существующий датасет добавляется новый пользователь со его топом исполниетелей, в зависимости от позиции исполнителя в топе присваивается колличество прослушиваний в порядке убывания: от большего к меньшему. Уже с новым пользователем составляется матрица похожести, в которой, благодаря случайным блужданиям составляется список рекомендаций. 

# Полученные результаты: 
Для оценки полученных результатов, я попросила воспользоваться системой рекомендаций 20 человек и спросила сколько исполнителей из предложенных им понравились. В качестве критерия оценки пользователь либо знал репертуар исполнителя и относил к понравилось/не понравилось без прослушивания, либо не знал, и я просила прослушать заглавные треки нескольких альбомов/синглов.  

На первой итерации я получила следующий резулультаты: 12 человек оценили 7 исполнителей из списка как понравившееся, остальные варьировались от 5 до 8. В среднем 68% рекомендуемых исполнителей были оценены как понравившееся. 

Для улучшения полученного результата я увиличила длину выдаваемого списка с 10 до 20, и поменяла подсчет прослушиваний, умножив каждый на 50, чтобы приблизить данные к средним среди других пользователей. В результате я получила более расширенный список исполнителей, смещенный к похожести на первых исполнителей в списке топа, заданного ранее пользователем. В итоге в среднем 80,5% рекомендуемых исполнителей были отмечены как понравившиеся. 

# Приложение: 
Статистика колличества прослушиванй среди пользователей ![image](https://github.com/abyzgareeva/ml/assets/61008851/ef315d28-deee-4f66-a36e-1e449fde479e)
