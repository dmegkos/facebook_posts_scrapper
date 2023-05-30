# Facebook Page Scraper (Python)

This application, written in Python, is designed to scrape posts from provided Facebook pages and export the results into an Excel file. The user interface is created using Tkinter, and data manipulation and storage are handled using Pandas. 

## Features

1. **Input**: The application accepts an Excel file containing Facebook page IDs. 
2. **Authentication (Optional)**: The app includes optional input fields for logging into a Facebook account. This enables access to pages that require likes. 
3. **Configurable Fetching Parameters**: Users can set the number of pages to scroll through and posts per scroll.
4. **Progress Tracking**: A progress bar shows the progress of the data fetching operation.
5. **Output**: The scraped data is sorted by likes, stored in a Pandas DataFrame, and subsequently exported into an Excel file.

## Files

1. **FFP.py**: The main application file, containing the Tkinter GUI code and the main application logic.
2. **get_fb_posts.py**: The engine file, handling the fetching of the Facebook posts.

## Installation & Usage

Make sure you have the following Python packages installed:

- pandas
- tkinter
- openpyxl
- facebook_scraper

If not, they can be installed using pip:

```bash
pip install pandas tkinter openpyxl facebook_scraper
```

## To use the application:

1. Clone the repository or download the zip file and extract it.
2. Navigate to the project directory.
3. Run the FFP.py script.

``` bash
python FFP.py
```

A GUI will pop up. Follow these steps:

- Load the input Excel file with Facebook page IDs.
- (Optional) Input your Facebook account username and password.
- Set the number of pages to scroll through and posts per scroll.
- Click the "Generate File" button to start the scraping process. A progress bar will indicate the status of the scraping operation.

The application will prompt you to choose a location to save the output Excel file containing the scraped data.

**Disclaimer:** Please use this tool responsibly and respect Facebook's terms and conditions.