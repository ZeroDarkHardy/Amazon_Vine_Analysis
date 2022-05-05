# Amazon_Vine_Analysis

- [Project Overview](#project-overview)
    - [Resources](#resources)
- [ETL Process](#etl-process)
- [Results](#results)
- [Summary](#summary)

## Project Overview

The aim of this project is to analyze online reviews within the Amazon Vine program to determine whether a bias exists toward favorable reviews from paid subscribers.<br/>
<br/>
We used PySpark to build our ETL process and clean our dataset, which we then connected to an AWS RDS (PostgreSQL) instance to house our data.  We then used PgAdmin to design and interact with our PostgreSQL database, extracting data for later testing.<br/>
<br/>
The presented dataset contains US reviews for video games, but the ETL framework can be applied seamlessly to all Amazon Vine review datasets due to their shared schemata.
<br/>

## Resources
- Source Data: [Amazon - Video Game Reviews Dataset](https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Video_Games_v1_00.tsv.gz)<br/>
- Software/Languages: Google Colab, PostgreSQL 14, pgAdmin 4 v6.1, AWS (RDS), Python, PySpark 3.2.1

## ETL Process

Using Spark, we read our dataset from an AWS S3 bucket:<br/>
![load_dataset.png](https://github.com/ZeroDarkHardy/Amazon_Vine_Analysis/blob/main/images/load_dataset.png)<br/>
<br/>

Using pgAdmin (having been connected to the AWS RDS instance we created), we create our database using the following schema:<br/>
![schema.png](https://github.com/ZeroDarkHardy/Amazon_Vine_Analysis/blob/main/images/schema.png)<br/>
<br/>

We dataset was segmented to match the format of our schema:<br/>
![customers_table.png](https://github.com/ZeroDarkHardy/Amazon_Vine_Analysis/blob/main/images/customers_table.png)<br/>
![products_table.png](https://github.com/ZeroDarkHardy/Amazon_Vine_Analysis/blob/main/images/products_table.png)<br/>
![review_id_table.png](https://github.com/ZeroDarkHardy/Amazon_Vine_Analysis/blob/main/images/review_id_table.png)<br/>
![vine_table.png](https://github.com/ZeroDarkHardy/Amazon_Vine_Analysis/blob/main/images/vine_table.png)<br/>

...And then connected spark to our RDS instance:
![connect_rds.png](https://github.com/ZeroDarkHardy/Amazon_Vine_Analysis/blob/main/images/connect_rds.png)<br/>

## Results

Within Spark, we determined the average number of 5-Star reviews for both unpaid subcribers and paid Vine members.<br/>

### Unpaid customer reviews (Totals)
![unpaid_review_totals.png](https://github.com/ZeroDarkHardy/Amazon_Vine_Analysis/blob/main/images/unpaid_review_totals.png)

### Paid Vine member reviews (Totals)
![paid_review_totals.png](https://github.com/ZeroDarkHardy/Amazon_Vine_Analysis/blob/main/images/paid_review_totals.png)

### Comparing Averages
![unpaid_percentage.png](https://github.com/ZeroDarkHardy/Amazon_Vine_Analysis/blob/main/images/unpaid_percentage.png)
![paid_percentage.png](https://github.com/ZeroDarkHardy/Amazon_Vine_Analysis/blob/main/images/paid_percentage.png)

## Summary

We observe a significant difference in the occurance rate of 5-star reviews between the two demographics.  With 51.06% of paid Vine members voting 5-stars (and only 38.70% of unpaid users), there is a clear bias toward positive reviews among the paid membership.