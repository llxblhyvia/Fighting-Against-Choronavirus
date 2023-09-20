# Fighting Against Choronavirus

## Overview

Since the beginning of 2020, COVID-19 has spread wantonly around the world. Making the public aware of the typical symptoms after COVID-19 infection and the different characteristics of the virus infection among different populations will enable the public to prepare more fully to deal with it. Therefore, we have developed the **Fight Against Choronavirus** (**FAC**) data visualization webpage, which enables the public to have a clear and intuitive understanding of the symptoms of COVID-19 infection in an interactive way. This project is completely open source for all the data processing, visualization, and web development parts.
![main]()


## Data Analytics and Visualization

### Data

Downloaded from [Vaccine Adverse Event Reporting System (VAERS)](https://vaers.hhs.gov).[![VAERS Logo](https://vaers.hhs.gov/images/vaers-logo.png)](https://vaers.hhs.gov/index.html)

All data used are in [*VAERSDATA*](https://github.com/llxblhyvia/Fighting-Against-Choronavirus/tree/main/VAERSDATA).

### Code

The [code](https://github.com/llxblhyvia/Fighting-Against-Choronavirus/tree/main/FAC-CODE/FAC-data_visual) data processing and visualization part are divided to four parts : 

- a_b_foundamental_visual.ipynb for  foundamental visualization, corresponding to the first two pages of the main page
- c_wordcloud.ipynb for generating wordclouds of  adverse reactions under different conditions
- d-time.ipynb for adverse effects over time
- e-model.ipynb for Adverse effects of deceased patients and health advice for people.

### Dependencies

This code was confirmed to run with the following environment:

- Processed with Python 3.8
- pyecharts 0.5.11
- jupyter-notebook : 6.1.4

## Web Development

### How to Run

### Online mode

Open ❗️with **Safari** browser.

#### local mode of operation (LMO)

Download and open the whole [project](https://github.com/llxblhyvia/Fighting-Against-Choronavirus/tree/main/FAC-CODE/FAC-web_dev) with Pycharm, click the triangle symbol next to

```python
 `if __name__ == '__main__':` 
```

in `app.py` and open with **Safari** browser to get optimal effect. 

### Dependencies

This code was confirmed to run with the following environment:

- Python 3.8.5
- Flask 1.1.2.
