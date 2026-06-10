class APIconfig:
    def __init__(self, api_ke, model="gpt-3.5-turbo", max_token=100):
        self.api_key = api_ke
        self.model = model
        self.max_token = max_token
        self.base_url = "https://api.openai.com/v1/"


dev_config = APIconfig("sk-dev-key", max_token=50)

prod_config = APIconfig("sk-prod-key", model= "gpt-4", max_token=100)

print(dev_config.api_key)
print(dev_config.model)
print(dev_config.max_token)
print(dev_config.base_url)
print(prod_config.api_key)
print(prod_config.model)
print(prod_config.max_token)
print(prod_config.base_url)
print("hello world")
print("hello world2")
print("hello world3")


        
      
        


    
