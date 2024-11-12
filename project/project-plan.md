# Project Plan

## Title
<!-- Title of my Project-->
Investigating Potential Racial Bias in Traffic Policing of US: An Evidence-Based Analysis

## Main Question

<!-- This is the question I want find answer based on the Data I have -->
1. Are there observable patterns in traffic stop occurrences and their outcomes based on the drivers' race?

## Description

<!-- A abstract of my project (max. 200 words. I will be answering why and how I attempt it.) -->
This project will explore potential racial patterns in traffic police behavior by analyzing traffic stops and their outcomes using data from [the Stanford Open Policing Project](https://openpolicing.stanford.edu/). By examining key factors such as stop location, driver demographics, reasons for stops and outcomes; this project aims to provide evidence based on real data regarding the equity of traffic policing practices. Given recent public discourse around racial profiling, this analysis will provide a data-driven understanding of this important topic. 

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: 
* Metadata URL: https://openpolicing.stanford.edu/data/
* Data URL:
    - New Hampshire: https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_nh_statewide_2020_04_01.csv.zip
    - Rhode Island: https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_ri_statewide_2020_04_01.csv.zip
    - Connecticut: https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_ct_hartford_2020_04_01.csv.zip
    - Vermont: https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_vt_statewide_2020_04_01.csv.zip
    - Massachusetts: https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_ma_statewide_2020_04_01.csv.zip
    - New Jersey: https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_nj_camden_2020_04_01.csv.zip
    - Maryland: https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_md_statewide_2020_04_01.csv.zip
    - Virginia: https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_va_statewide_2020_04_01.csv.zip
    - San Francisco: https://stacks.stanford.edu/file/druid:yg821jf8611/yg821jf8611_ca_san_francisco_2020_04_01.csv.zip

* Data Type: CSV (Inside a Zip folder)

These datasets contain traffic records from various U.S. locations, including New Hampshire, Rhode Island, Connecticut, Vermont, Massachusetts, New Jersey, Maryland, Pennsylvania, Virginia and San Francisco.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Concatenate Datasets from Multiple Locations [#1][i1]
2. Duplicate Column Handling [#2][i2]

[i1]: https://github.com/ThreeSwordAI/made-project-W24/issues/1
[i2]: https://github.com/ThreeSwordAI/made-project-W24/issues/2