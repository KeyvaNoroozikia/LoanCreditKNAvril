#!/usr/bin/env python
# coding: utf-8

# # Application Streamlit via Google Colab:
# 
# On va mettre en place notre application et notre dashboard via Streamlit, sur lequel on va appliquer notre modèle LightGBM.
# 

# In[7]:


import sys
from IPython import get_ipython
get_ipython().magic(u'matplotlib inline')

# In[8]:


PATH =''


# In[9]:



import streamlit.components.v1 as components


# In[10]:


import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl


# ## Mise en place de l'application Streamlit : paramétrage
# 

# In[11]:





# In[12]:


get_ipython().run_cell_magic('writefile', 'app_bis.py', 'import pandas as pd\nimport pickle\nimport streamlit as st\nimport json\nimport requests \nimport numpy as np\n \nst.set_page_config(\n    page_title="Loan Prediction App by Keyvan NOROOZI KIA",\n\n)\n\nst.set_option(\'deprecation.showPyplotGlobalUse\', False)\n\n######################\n#main page layout\n######################\n\nst.title("Loan Default Prediction by Keyvan NOROOZI KIA")\nst.subheader("Are you sure your loan applicant is surely going to pay the loan back?💸 "\n                 "This machine learning app will help you to make a prediction to help you with your decision!")\n\ncol1, col2 = st.columns([1, 1])\n\n\nwith col2:\n    st.write("""To borrow money, credit analysis is performed. Credit analysis involves the measure to investigate\nthe probability of the applicant to pay back the loan on time and predict its default/ failure to pay back.\nThese challenges get more complicated as the count of applications increases that are reviewed by loan officers.\n\nBelow you will see the app prediction and the probability(as a number) that customer will repay his loan.\n\nIf the customer can repay his loan, you will see a green text with a positive result. \nIf the customer can\'t repay his loan, you will see a red text with a negative result.\n\n\n""")\n\nst.subheader("To predict default/ failure to pay back status, you need to follow the steps below:")\nst.markdown("""\n1. Enter/choose the parameters that best descibe your applicant on the left side bar;\n2. Press the "Predict" button and wait for the result.\n""")\n\nst.subheader("Below you could find prediction result: ")\n\n######################\n#sidebar layout\n######################\n\nst.sidebar.title("Loan Applicant Info")\n\nst.sidebar.write("Please choose parameters that descibe the applicant")\n\n#input features\ncontract = st.sidebar.slider("name contract type?:",min_value=0, max_value=1,step=1)\nchildren = st.sidebar.slider("How many children?:",min_value=1, max_value=10,step=1)\ncredit_amnt =st.sidebar.slider("Please choose Loan amount you would like to apply:",min_value=1000, max_value=400000,step=500)\nmembers = st.sidebar.slider(\'family members?\', min_value =1, max_value=10, step=1 )\ncredit_active =st.sidebar.slider("Credit Active? Yes : 1, No : 0 :",min_value=0, max_value=1,step=1)\namt_income_total =st.sidebar.slider("what is your income:",min_value=1000, max_value=400000,step=500)\nbureau =st.sidebar.slider("bureau year?:",min_value=1990, max_value=2022,step=1)\ndelay =st.sidebar.slider((\'how long (in days) was the delay between your payment and the payment date on your previous application ?\'),min_value=0, max_value=4000,step=1)\n\n\n\n\n\nuser_input_dict={"contract":contract, "children":children, "credit_amnt":credit_amnt, "members":members, "credit_active":credit_active,\n                "amt_income_total":amt_income_total,"delay":delay,"bureau":bureau}\n#user_input=pd.DataFrame(data=user_input_dict)\n\n\n\n\n\n\n\n#predict button\n\nbtn_predict = st.sidebar.button("Predict")\n\nif btn_predict:\n  res = requests.post(url=\'http://127.0.0.1:8070/Predict\',data = json.dumps(user_input_dict))\n  st.subheader(f"Response from API ={res.text}")\n \nif __name__==\'__main__\':\n  app_layout()')


# In[13]:


#streamlit run app.py


# ## Installation du tunnel local

# In[ ]:


#!npm install localtunnel


# ## Exécution de Streamlit sur colab
# 

# In[ ]:





# ## Mise en place du tunnel sur le port 8501
# Then just click in the `url` showed.
# 
# A `log.txt`file will be created.

# In[ ]:





# [![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y3VYYE)

# In[ ]:


X = 2
print(X)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




