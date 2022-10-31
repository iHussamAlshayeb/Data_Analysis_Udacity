#!/usr/bin/env python
# coding: utf-8

# 
# # Project: Investigate a Dataset (TMDB Dataset)
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# 
# #### Questions
# 
# <p>1-Which year has the highest release of movies?</p>
# <p>2-Which Month Released Highest Number Of Movies In All Of The Years?</p>
# <p>3-Top Movies based on features</p>

# In[1]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# ### General Properties

# In[2]:


# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.

df = pd.read_csv("tmdb-movies.csv")

df.info()


# In[3]:


#print the shape of the data rows and columns
df.shape


# In[4]:


#print 5 rows from the data
df.head(5)


# 
# ### Data Cleaning (Replace this with more specific notes!)

# In[5]:


#remove unwanted columns
labels = ['homepage', 'tagline', 'overview', 'keywords', 'production_companies']
df = df.drop(columns = labels)


# In[6]:


# Fixing 'release_date dtype()'
df['release_date'] = pd.to_datetime(df['release_date'])
df.info()


# In[7]:


#Finding missing values
df.isna().sum()


# In[8]:


#Removing missing values from 'cast' and 'genres'
df = df[df["cast"].isnull() != True]
df = df[df["genres"].isnull() != True]
df = df[df["imdb_id"].isnull() != True]
df = df[df["director"].isnull() != True]


# df.isna().sum()

# In[9]:


#finding duplicated values
df.duplicated().sum()


# In[10]:


#removing duplicated values
df.drop_duplicates(inplace = True)
df.duplicated().sum()


# In[11]:


#print the shape after doing the cleaning process
df.shape


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# 
# 

# ### Research Question 1 (Which year has the highest release of movies?)

# In[12]:


movies_per_year = df.groupby('release_year').count()['id']
print(movies_per_year)


# In[13]:


movies_per_year.plot(xticks = np.arange(1960,2016,5))
sns.set(rc={'figure.figsize':(14,5)})
plt.title("Years Vs Number of Movies", fontsize= 13)
plt.xlabel("Release Year", fontsize = 12)
plt.ylabel("Number Of Movies", fontsize = 12)
sns.set_style('whitegrid')


# <strong>After Seeing the plot and the output we can conclude that year 2014 year has the highest release of movies (700) followed by year 2013 (659) and year 2015 (629).</strong>

# ## Research Question 2 (Which Month Released Highest Number Of Movies In All Of The Years?)
# 

# In[14]:


released_movies = df['release_date'].dt.month.value_counts().sort_index()
print(released_movies)


# In[15]:


months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
released_movies = pd.DataFrame(released_movies)
released_movies['month'] = months
#change the column name of the new dataframe 'number_of_release'
released_movies.rename(columns = {'release_date':'number_of_release'},inplace=True)

released_movies.plot(x='month',kind='bar',fontsize = 11,figsize=(8,6))
#set the labels and titles of the plot.
plt.title('Months vs Number Of Movie Releases',fontsize = 15)
plt.xlabel('Month',fontsize = 13)
plt.ylabel('Number of movie releases',fontsize = 13)


# <strong>According to the plot we can conclude that there are higher number of release in september and october month.</strong>
# 
# 

# ### Research Question 3 (Top Movies based on features)

# #### Question #3.1: Top Movies based on their revenue
# 

# In[ ]:





# In[16]:


#Fetching different columns with 2 different ways of code
movies_and_revenue = df[["original_title", "revenue_adj"]]
movies_and_budget = df[['original_title','budget_adj']]
movies_and_popularity = df[['original_title','popularity']]
movies_and_votes= df[['original_title','vote_average']]



# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))

# Horizontal Bar Plot
ax.barh(movies_and_revenue.sort_values(by = "revenue_adj", ascending=False).head(10).original_title,
            movies_and_revenue.sort_values(by = "revenue_adj", ascending=False).head(10).revenue_adj)

def drawFig(title):
    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)


    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)

    # Add x, y gridlines
    ax.grid(visible = True, color ='grey', linestyle ='-.', linewidth = 0.5, alpha = 0.2)

    # Show top values
    ax.invert_yaxis()

    # Add annotation to bars
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,
                 str(round((i.get_width()), 2)),
                 fontsize = 10, fontweight ='bold',
                 color ='grey')

    # Add Plot Title
    ax.set_title(title,
                 loc ='left', )

    # Add Text watermark
    fig.text(0.9, 0.15, 'Hussam', fontsize = 12,
             color ='grey', ha ='right', va ='bottom',
             alpha = 0.7)

    # Show Plot
    plt.show()
    
drawFig("Top 10 movies based on their adjusted revenue")


# <strong>According to the table above, the top 5 movies from the given dataset based on their adjusted revenue are the followings; Avatar, Star Wars, Titanic, The Exorcist and Jaws.</strong>

# #### Question #3.2: Top Movies based on their  budget
# 

# In[17]:



# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))

# Horizontal Bar Plot
ax.barh(movies_and_budget.sort_values(by = "budget_adj", ascending=False).head(10).original_title,
        movies_and_budget.sort_values(by = "budget_adj", ascending=False).head(10).budget_adj)

drawFig("Top 10 movies based on their adjusted budget")


# <strong>According to the table above, the top 5 movies from the given dataset based on their adjusted budget are the followings; The Warrioi's Way, Pirates of the Caribbean. On Stranger Tides, Pirates of the Caribbean. At World's End, Superman Returns and Titanic.</strong>

# #### Question #3.3: Top Movies based on their popularity
# 

# In[18]:


# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))

# Horizontal Bar Plot
ax.barh(movies_and_popularity.sort_values(by = "popularity", ascending=False).head(10).original_title,
        movies_and_popularity.sort_values(by = "popularity", ascending=False).head(10).popularity)

drawFig("Top 10 movies based on their popularity")


# <strong>According to the table above, the top 5 movies from the given dataset based on their Popularity are the followings; Jurassic World, Mad Max: Fury Road, Interstellar, Gaurdians of the Galaxy and Insurgent.</strong>

# #### Question #3.4: Top Movies based on their average vote
# 

# In[19]:


# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))

# Horizontal Bar Plot
ax.barh(movies_and_votes.sort_values(by = "vote_average", ascending=False).head(10).original_title,
        movies_and_votes.sort_values(by = "vote_average", ascending=False).head(10).vote_average)

drawFig("Top 10 movies based on their vote average")


# <strong>According to the table above, the top 5 movies from the given dataset based on their Voting Average are the followings; The Story of Film: An Odyssey, Black Mirror: White Christmas, Pink Floyd: Pulse, The Art of Flight and A Personal journey with Martin scoursese Through American Movies.</strong>

# <a id='conclusions'></a>
# ## Conclusions
# 
# 

# <p>1- Year 2014 year has the highest release of movies (700) followed by year 2013 (659) and year 2015 (629).</p>
# <p>2- The higher number of release in september and october month.</p>
# <p>3- The top 5 movies from the given dataset based on their adjusted revenue are the followings; Avatar, Star Wars, Titanic, The Exorcist and Jaws.</p>
# <p>4- The top 5 movies from the given dataset based on their adjusted budget are the followings; The Warrioi's Way, Pirates of the Caribbean. On Stranger Tides, Pirates of the Caribbean. At World's End, Superman Returns and Titanic.</p>
# <p>5- The top 5 movies from the given dataset based on their Popularity are the followings; Jurassic World, Mad Max: Fury Road, Interstellar, Gaurdians of the Galaxy and Insurgent.</p>
# <p>6- The top 5 movies from the given dataset based on their Voting Average are the followings; The Story of Film: An Odyssey, Black Mirror: White Christmas, Pink Floyd: Pulse, The Art of Flight and A Personal journey with Martin scoursese Through American Movies.</p>
# 
# <strong>The limitations associated with the conclusions are:</strong><br>
# 
# There is a big limitation here, as can be seen from data processed above, around 52 % of budget data is zero !! which affects profit calculation greatly. Combined with zero revenue, around 65 % of profit is zero or wrongly calculated !!
