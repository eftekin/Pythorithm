import os
import re
import tkinter as tk
from tkinter import Listbox, PhotoImage, messagebox

import matplotlib.pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup


class OlympicsMedalTracker:
    def __init__(self):
        """Initialize the main application window"""
        self.root = tk.Tk()
        self.root.title("Olympics Medal Tracker")
        self.root.geometry("600x700")
        self.root.minsize(width="400", height="700")
        self.root.maxsize(width="800", height="750")

        self.df = pd.DataFrame()
        self._setup_ui()

    def _setup_ui(self):
        """Set up the user interface components"""
        self._create_title()
        self._load_image()
        self._create_url_section()
        self._create_country_list()
        self._create_action_buttons()

    def _create_title(self):
        """Create the application title"""
        title_label = tk.Label(
            self.root, text="Olympics Medal Tracker", font=("Helvetica", 16, "bold")
        )
        title_label.pack(pady=10)

    def _load_image(self):
        """Load the Olympic rings image with error handling"""
        try:
            img_path = os.path.abspath("olympic_rings.png")
            if os.path.exists(img_path):
                img = PhotoImage(file=img_path)
                img_label = tk.Label(self.root, image=img)
                img_label.image = img
                img_label.pack(pady=5)
        except Exception as e:
            print(f"Image loading error: {e}")

    def _create_url_section(self):
        """Create URL input section"""
        tk.Label(self.root, text="Enter URL:").pack(pady=5)
        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.insert(0, "https://www.bbc.com/sport/olympics/paris-2024/medals")
        self.url_entry.pack(pady=5)

        tk.Button(self.root, text="Show List", command=self._fetch_and_display).pack(
            pady=5
        )

    def _create_country_list(self):
        """Create country listbox"""
        tk.Label(self.root, text="Click on a country to see detailed medals:").pack(
            pady=5
        )
        self.listbox = Listbox(self.root, height=10, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

    def _create_action_buttons(self):
        """Create action buttons for country chart and analytics"""
        tk.Button(
            self.root,
            text="Show Chart",
            command=self._show_country_chart,
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Show General Analytics",
            command=self._show_general_analytics,
        ).pack(pady=5)

    def _fetch_and_display(self):
        """Fetch and populate country list"""
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a URL.")
            return

        self.df = self._scrape_data(url)
        if not self.df.empty:
            self.listbox.delete(0, tk.END)
            self.df["Total"] = self.df[["Gold", "Silver", "Bronze"]].sum(axis=1)
            for country in self.df["Country"]:
                self.listbox.insert(tk.END, country)

    def _scrape_data(self, url):
        """Scrape Olympic medal data from the provided URL"""
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            table = soup.find("table")
            rows = table.find_all("tr")[1:]

            data = {"Country": [], "Gold": [], "Silver": [], "Bronze": []}

            for row in rows:
                cols = row.find_all("td")
                if len(cols) < 4:
                    continue

                country_span = cols[1].select_one("div div span:nth-of-type(2)")
                country = country_span.text.strip() if country_span else "Unknown"

                data["Country"].append(country)
                data["Gold"].append(self._clean_medal_count(cols[2]))
                data["Silver"].append(self._clean_medal_count(cols[3]))
                data["Bronze"].append(self._clean_medal_count(cols[4]))

            return pd.DataFrame(data)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to scrape data: {e}")
            return pd.DataFrame()

    def _clean_medal_count(self, column):
        """Clean and convert medal count to integer"""
        medal_str = re.sub(r"[^0-9]", "", column.text.strip())
        return int(medal_str) if medal_str.isdigit() else 0

    def _show_country_chart(self):
        """Display bar chart for a specific country's medals"""
        if self.df.empty:
            messagebox.showwarning("Warning", "Fetch data first")
            return

        selected_country = self.listbox.get(tk.ACTIVE)
        country_data = self.df[self.df["Country"] == selected_country]

        if country_data.empty:
            messagebox.showerror("Error", f"No data available for {selected_country}")
            return

        medals = ["Gold", "Silver", "Bronze"]
        counts = country_data[medals].iloc[0].values

        plt.figure(figsize=(8, 6))
        plt.bar(medals, counts, color=["gold", "silver", "#cd7f32"])
        plt.title(f"Medal Counts for {selected_country}")
        plt.xlabel("Medal Type")
        plt.ylabel("Count")
        plt.show()

    def _show_general_analytics(self):
        """Display comprehensive analytics for top 10 countries"""
        if self.df.empty:
            messagebox.showwarning("Warning", "Fetch data first")
            return

        top_10_df = self.df.nlargest(10, "Total")

        fig, axs = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle("Top 10 Countries Olympic Medal Analytics", fontsize=16)

        medal_types = ["Gold", "Silver", "Bronze"]
        pie_chart_axes = [axs[0, 0], axs[0, 1], axs[1, 0]]

        for medal, ax in zip(medal_types, pie_chart_axes):
            ax.pie(top_10_df[medal], labels=top_10_df["Country"], autopct="%1.1f%%")
            ax.set_title(f"{medal} Medal Distribution")

        # Line chart instead of bar chart
        axs[1, 1].plot(top_10_df["Country"], top_10_df["Total"], marker="o")
        axs[1, 1].set_title("Total Medals by Country")
        axs[1, 1].set_xlabel("Country")
        axs[1, 1].set_ylabel("Total Medals")
        axs[1, 1].tick_params(axis="x", rotation=45)
        axs[1, 1].grid(True, linestyle="--", alpha=0.7)

        plt.tight_layout()
        plt.show()

    def run(self):
        """Start the application main loop"""
        self.root.mainloop()


def main():
    """Create and run the Olympic Medal Tracker application"""
    app = OlympicsMedalTracker()
    app.run()


if __name__ == "__main__":
    main()
