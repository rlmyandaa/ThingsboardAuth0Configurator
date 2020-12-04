#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[7]:


time.sleep(0.5)
print('Getting original thingsboard.yml file from')
print('/etc/thingsboard/conf/thingsboard.yml')
print()
print()
os.system('cp /etc/thingsboard/conf/thingsboard.yml .')


# In[ ]:


time.sleep(0.5)
print('Original thingsboard.yml file backed up to thignsboard_raw.yml file')
os.rename(r'thingsboard.yml',r'thingsboard_raw.yml')
time.sleep(0.5)
print('Backup complete..')
time.sleep(0.5)


# In[ ]:


file = open("thingsboard_raw.yml", "rt")
#read file contents to string
data = file.read()
#replace all occurrences of the required string


# In[ ]:


#service Name

data = data.replace('default:', 'auth0:')


# In[ ]:


#loginButtonLabel

old = 'loginButtonLabel: "${SECURITY_OAUTH2_DEFAULT_LOGIN_BUTTON_LABEL:Default}"'
new = 'loginButtonLabel: "${SECURITY_OAUTH2_DEFAULT_LOGIN_BUTTON_LABEL:Auth0}"'
data = data.replace(old, new)


# In[ ]:


old = 'loginButtonIcon: "${SECURITY_OAUTH2_DEFAULT_LOGIN_BUTTON_ICON:}"'
new = 'loginButtonIcon: "${SECURITY_OAUTH2_DEFAULT_LOGIN_BUTTON_ICON:mdi:shield-account}"'
data = data.replace(old, new)


# In[ ]:


#Client Name

clientName = input('Enter clientName: ')

old = 'clientName: "${SECURITY_OAUTH2_DEFAULT_CLIENT_NAME:ClientName}"'
new = 'clientName: "${SECURITY_OAUTH2_DEFAULT_CLIENT_NAME:'
new = new+clientName+'}"'

data = data.replace(old, new)


# In[ ]:


#Client ID
clientId = input('Enter clientId: ')

old = 'clientId: "${SECURITY_OAUTH2_DEFAULT_CLIENT_ID:}"'
new = 'clientId: "${SECURITY_OAUTH2_DEFAULT_CLIENT_ID:'
new = new+clientId+'}"'

data = data.replace(old, new)


# In[ ]:


#Client Secret
clientSecret = input('Enter clientSecret: ')

old = 'clientSecret: "${SECURITY_OAUTH2_DEFAULT_CLIENT_SECRET:}"'
new = 'clientSecret: "${SECURITY_OAUTH2_DEFAULT_CLIENT_SECRET:'
new = new+clientSecret+'}"'

data = data.replace(old, new)


# In[ ]:


#Access Token URI
accessTokenUri = input('Enter accessTokenUri: ')

old = 'accessTokenUri: "${SECURITY_OAUTH2_DEFAULT_ACCESS_TOKEN_URI:}"'
new = 'accessTokenUri: "${SECURITY_OAUTH2_DEFAULT_ACCESS_TOKEN_URI:'
new = new+accessTokenUri+'}"'

data = data.replace(old, new)


# In[ ]:


#UserScope

old = 'scope: "${SECURITY_OAUTH2_DEFAULT_SCOPE:}"'
new = 'scope: "${SECURITY_OAUTH2_DEFAULT_SCOPE:openid,email,profile}"'

data = data.replace(old, new)


# In[ ]:


#Redirect URI Template

old = 'redirectUriTemplate: "${SECURITY_OAUTH2_DEFAULT_REDIRECT_URI_TEMPLATE:http://localhost:8080/login/oauth2/code/}"'
new = 'redirectUriTemplate: "${SECURITY_OAUTH2_DEFAULT_REDIRECT_URI_TEMPLATE:http://127.0.0.1:8080/login/oauth2/code/}"'

data = data.replace(old, new)


# In[ ]:


#jwkSetUri
jwkSetUri = input('Enter jwkSetUri: ')

old = 'jwkSetUri: "${SECURITY_OAUTH2_DEFAULT_JWK_SET_URI:}"'
new = 'jwkSetUri: "${SECURITY_OAUTH2_DEFAULT_JWK_SET_URI:'
new = new+jwkSetUri+'}"'

data = data.replace(old, new)


# In[ ]:


#authorizationGrantType

old = 'authorizationGrantType: "${SECURITY_OAUTH2_DEFAULT_AUTHORIZATION_GRANT_TYPE:authorization_code}"'


# In[ ]:


#clientAuthenticationMethod

old = 'clientAuthenticationMethod: "${SECURITY_OAUTH2_DEFAULT_CLIENT_AUTHENTICATION_METHOD:post}" # basic or post'


# In[ ]:


#userInfoUri

userInfoUri = input('Enter userInfoUri: ')

old = 'userInfoUri: "${SECURITY_OAUTH2_DEFAULT_USER_INFO_URI:}"'
new = 'userInfoUri: "${SECURITY_OAUTH2_DEFAULT_USER_INFO_URI:'
new = new+userInfoUri+'}"'

data = data.replace(old, new)


# In[ ]:


#userNameAttributeName

old = 'userNameAttributeName: "${SECURITY_OAUTH2_DEFAULT_USER_NAME_ATTRIBUTE_NAME:email}"'


# In[ ]:


#allowUserCreation
old = 'allowUserCreation: "${SECURITY_OAUTH2_DEFAULT_MAPPER_ALLOW_USER_CREATION:true}"'


# In[ ]:


#activateUser

old = 'activateUser: "${SECURITY_OAUTH2_DEFAULT_MAPPER_ACTIVATE_USER:false}"'
new = 'activateUser: "${SECURITY_OAUTH2_DEFAULT_MAPPER_ACTIVATE_USER:true}"'

data = data.replace(old, new)


# In[ ]:


#Default Mapper Type

old = 'type: "${SECURITY_OAUTH2_DEFAULT_MAPPER_TYPE:basic}"'


# In[ ]:


#emailAttributeKey

old = 'emailAttributeKey: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_EMAIL_ATTRIBUTE_KEY:email}"'


# In[ ]:


#firstNameAttributeKey

old = 'firstNameAttributeKey: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_FIRST_NAME_ATTRIBUTE_KEY:}"'
new = 'firstNameAttributeKey: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_FIRST_NAME_ATTRIBUTE_KEY:given_name}"'

data = data.replace(old, new)


# In[ ]:


#lastNameAttributeKey

old = 'lastNameAttributeKey: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_LAST_NAME_ATTRIBUTE_KEY:}"'
new = 'lastNameAttributeKey: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_LAST_NAME_ATTRIBUTE_KEY:family_name}"'

data = data.replace(old, new)


# In[ ]:


#tenantNameStrategy

old = 'tenantNameStrategy: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_TENANT_NAME_STRATEGY:domain}"'
new = 'tenantNameStrategy: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_TENANT_NAME_STRATEGY:custom}"'

data = data.replace(old, new)


# In[ ]:


#tenantNamePattern

old = 'tenantNamePattern: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_TENANT_NAME_PATTERN:}"'
new = 'tenantNamePattern: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_TENANT_NAME_PATTERN:%{nickname}_%{given_name} %{family_name}}"'

data = data.replace(old, new)


# In[ ]:


#customerNamePattern

old = 'customerNamePattern: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_CUSTOMER_NAME_PATTERN:}"'


# In[ ]:


#defaultDashboardName

old = 'defaultDashboardName: "${SECURITY_OAUTH2_DEFAULT_MAPPER_BASIC_DEFAULT_DASHBOARD_NAME:}"'


# In[ ]:


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


# In[ ]:


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

