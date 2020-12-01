#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import os

def clear(): 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    else: 
        _ = os.system('clear') 

time.sleep(0.5)
print('================================================')
time.sleep(0.5)
print('===============Auth0 Configurator===============')
time.sleep(0.5)
print('===========v1_DPTE UPI - @l0wpassfilter=========')
time.sleep(0.5)
print('================================================')
time.sleep(0.5)
print()
print()

input('Press enter to continue...')
clear()


# In[2]:


time.sleep(0.5)
print('Make sure to put thingsboard.yml file in the same directory as this program')
input('Press enter to continue...')
print()
print()
time.sleep(0.5)
print('Finding thingsboard.yml file')
time.sleep(0.5)


# In[3]:


if(os.path.isfile('thingsboard.yml')):
    print('Found thingsboard.yml file')
    time.sleep(0.5)
    print('Original thingsboard.yml file backed up to thignsboard_raw.yml file')
    os.rename(r'thingsboard.yml',r'thingsboard_raw.yml')
    time.sleep(0.5)
    print('Backup complete..')
    time.sleep(0.5)
else:
    print('thingsboard.yml not found, please put your original thingsboard.yml file first and rerun this program')
    quit()


# In[4]:




file = open("thingsboard_raw.yml", "rt")
#read file contents to string
data = file.read()
#replace all occurrences of the required string


# In[5]:


#service Name

data = data.replace('default:', 'auth0:')


# In[6]:


#loginButtonLabel

old = 'loginButtonLabel: "${SECURITY_OAUTH2_DEFAULT_LOGIN_BUTTON_LABEL:Default}"'
new = 'loginButtonLabel: "${SECURITY_OAUTH2_DEFAULT_LOGIN_BUTTON_LABEL:Auth0}"'
data = data.replace(old, new)


# In[7]:


old = 'loginButtonIcon: "${SECURITY_OAUTH2_DEFAULT_LOGIN_BUTTON_ICON:}"'
new = 'loginButtonIcon: "${SECURITY_OAUTH2_DEFAULT_LOGIN_BUTTON_ICON:mdi:shield-account}"'
data = data.replace(old, new)


# In[8]:


#Client Name

clientName = input('Enter clientName: ')

old = 'clientName: "${SECURITY_OAUTH2_DEFAULT_CLIENT_NAME:ClientName}"'
new = 'clientName: "${SECURITY_OAUTH2_DEFAULT_CLIENT_NAME:'
new = new+clientName+'}"'

data = data.replace(old, new)


# In[9]:


#Client ID
clientId = input('Enter clientId: ')

old = 'clientId: "${SECURITY_OAUTH2_DEFAULT_CLIENT_ID:}"'
new = 'clientId: "${SECURITY_OAUTH2_DEFAULT_CLIENT_ID:'
new = new+clientId+'}"'

data = data.replace(old, new)


# In[10]:


#Client Secret
clientSecret = input('Enter clientSecret: ')

old = 'clientSecret: "${SECURITY_OAUTH2_DEFAULT_CLIENT_SECRET:}"'
new = 'clientSecret: "${SECURITY_OAUTH2_DEFAULT_CLIENT_SECRET:'
new = new+clientSecret+'}"'

data = data.replace(old, new)


# In[11]:


#Access Token URI
accessTokenUri = input('Enter accessTokenUri: ')

old = 'accessTokenUri: "${SECURITY_OAUTH2_DEFAULT_ACCESS_TOKEN_URI:}"'
new = 'accessTokenUri: "${SECURITY_OAUTH2_DEFAULT_ACCESS_TOKEN_URI:'
new = new+accessTokenUri+'}"'

data = data.replace(old, new)


# In[12]:


#UserScope

old = 'scope: "${SECURITY_OAUTH2_DEFAULT_SCOPE:}"'
new = 'scope: "${SECURITY_OAUTH2_DEFAULT_SCOPE:openid,email,profile}"'

data = data.replace(old, new)


# In[13]:


#Redirect URI Template

old = 'redirectUriTemplate: "${SECURITY_OAUTH2_DEFAULT_REDIRECT_URI_TEMPLATE:http://localhost:8080/login/oauth2/code/}"'


# In[14]:


#jwkSetUri
jwkSetUri = input('Enter jwkSetUri: ')

old = 'jwkSetUri: "${SECURITY_OAUTH2_DEFAULT_JWK_SET_URI:}"'
new = 'jwkSetUri: "${SECURITY_OAUTH2_DEFAULT_JWK_SET_URI:'
new = new+jwkSetUri+'}"'

data = data.replace(old, new)


# In[15]:


#authorizationGrantType

old = 'authorizationGrantType: "${SECURITY_OAUTH2_DEFAULT_AUTHORIZATION_GRANT_TYPE:authorization_code}"'


# In[16]:


#clientAuthenticationMethod

old = 'clientAuthenticationMethod: "${SECURITY_OAUTH2_DEFAULT_CLIENT_AUTHENTICATION_METHOD:post}" # basic or post'


# In[17]:


#userInfoUri

userInfoUri = input('Enter userInfoUri: ')

old = 'userInfoUri: "${SECURITY_OAUTH2_DEFAULT_USER_INFO_URI:}"'
new = 'userInfoUri: "${SECURITY_OAUTH2_DEFAULT_USER_INFO_URI:'
new = new+userInfoUri+'}"'

data = data.replace(old, new)


# In[18]:


#userNameAttributeName

old = 'userNameAttributeName: "${SECURITY_OAUTH2_DEFAULT_USER_NAME_ATTRIBUTE_NAME:email}"'


# In[19]:


#allowUserCreation
old = 'allowUserCreation: "${SECURITY_OAUTH2_DEFAULT_MAPPER_ALLOW_USER_CREATION:true}"'


# In[20]:


#activateUser

old = 'activateUser: "${SECURITY_OAUTH2_DEFAULT_MAPPER_ACTIVATE_USER:false}"'


# In[21]:


#Default Mapper Type

old = 'type: "${SECURITY_OAUTH2_DEFAULT_MAPPER_TYPE:basic}"'


# In[22]:


#emailAttributeKey

old = 'emailAttributeKey: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_EMAIL_ATTRIBUTE_KEY:email}"'


# In[23]:


#firstNameAttributeKey

old = 'firstNameAttributeKey: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_FIRST_NAME_ATTRIBUTE_KEY:}"'
new = 'firstNameAttributeKey: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_FIRST_NAME_ATTRIBUTE_KEY:email}"'

data = data.replace(old, new)


# In[24]:


#lastNameAttributeKey

old = 'lastNameAttributeKey: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_LAST_NAME_ATTRIBUTE_KEY:}"'


# In[25]:


#tenantNameStrategy

old = 'tenantNameStrategy: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_TENANT_NAME_STRATEGY:domain}"'
new = 'tenantNameStrategy: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_TENANT_NAME_STRATEGY:email}"'

data = data.replace(old, new)


# In[26]:


#tenantNamePattern

old = 'tenantNamePattern: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_TENANT_NAME_PATTERN:}"'
new = 'tenantNamePattern: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_TENANT_NAME_PATTERN:%{email}}"'

data = data.replace(old, new)


# In[27]:


#customerNamePattern

old = 'customerNamePattern: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_CUSTOMER_NAME_PATTERN:}"'


# In[28]:


#defaultDashboardName

old = 'defaultDashboardName: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_DEFAULT_DASHBOARD_NAME:}"'


# In[29]:


file.close()
print('================================================')
time.sleep(0.5)
print('Input Data Complete')
time.sleep(0.5)
print('Writing File to thingboard.yml')
file = open("thingsboard.yml", "wt")
#overrite the input file with the resulting data
file.write(data)
#close the file
file.close()

time.sleep(0.5)
print('Writing complete..')


# In[34]:


print('================================================')
time.sleep(0.5)
print('Please put generated thingsboard.yml file to thingsboard conf directory')
print('ex : etc/thingsboard/conf on ubuntu')
time.sleep(0.5)
print('And then restart thingsboard service || sudo service thingboard restart')
time.sleep(1)
print('================================================')
print('===============Have a Nice Day==================')
print('================================================')
print('exiting program..')

