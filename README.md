# Welcome to NBA Sports Betting project repository! 🏀

**<h3>Overview</h3>**
NBA Sports Betting is a project focused on predicting NBA playoff outcomes through the application of machine learning techniques and data analysis. Our goal is to provide insights and predictions to enhance your sports betting experience.

**<h3>Key Features</h3>**
- Data Source: We have gathered data from the Basketball Reference website, covering team and player statistics spanning from 2002 to 2022. Data used can be found in basketball_ref_scraper, data and other_scrapers folders. 
- Predictive Models: We have developed and fine-tuned three models (models.ipynb) using Scikit-Learn and TensorFlow frameworks:
  - kNN (k-Nearest Neighbors)
  - Random Forest Regressor
  - Neural Networks
- Betting Strategies: In addition to our models, we employ advanced betting strategies such as line shopping and the Kelly Criterion for optimization.

Requirements.txt: use the following to install the env:
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
