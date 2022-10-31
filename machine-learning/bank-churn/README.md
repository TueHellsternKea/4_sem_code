# Predicting Bank Customer Churn

![](https://miro.medium.com/max/4800/1*eKpMt4Qt6D8Lluk6NHzsew.png)

This is an exampel for solving classification problems with Python’s Scikit-learn library.

We will try to predict whether or not a bank customer will churn in the future, base on the data.

## Identify potential churn factors
- Credit Score
- Country
- Gender
- Age group
- Tenure
- Balance
- Number of products
- Has credit card
- Is active member
- Estimated Salary

## Potential churn factors?

### Country
![](https://miro.medium.com/max/494/1*PV6hJtV4T_wNhluhLw69iQ.png)

Country distribution on churners
It is seen that customer churn rates in Germany and France are 2 times higher than in Spain.

### Gender
![](https://miro.medium.com/max/490/1*7GAlg3scXemGOzpPFYbHQg.png)

As can be seen on the pie graph, the female churner rate is higher than the male churner rate.

### Number of product
![](https://miro.medium.com/max/640/1*GpEAps51jp6EgcdPAxf-lw.png)

The heat map indicates that the churned customer number decreases in all countries when the number of products increases.

### Credit Card
![](https://miro.medium.com/max/640/1*icEz-srQhsbpNwy5LTg9cQ.png)

Interestingly, churn decision among customers is higher even they have a credit card.

### Being an active member
![](https://miro.medium.com/max/640/1*8QbaFqjsWk83aE-khLM9Hw.png)

Churner number is lower among customers who are active members.

![](https://miro.medium.com/max/640/1*efcZNVOw1PRnJ6Xz1ttBKw.png)

The average age of churned customers who are not active members and don’t have a credit card is higher. The age range of customers having 1 product is very large. There is no non-churner even they have 4 products if they don’ have a credit card and are not active members.

![](https://miro.medium.com/max/640/1*dLdU8ze31IevLc0qROu5BA.png)

The average age of churned customers who are active members and have a credit card is highest if they have 4 products.

### Age Group
![](https://miro.medium.com/max/640/1*AfKr2x5qAVW2dEsekTyijA.png)

Customers, who are under age 25 & age 65 and older in Germany and France, tend to churn more with respect to balance and credit score.

![](https://miro.medium.com/max/640/1*ZqZlZeo7KsHRYTU8KlaSfA.png)

In addition, credit score, tenure, balance, and estimated salary don’t affect churn decision. Still, I would like to point on the balances in Germany where there is no zero balance in their account.

## Less Loyal Customers
- Germany & France
- Female
- NumOfProduct < 2
- Age 25-64
- Has Credit Card
- Student & retired customers in Germany & France

## More Loyal Customers
- Spain
- Male
- NumOfProduct >= 2
- Active member
- Student & retired customers in Spain

# Data
The data for this excampel are from [https://www.kaggle.com/datasets/hj5992/bank-churn-modelling](https://www.kaggle.com/datasets/hj5992/bank-churn-modelling)
