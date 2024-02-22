# Exchange Rate Microservice
This microservice performs an API request to get the current exchange rate between two currencies.
The exchange rates are obtained from exchangerate-api.com. The base currency value is multiplied by
the received exchange rate to convert it to the target currency value.

## Requesting Data
Data requests are made via the Python subprocess module to spawn the fetchExchangeRate function from the
parent program. The function takes two parameters, base_currency and target_currency, which are passed
through input pipes in the run() process. 

![image](https://github.com/demobetav2/361_microservice/assets/122329027/7161c9e1-3858-435b-9e6c-26fdfc268e45)

## Receiving Data
Data is received from the microservice via the Python subprocess stdout pipe. The function prints a string to 
stdout containing either an error message, or if successful, the exchange rate proceeded by "success." The string
should be split() and the 0 index checked for "success," and if found, access index 1 for the exchange rate.
Otherwise, an error message is returned for processing.

![image](https://github.com/demobetav2/361_microservice/assets/122329027/60a530f3-2c44-43fd-901e-a15e187529fc)

## UML Diagram
![image](https://github.com/demobetav2/361_microservice/assets/122329027/03c2214f-0233-411e-a085-017a36e47bdc)
