# IFSC_RESTful_API

A REST service that can:
1. Given a bank branch IFSC code, get branch details.
2. Given a bank name and city, gets details of all branches of the bank in the city.

## API Guide

To get the branch details of the given IFSC code:
`http://manasvi.pythonanywhere.com/ifsc/"ifsc_code_without_double_quotes"`
> Example: http://manasvi.pythonanywhere.com/ifsc/ABHY0065002

To get the details of all the branches of a bank in a city:
`http://manasvi.pythonanywhere.com/branches/"bank_name_seperated_by_hyphen_without_double_quotes"/"city_name_without_double_quotes"`
> Example: http://manasvi.pythonanywhere.com/branches/axis-bank/ghaziabad

### Note:
The API also returns data in JSON by directly appending `.json` at the end of url.
> Example: http://manasvi.pythonanywhere.com/ifsc/ABHY0065002.json
