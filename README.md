**PROPERTY VALUE PREDICTION WITH ZILLOW DATASET**
Using various regression methods, the purpose of this study is to construct a predicting model using various features in real housing market.

**DATA COMPOSITION**
May 2017 - June 2017
Orange County, Los Angeles County, and Ventura County in California

**KEY OBJECTIVES**

- Visualize tax rate distribution in Orange County, Los Angeles County, and Ventura County in California

- General perception: Other than the physical locations of properties
  square footage, bedroom number, bathroom number are some driving factors for property value
> In this first machine learning model construction attempt, 
> the baseline model will only take **square footage, bedroom number, bathroom number** into consideration.

- Provide other models with better performance

**KEY TAKEAWAY**
- baseline model using sqft, total bed, total bath - $R^2$ 0.38

- improved model
> polynomial/linear regression
>
> Feature: bath, bed, sqft, garage sqft, year built
>
> $R^2$ train-set 0.48, test-set 0.46

For all the prediction modelS and requested tax rate distribution data
> check out "Zillow - detailed version.ipnb"

**NOTES ABOUT DATA**
Total data category/ column: 57

> 32 columns (56% of columns) presents > 70% missing data
>
> Dropped the columns with excessive amount of missing data
>
> Treat missing data: fill in median


**SETUP**
- env file should contain your database access key
- **please download all the .py file, especially wrangle.py and split_scale.py**





