<n2>Перевірка різних методів кластерізації</h2>
<img src="img/income clasification methods.jpg" alt="text">
<img src="img/health clasification methods.jpg" alt="text">
<img src="img/child_mort clasification methods.jpg" alt="text">
<p>За графіками кластерів наглядно видно що метод Dbscan не підходить, найкращими методами можно виявити спектральний метод та k-mean очікування-максимізації</p>
<p>Використовуючи метод очікування максимізації побудуємо всі наступні графіки з автоматичним виявилення кількость центрів</p>
<br>
<h2>Проводимо кореляцію даних для визначення цінних рис</h2>
<br>
<img src="img/feature_corr.png" alt="text">
<p>За даною кореляцію можна зазначити наступне:</p>
<ol>
  <li>Як і очіковалось <b>термін життя</b> сильно залежить від дитячою смертності, а також народжуванності дитини а також від дохіда</li>
  <li>Як і очікувалось теж саме стосується "продолородності"</li>
</ol>
Тож можно не звертати увагу на ці дані
<br>
<h2>Проводимо кластерізацію методом K-Means</h2>
<img src="img/gdpp_child_mort_clasification_features.jpg" alt="text">
Як можно побачити більш нужденні країни знаходиться в 0 кластері з великою смертністю дітей і нізькою Валовим внутрішнім продуктом
<img src="img/gdpp_health_clasification_features.jpg" alt="text">
Як можно побачити більш нужденні країни знаходиться в 1 кластері з низьким відсотком вкладенням коштів в здоров'є і нізькою Валовим внутрішнім продуктом
<img src="img/gdpp_imports_clasification_features.jpg" alt="text">
<br>
Після остаточної кластерізації всіх вказаних рис можно побачити зв'язок, 3 кластер відносить себе до стран яким треба допомогити
<img src="img/resulat_clustering.png" alt="text">
Країни 3-світу
<img src="img/urgent_need.png" alt="text">
Всі останні країни надані в результуючуми файлі
<h2>Висновок</h2>
<p>Протестуючи наші дані на різних методах кластерізації, можно знайти, один який найкраще підходить відконувши інші. Проведячи коряліцію можно знайти дані які сильно залежать від інших і тит самими відкинути їх. Провели аналіз даних. Вибраний метод використали для кластерізації 2 параметрів. Знайшли схожесть груп кластерів. Після декількох кластерізацій можно виділити групу стран яким потрібна допомога.</p>