# Test_28.03.2025
Этот проект реализует автоматизированные тесты для проверки футеров на нескольких страницах веб-сайта https://only.digital/. Тесты написаны с использованием фреймворка Playwright , который позволяет эффективно взаимодействовать с элементами веб-страниц и записывать шаги выполнения тестов.

Тесты проверяют:

• Наличие всех ключевых элементов футера (тексты, кнопки, ссылки, изображения).
• Видимость элементов при прокрутке страницы.
• Корректность отображения футеров на пяти разных страницах сайта.

Альтернативные подход:
• Задачу можно было решить с использованием pytest в сочетании с Playwright.
• Также можно было создать отдельные автотесты для каждой страницы, так как футеры на них немного отличаются. В этом случае локаторы можно было бы написать через XPath , что обеспечило бы большую надежность.

Все шаги теста записываются в файл trace.zip. Для просмотра записи выполните команду:
playwright show-trace trace.zip
