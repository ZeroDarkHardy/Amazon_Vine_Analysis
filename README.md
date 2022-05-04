# Amazon_Vine_Analysis

## Project Overview

The aim of this project is to analyze online reviews within the Amazon Vine program to determine whether a bias exists toward favorable reviews from paid subscribers.<br/>
<br/>
We used PySpark to build our ETL process and clean our dataset, which we then connected to an AWS RDS (PostgreSQL) instance to house our data.  We then used PgAdmin to design and interact with our PostgreSQL database, extracting data for basic weighted testing.<br/>
<br/>
The presented dataset contains US reviews for video games, but the ETL framework can be seamlessly to all Amazon Vine review datasets due to their shared schemata.
<br/>

## Resources
- Source Data: [Amazon - Video Game Reviews Dataset](https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Video_Games_v1_00.tsv.gz)<br/>
- Software/Languages: Google Colab, PostgreSQL 14, pgAdmin 4 v6.1, AWS (RDS), Python, PySpark 3.2.1

## ETL Process

Using Spark, we read our dataset from an AWS S3 bucket:<br/>
![load_dataset.png](https://github.com/ZeroDarkHardy/Amazon_Vine_Analysis/blob/main/images/load_dataset.png)<br/>
