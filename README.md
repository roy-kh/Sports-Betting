# Welcome to NBA Sports Betting project repository! 🏀

**<h3>Overview</h3>**
NBA Sports Betting is a project focused on predicting NBA playoff outcomes through the application of machine learning techniques and data analysis. Our goal is to provide insights and predictions to enhance your sports betting experience. Our overall findings are summarized in the "NBA Betting_A QuantSC Project Overview.pdf" powerpoint.

**<h3>Key Features</h3>**
- Data Source: We have gathered data from the Basketball Reference website, covering team and player statistics spanning from 2002 to 2022. Data used can be found in basketball_ref_scraper, data and other_scrapers folders. 
- Predictive Models: We have developed and fine-tuned four models using Scikit-Learn and TensorFlow frameworks:
  - Linear Regression
  - kNN (k-Nearest Neighbors)
  - Random Forest Regressor
  - Neural Networks
- Betting Strategies: In addition to our models, we employ advanced betting strategies such as line shopping and the Kelly Criterion for optimization.

**<h3>Understanding the Repository</h3>**
- As previously mentioned, the data used can be found in basketball_ref_scraper, data and other_scrapers folders.
- basketball_ref_scraper_ preprocess.py and the models folder then preprocesses the imported data, preparing it for further analysis and modeling.
- initial_data_analysis.ipynb is where we conducted basic analysis of the data, familiarizing ourselves with the imported datasets and their variables.
- Finally, models.ipynb and jq_models.ipynb ran these models on different datasets, focusing on different variables while testing for the most accurate model.
- The resources folder includes PDFs which we had used to familiarize ourselves with the topic and investigate how to potentially approach the topic.

Requirements.txt: use the following to install the env:
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
