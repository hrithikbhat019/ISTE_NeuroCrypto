
# coding: utf-8

# In[5]:


def symm_crypto_create(input_message, input_key):
 
  # Alice creates a ciphertext and a secret key from the input message
  Alice_out_ciphertext = model( 'Alice', input_message, input_key)
  
  # Bob takes the ciphertext along with the secret key to decrypt and generate the original message
  Bob_out_message      = model( 'Bob',   Alice_out_ciphertext, input_key)

  # Eve takes in just the ciphertext text and tries to decrpyt it without using key
  Eve_out_message      = model( 'Eve',   Alice_out_ciphertext)
  
  return Bob_out_message, Eve_out_message



# In[ ]:

`

