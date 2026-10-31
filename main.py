
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns", None)   
pd.set_option("display.width", 150)          

class SalesDataAnalyzer:
    def __init__(self, file_path=None):
        self.data = None
        self.last_fig = None
        if file_path:
            self.load_data(file_path)

    def __del__(self):
        plt.close("all")

    # ---------- Load / Explore / Clean ----------
    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            if "Sale_Date" in self.data.columns:
                self.data["Sale_Date"] = pd.to_datetime(self.data["Sale_Date"])
                self.data["Year"] = self.data["Sale_Date"].dt.year
                self.data["Month"] = self.data["Sale_Date"].dt.month
            print("Dataset loaded successfully!")
        except FileNotFoundError:
            print("File not found:", file_path)
        except Exception as e:
            print("Error while loading file:", e)

    def explore_data(self, choice):
        if choice == 1:
            print(self.data.head())
        elif choice == 2:
            print(self.data.tail())
        elif choice == 3:
            print(list(self.data.columns))
        elif choice == 4:
            print(self.data.dtypes)
        elif choice == 5:
            self.data.info()
        else:
            print("Invalid choice!")

    def clean_data(self, choice, value=None):
        if choice == 1:
            missing = self.data[self.data.isnull().any(axis=1)]
            if missing.empty:
                print("No missing values found in the dataset!")
            else:
                print(missing)
        elif choice == 2:
            nums = self.data.select_dtypes(include=np.number).columns
            self.data[nums] = self.data[nums].fillna(self.data[nums].mean())
            print("Missing values filled with mean.")
        elif choice == 3:
            self.data = self.data.dropna()
            print("Rows with missing values dropped.")
        elif choice == 4:
            self.data = self.data.fillna(value)
            print("Missing values replaced with", value)
        else:
            print("Invalid choice!")

    # Numpy 
    def numpy_demo(self):
        arr = self.data["Sales_Amount"].to_numpy()
        print("Numpy array     :", arr[:10])
        print("First 5 elements:", arr[:5])
        print("Last 3 elements :", arr[-3:])
        print("Every 2nd item  :", arr[::2][:5])
        print("Sales x 2       :", (arr * 2)[:5])
        print("Sales + 100     :", (arr + 100)[:5])

    # Math / Combine / Split 
    def mathematical_operations(self):
        self.data["Profit"] = (self.data["Unit_Price"] - self.data["Unit_Cost"]) * self.data["Quantity_Sold"]
        self.data["Discounted_Sales"] = (self.data["Sales_Amount"] * (1 - self.data["Discount"])).round(2)
        print(self.data[["Sales_Amount", "Discount", "Discounted_Sales", "Profit"]].head())

    def combine_data(self, other_dataframe):
        combined = pd.concat([self.data, other_dataframe], ignore_index=True)
        print("Combined shape:", combined.shape)
        return combined

    def split_data(self, column="Region"):
        parts = {name: df for name, df in self.data.groupby(column)}
        for name, df in parts.items():
            print(f"{column} = {name} -> {len(df)} rows")
        return parts

    # Search / Sort / Filter 
    def search_sort_filter(self, choice):
        if choice == 1:
            cat = input("Enter product category to search (Food/Clothing/...): ")
            print(self.data[self.data["Product_Category"].str.contains(cat, case=False)].head(10))
        elif choice == 2:
            col = input("Sort by column (Sales_Amount/Quantity_Sold/Profit): ")
            print(self.data.sort_values(by=col, ascending=False).head(10))
        elif choice == 3:
            region = input("Enter region to filter (North/South/East/West): ")
            print(self.data[self.data["Region"].str.lower() == region.lower()].head(10))
        elif choice == 4:
            amount = float(input("Show sales greater than: "))
            print(self.data[self.data["Sales_Amount"] > amount].head(10))
        else:
            print("Invalid choice!")

    # Aggregate / Stats / Pivot 
    def aggregate_functions(self):
        print("Total Sales :", round(self.data["Sales_Amount"].sum(), 2))
        print("Mean Sales  :", round(self.data["Sales_Amount"].mean(), 2))
        print("Count       :", self.data["Sales_Amount"].count())
        print("\nRegion-wise Sales:")
        print(self.data.groupby("Region")["Sales_Amount"].agg(["sum", "mean", "count"]).round(2))

    def statistical_analysis(self):
        print(self.data.describe())
        print("\nStd Dev  :", round(self.data["Sales_Amount"].std(), 2))
        print("Variance :", round(self.data["Sales_Amount"].var(), 2))
        print("25th/50th/75th percentile:", self.data["Sales_Amount"].quantile([0.25, 0.5, 0.75]).tolist())

    def create_pivot_table(self):
        pivot = pd.pivot_table(self.data, values="Sales_Amount", index="Region",
                               columns="Product_Category", aggfunc="sum", fill_value=0).round(2)
        print(pivot)
        return pivot

    def advanced_operations(self):
        df = self.data.reset_index(drop=True)
        df["Region_Avg_Sales"] = df.groupby("Region")["Sales_Amount"].transform("mean").round(2)
        print(df[["Region", "Sales_Amount", "Region_Avg_Sales"]].head())

    # Visualization 
    def visualize_data(self, choice, x=None, y=None):
        fig, ax = plt.subplots(figsize=(8, 5))

        if choice == 1:      
            d = self.data.groupby(x)[y].sum()
            ax.bar(d.index.astype(str), d.values, label=y)
        elif choice == 2:    
            d = self.data.groupby(x)[y].sum()
            ax.plot(d.index.astype(str), d.values, marker="o", label=y)
        elif choice == 3:    
            ax.scatter(self.data[x], self.data[y], label=f"{x} vs {y}")
        elif choice == 4:    
            d = self.data.groupby(x)[y].sum()
            ax.pie(d.values, labels=d.index, autopct="%1.1f%%")
        elif choice == 5:    
            ax.hist(self.data[x], bins=10, edgecolor="black", label=x)
        elif choice == 6:   
            p = pd.pivot_table(self.data, values="Sales_Amount", index="Month",
                               columns="Region", aggfunc="sum", fill_value=0)
            ax.stackplot(p.index, p.T.values, labels=p.columns)
            x, y = "Month", "Sales_Amount"
        else:
            print("Invalid choice!")
            plt.close(fig)
            return

        name = {1: "bar plot", 2: "line plot", 3: "scatter plot",
                4: "pie chart", 5: "histogram", 6: "stack plot"}[choice]

        ax.set_title("Sales Visualization")
        if choice != 4:
            ax.set_xlabel(x)
            ax.set_ylabel(y if choice != 5 else "Frequency")
            ax.legend()
        self.last_fig = fig
        print(f"Generating {name}...")
        plt.show()
        print(f"{name.capitalize()} displayed successfully!")

    def save_plot(self, file_name):
        if self.last_fig is None:
            print("No plot to save. Create a visualization first.")
            return
        self.last_fig.savefig(file_name, dpi=150, bbox_inches="tight")
        print(f"Visualization saved as {file_name} successfully!")


# ---------- Optional: Inheritance + operator overloading ----------
class AdvancedSalesAnalyzer(SalesDataAnalyzer):
    def __init__(self, file_path=None):
        super().__init__(file_path)

    def __add__(self, other):                # operator overloading
        result = AdvancedSalesAnalyzer()
        result.data = pd.concat([self.data, other.data], ignore_index=True)
        return result


def show_menu():
    print("\n========== Data Analysis & Visualization Program ==========")
    print("Please select an option:")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    print("===========================================================")


def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return -1


def main():
    analyzer = AdvancedSalesAnalyzer()

    while True:
        show_menu()
        choice = get_int("\nEnter your choice: ")

        if choice == 1:
            print("\n== Load Dataset ==")
            path = input("Enter the path of the dataset (CSV file): ").strip()
            analyzer.load_data(path)
            continue

        if choice == 8:
            print("\nExiting the program. Goodbye!")
            break

        if choice not in range(1, 9):
            print("Invalid choice! Try again.")
            continue

        if analyzer.data is None:
            print("Please load the dataset first (option 1).")
            continue

        if choice == 2:
            print("\n== Explore Data ==")
            print("1. Display the first 5 rows\n2. Display the last 5 rows\n3. Display column names")
            print("4. Display data types\n5. Display basic info")
            analyzer.explore_data(get_int("Enter your choice: "))

        elif choice == 3:
            print("\n== DataFrame Operations ==")
            print("1. Numpy array demo (indexing/slicing)\n2. Mathematical operations")
            print("3. Combine data\n4. Split data\n5. Search / Sort / Filter")
            print("6. Aggregate functions\n7. Pivot table\n8. Advanced (groupby + transform)")
            sub = get_int("Enter your choice: ")
            if sub == 1:
                analyzer.numpy_demo()
            elif sub == 2:
                analyzer.mathematical_operations()
            elif sub == 3:
                analyzer.combine_data(analyzer.data.copy())
            elif sub == 4:
                analyzer.split_data(input("Split by column (Region/Product_Category/Sales_Channel): ") or "Region")
            elif sub == 5:
                print("1. Search category\n2. Sort\n3. Filter by region\n4. Filter by sales amount")
                analyzer.search_sort_filter(get_int("Enter your choice: "))
            elif sub == 6:
                analyzer.aggregate_functions()
            elif sub == 7:
                analyzer.create_pivot_table()
            elif sub == 8:
                analyzer.advanced_operations()
            else:
                print("Invalid choice!")

        elif choice == 4:
            print("\n== Handle Missing Data ==")
            print("1. Display rows with missing values\n2. Fill missing values with mean")
            print("3. Drop rows with missing values\n4. Replace missing values with a specific value")
            sub = get_int("Enter your choice: ")
            val = input("Enter value: ") if sub == 4 else None
            analyzer.clean_data(sub, val)

        elif choice == 5:
            print("\n== Descriptive Statistics ==")
            analyzer.statistical_analysis()

        elif choice == 6:
            print("\n== Data Visualization ==")
            print("1. Bar Plot\n2. Line Plot\n3. Scatter Plot\n4. Pie Chart")
            print("5. Histogram\n6. Stack Plot")
            sub = get_int("Enter your choice: ")
            names = {1: "Bar Plot", 2: "Line Plot", 3: "Scatter Plot",
                     4: "Pie Chart", 5: "Histogram", 6: "Stack Plot"}
            if sub not in names:
                print("Invalid choice!")
            else:
                print(f"\n== {names[sub]} ==")
                x = y = None
                if sub in (1, 2, 3, 4):
                    x = input("Enter x-axis column name: ")
                    y = input("Enter y-axis column name: ")
                elif sub == 5:
                    x = input("Enter column name: ")
                try:
                    analyzer.visualize_data(sub, x, y)
                except Exception as e:
                    print("Could not create plot:", e)

        elif choice == 7:
            print("\n== Save Visualization ==")
            name = input("Enter file name to save the plot (e.g., scatter_plot.png): ")
            analyzer.save_plot(name)


if __name__ == "__main__":
    main()