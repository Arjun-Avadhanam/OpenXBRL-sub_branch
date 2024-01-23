This repository is a small sub branch of a much bigger project titled OpenXBRL.In order to learn everything about the project OpenXBRL you may visit the link : https://github.com/Debarag/OpenXBRL

It was a collaborative effort along with Dr. Debarag Banerjee and Dr. Efraim Berkovich both of whom are listed as contributors in the repository.

This sub branch contains a small section of the code that had been implemented by me, a simple function to return the contents of any 10K/10Q file as a flat html.

I have also added a small helper function, load_url that is used to extract the contents of any url(that contains the iXBRL version of the 10K/10Q file) which can be passed as an argument to the main extraction function.

Please note that the function does require a specific url to be passed, however there are ways to obtain various files from different companies through narrowing down CIKS,company tickers,file formats etc that has been explore in the main repo(OpenXBRL)

The function generate_flat_html takes in the returned content of the url request as input and is able to generate a flat html of the report.I decided to save the file as an html for convenience, however any user can easily modify this based on their use case.

This repo aims to make the financial reports of the SEC easier to use as data. 
