# Stock Bot: Dynamic Stock Analysis and Visualization Tool  

Stock Bot is an interactive Python-based CLI tool designed to help users analyze stocks using `yfinance`. This tool allows users to specify stock screening criteria, analyze trends, and display information in a dynamic, visually enriched interface. 

---

## **Features**

### **Menu-Driven Interface**
- Provides an intuitive menu for users to configure and run the bot.
- Includes options for configuring global and independent settings, viewing logs, and accessing a detailed help menu.

### **Dynamic Settings**
- **Global Settings**: Apply common screening criteria to all stocks.
- **Independent Box Settings**: Customize screening criteria for specific stocks without affecting global settings.

### **Stock Visualization**
- Each stock is displayed in its own "box," with dynamic loading bars showing metrics such as:
  - **Last Close Price**
  - **Volume**
  - **Price Averages**
  - **Price Changes (%)**
  - And more!

### **Real-Time Updates**
- Stock data is updated at a user-defined refresh interval.
- Information for independent boxes updates separately from global settings.

### **Configuration Management**
- All settings and preferences are saved to a `config.json` file.
- Users can easily toggle and modify settings through the menu.

### **Help and Documentation**
- A detailed help menu guides users through bot setup and usage.
- Includes an overview of the tool, configuration steps, and how to analyze stocks effectively.

---

## **Installation**

### **Prerequisites**
- Python 3.7 or higher
- `yfinance` library  

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/unaveragetech/stock-bot.git
   cd stock-bot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the bot:
   ```bash
   python stock_bot.py
   ```

---

## **Usage**

### **Getting Started**
When you run `stock_bot.py`, you’ll be greeted with the **main menu**, where you can:
1. Configure **global settings** for all stocks.
2. Configure **independent settings** for specific stock boxes.
3. Run the bot to analyze stocks.
4. View details of the last run.
5. Access the help menu for more information.
6. Exit the tool.

### **Configuration Options**
- **Max Price**: Maximum stock price to include in the analysis.
- **Min Volume**: Minimum trade volume for filtering stocks.
- **Time Window**: The number of days to analyze stock trends.
- **Refresh Interval**: Time (in seconds) between data updates.

### **Example Workflow**
1. Run the bot:
   ```bash
   python stock_bot.py
   ```
2. From the menu, configure global settings (e.g., max price of $10, min volume of 100,000).
3. Add an independent box for `AAPL` with a unique configuration.
4. Run the bot and view stock data displayed in real-time.

---

## **Help Menu**

Access the help menu at any time for guidance. It provides:
- **Global Settings**: How to configure shared stock criteria.
- **Independent Box Settings**: Steps to customize individual stock boxes.
- **Running the Bot**: Instructions for running the analysis.
- **Last Run Details**: Viewing the results of the most recent analysis.
- **About `yfinance`**: Overview of the data source.

---

## **Configuration File**
The bot automatically generates a `config.json` file to store user preferences.  
### **Example `config.json`**:
```json
{
    "global_settings": {
        "max_price": 10.0,
        "min_volume": 100000,
        "time_window": 30,
        "refresh_interval": 10
    },
    "independent_boxes": {
        "AAPL": {
            "max_price": 150.0,
            "min_volume": 200000,
            "time_window": 10,
            "refresh_interval": 5
        }
    },
    "last_run": {
        "stocks_processed": ["AAPL", "MSFT"],
        "runtime": "2024-11-27 15:45:00"
    }
}
```

---

## **Technical Details**

### **Libraries Used**
- **`yfinance`**: Retrieves stock data from Yahoo Finance.
- **`rich`**: Creates visually enriched CLI elements, including tables, panels, and dynamic progress bars.
- **`json`**: Handles configuration file management.

---

## **Future Features**
- Additional stock indicators, such as PE ratio, market cap, and moving averages.
- Integration with other financial APIs for cross-verification.
- Enhanced visualizations, including charts and graphs.
- Support for exporting analysis reports to CSV or HTML.

---

## **Contributing**
Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.  

---

## **Contact**
For any questions or feedback, feel free to reach out via GitHub issues.  
