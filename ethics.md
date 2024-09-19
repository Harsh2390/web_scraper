# Ethical Considerations of Web Scraping
Web scraping can be a powerful tool for gathering data from publicly available websites, but it comes with important ethical considerations. This document outlines the key ethical issues related to web scraping and how they have been addressed in this project.

- *Yahoo Finance Terms of Service*: This project scrapes publicly available financial data from Yahoo Finance. I have reviewed Yahoo Finance’s ToS to ensure that the scraping activities do not violate their policies. It is important for users to verify and comply with these ToS and avoid scraping if it goes against their rules.

- *Compliance with Data Privacy Laws*: The project only collects public data available on Yahoo Finance. No personal data or sensitive information is gathered, which mitigates risks of violating privacy laws like the General Data Protection Regulation (GDPR).

## Purpose of Data Collection
The main objective of this project is to gather publicly accessible financial data from Yahoo Finance for educational and research reasons. The retrieved data can be utilized to study market trends, assess stock performance, and formulate trading strategies. The project neither collects nor manipulates sensitive or personal information, nor is it utilized for commercial purposes.

## Data Sources and Respect for robots.txt
Web scraping can raise ethical concerns if done without respecting the rules established by websites. To ensure that this project adheres to ethical standards:

1. Respecting Site Policies: The project only scrapes data from websites that do not explicitly prohibit scraping in their Terms of Service (ToS). In particular, Yahoo Finance's ToS has been reviewed to ensure compliance.
2. robots.txt Compliance: The project respects the robots.txt file, a standard used by websites to instruct web crawlers which parts of the site should not be accessed or scraped. Before scraping any website, users are encouraged to check the robots.txt file (https://finance.yahoo.com/robots.txt) and avoid scraping content from restricted areas.

## Collection Practices
Ethical web scraping requires responsible data collection practices to avoid disrupting website operations or violating any protected content:

- No Bypassing Security: The project only collects data from publicly accessible web pages. It does not bypass login pages, paywalls, or any form of password protection. Sites that require authentication are off-limits for scraping, in accordance with their data access restrictions.

## Data Handling and Privacy
Data privacy is a critical aspect of ethical web scraping. This project is committed to safeguarding user privacy by ensuring that only non-personally identifiable information (non-PII) is collected:

- No Collection of Personal Data: This project strictly avoids scraping any data that could identify individual users, such as usernames, email addresses, or other personally identifiable information (PII).

- Secure Storage: Any scraped data is handled and stored securely. If any data is saved locally for further analysis, users are encouraged to ensure that sensitive information, if any, is not committed to version control systems. For example, users should add files containing scraped data to a `.gitignore` file to prevent accidental sharing or exposure on public platforms like GitHub.

## Data Usage
The data collected through this project is intended solely for educational and research purposes:

- Non-Commercial Use: This project is not intended for commercial exploitation. The collected data should be used to enhance understanding of financial markets, perform stock analysis, or create financial models for academic or research purposes. Redistributing or using the data for profit without permission from the data source is not permitted.