# Test_28.03.2025
Этот проект реализует автоматизированные тесты для проверки футеров на нескольких страницах веб-сайта https://only.digital/. <br>
Тесты написаны с использованием фреймворка Playwright , который позволяет эффективно взаимодействовать с элементами веб-страниц и записывать шаги выполнения тестов.

## Тесты проверяют

• Наличие всех ключевых элементов футера (тексты, кнопки, ссылки, изображения).<br>
• Видимость элементов при прокрутке страницы.<br>
• Корректность отображения футеров на пяти разных страницах сайта.

## Альтернативные подходы

• Задачу можно решить с использованием pytest в сочетании с Playwright.<br>
• Также можно создать отдельные автотесты для каждой страницы, так как на некоторых страницах футеры отличаются. В этом случае локаторы можно написать через XPath, что обеспечило бы большую надежность.

Все шаги теста записываются в файл trace.zip. Для просмотра записи выполните команду:<br>
`playwright show-trace trace.zip`
