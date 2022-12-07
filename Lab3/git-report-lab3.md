### Data Analysis 
During the study of the given data frame, it was decided to reject the zero values of the price, to replace all numerical values with the average, and to process the string values separately.

![describe](img/describe.jpg)

<b>84.04%</b> Sedan is four doors.

* It was reasonable if missed data for the number of doors will be replace by four.

![describe](img/num_of_doors.jpg)

We exclude extreme data, the total number decreased to 180

![describe](img/result_description.png)

### Correlation

<p>After the correlation of the data, 20 features remained from the 26 presented, and the 3 most important features were also determined.</p>
<b>Features vs Price:</b>

* Symboling feature vs Price is 0.036, p-value is 0.6331842154850545<br>
* Normalized losses feature vs Price is 0.317, p-value is 1.4352759788069227e-05<br>
* Make feature vs Price is 0.005, p-value is 0.9465789197062073<br>
* Body style feature vs Price is 0.085, p-value is 0.25421650817357294<br>
* Drive wheels feature vs Price is 0.565, p-value is 1.5008084787375338e-16<br>
* Wheel base feature vs Price is 0.612, p-value is 7.210669291835463e-20<br>
* Length feature vs Price is 0.716, p-value is 1.3237649365440924e-29<br>
* Width feature vs Price is 0.745, p-value is 4.483940735629761e-33<br>
* Height feature vs Price is 0.187, p-value is 0.012055937204577285<br>
* Curb weight feature vs Price is 0.838, p-value is 1.3532161301065677e-48<br>
* Engine type feature vs Price is 0.053, p-value is 0.4819564774757745<br>
* Num of cylinders feature vs Price is 0.155, p-value is 0.03756021162069747<br>
* Engine size feature vs Price is 0.725, p-value is 1.1540207363299491e-30<br>
* Fuel system feature vs Price is 0.671, p-value is 7.219421668533878e-25<br>
* Compression ratio feature vs Price is 0.022, p-value is 0.766261136862567<br>
* Horsepower feature vs Price is 0.769, p-value is 2.0073201202419802e-36<br>
* Peak rpm feature vs Price is 0.046, p-value is 0.5410315199111934<br>
* City mpg feature vs Price is 0.714, p-value is 2.591260715545443e-29<br>
* Highway mpg feature vs Price is 0.699, p-value is 1.0327686400384447e-27

#### from the following features of the car, the most influential can be singled out:

* <b>Curb weight</b> feature vs Price is 0.838, p-value is 1.3532161301065677e-48<br>
* <b>Horsepower</b> feature vs Price is 0.769, p-value is 2.0073201202419802e-36<br>
* <b>Engine size</b> feature vs Price is 0.725, p-value is 1.1540207363299491e-30<br>
* City mpg feature vs Price is 0.714, p-value is 2.591260715545443e-29<br>
* Highway mpg feature vs Price is 0.699, p-value is 1.0327686400384447e-27<br>
* Fuel system feature vs Price is 0.671, p-value is 7.219421668533878e-25<br>

### Visualization

<p>general characteristics broken down by product manufacturer and body type</p>

| ![general characteristics](img/general_characteristics.jpg) |
|:--:|
|<b>Img.1 - general characteristics</b>|

<p>As can be seen from the graphs, the most expensive cars are Jaguar, Mercedes-Benz, Porsche and BMW<br>
The largest number of presented cars from the manufacturer toyota<br>
The most diverse styles of the car are represented by a hardtop and a convertible with a minimum price of 12 thousand and a maximum of about 30 thousand and more</p>

| ![linear regresssion models](img/linear_regression_model.jpg) |
|:--:|
|<b>Img.2 - linear reg characteristics</b>|

<p>The fuel consumption ratio in the city and outside the city increases, and the price decreases. The situation is reversed with the size of the engine, as the size increases, the price increases.</p>

| ![box-and-whisker plot model.jpg](img/box-and-whisker_plot_model.jpg) |
|:--:|
|<b>Img.3 - box-plot characteristics</b>|

* According to the chart above, rear-engine cars have an average price of 35,000, front-engined cars range in price from 8,000 to 30,000, and the median is around 10,000.<br> But there are a small number that fall outside their chart . the price varies from 30 thousand to more than 45 thousand.<br>
* The driving wheels of expensive cars are of the rwd type, the median number is about 17,000 and the larger number is concentrated from 14,000 to about 23,000.

| ![importences features](img/importences_features.jpg) |
|:--:|
|<b>Img.4 - Importences features using RandomForest</b>|

<p>Using powerful tree-based ML models (random forest), calculated importences featyres</p>

| ![linear regresssion models](img/output.png) |
|:--:|
|<b>Img.5 - Correalation features </b>|

<p>Correlation of the data that we marked as important was carried out</p>
