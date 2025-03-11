# **🏀 NBA Player Playoff Similarity Finder**

**Author: Jeremy Serbée**

This Python project analyzes NBA playoff stats and determines the player whose playoff performance is most similar to a user-specified player. Using Euclidean distance on normalized data, it finds the closest statistical match based on a given season.

---

## **📌 Features**

* **Cleans and Processes NBA Playoff Data**: Reads raw stats from `playoffStats.csv` and converts them into structured objects.  
* **Player Normalization**: Ensures fair comparisons by normalizing numerical stats.  
* **Similarity Search**: Uses Euclidean distance to find the closest matching player based on playoff performance.  
* **Interactive CLI**: Users input a player's name and season to get a similarity result.

---

## **🛠️ Installation & Usage**

### **1️⃣ Clone the Repository**

bash  
CopyEdit  
`git clone https://github.com/yourusername/nba-playoff-similarity.git`  
`cd nba-playoff-similarity`

### **2️⃣ Install Dependencies**

Ensure you have Python installed (version 3.x). This project primarily uses built-in libraries (`csv` and `math`), so no additional packages are required.

### **3️⃣ Run the Script**

bash  
CopyEdit  
`python nba_data.py`

You'll be prompted to input a **player name** and **season**, and the script will return the player with the most similar playoff performance.

---

## **📂 Project Structure**

graphql  
CopyEdit  
`├── playoffStats.csv       # Dataset containing NBA playoff statistics`  
`├── nba_data.py            # Main script for user input & similarity search`  
`├── nba_driver.py          # Data processing, normalization, and distance calculation`  
`├── README.md              # Documentation`

### **📝 Code Breakdown**

#### **`nba_driver.py`**

* Reads `playoffStats.csv` and structures data into `Player` objects.  
* Converts attributes to the appropriate data types (int, float, string).  
* Implements **min-max normalization** for numerical stats.  
* Defines a function to compute **Euclidean distance** between players.

#### **`nba_data.py`**

* Loads and normalizes player data.  
* Asks for user input (player name & season).  
* Identifies the most similar playoff performance using **Euclidean distance**.  
* Returns the most statistically similar player.

---

## **📊 Example Output**

yaml  
CopyEdit  
`Choose a player: LeBron James`  
`Choose a season: 2012`

`Most similar playoff performance: Kawhi Leonard (2017)`  
`Euclidean Distance: 0.0421`

---

## **🔍 Future Improvements**

* Implement a web UI or API for easier interaction.  
* Allow users to compare **multiple** players at once.  
* Incorporate **dimensionality reduction (PCA)** for better performance.  
* Add more **advanced similarity metrics** (cosine similarity, Pearson correlation).

---

## **⚡ Contributing**

Feel free to submit pull requests or report issues\!

---

## **🏆 Credits**

* NBA data sourced from [Basketball-Reference](https://www.basketball-reference.com/).  
* Developed by Jeremy Serbée.

