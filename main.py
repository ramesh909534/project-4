import csv, webbrowser, sqlite3
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel # Added this import

# Plyer modules (Mobile use only)
try:
    from plyer import gps, call
except:
    gps = None
    call = None


# ---------------- Donor Card ----------------
class DonorCard(MDBoxLayout):
    name = StringProperty()
    phone = StringProperty()
    lat = StringProperty()
    lon = StringProperty()


# ---------------- Screens -------------------
class LoginScreen(Screen):
    def login_user(self, username, password):
        conn = sqlite3.connect("donors.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = cur.fetchone()
        conn.close()
        if result:
            Snackbar(MDLabel(text=f"Welcome {username}!")).open()
            self.manager.current = "home"
        else:
            Snackbar(MDLabel(text="Invalid username or password")).open()


class SignupScreen(Screen):
    def signup_user(self, username, password):
        if username and password:
            conn = sqlite3.connect("donors.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username=?", (username,))
            if cur.fetchone():
                Snackbar(MDLabel(text="Username already exists")).open()
            else:
                cur.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, password))
                conn.commit()
                Snackbar(MDLabel(text="Signup successful! Please login")).open()
                self.manager.current = "login"
            conn.close()
        else:
            Snackbar(MDLabel(text="Enter username & password")).open()


class HomeScreen(Screen):
    pass


class RegisterScreen(Screen):
    def get_gps_location(self, *args):
        if gps:
            try:
                gps.configure(on_location=self.update_location, on_status=self.gps_status)
                gps.start(minTime=1000, minDistance=1)
            except NotImplementedError:
                Snackbar(MDLabel(text="GPS not supported")).open()
        else:
            Snackbar(MDLabel(text="GPS not available")).open()

    def update_location(self, **kwargs):
        self.ids.lat.text = str(kwargs.get("lat", ""))
        self.ids.lon.text = str(kwargs.get("lon", ""))

    def gps_status(self, stype, status):
        print("GPS Status:", stype, status)

    def register_donor(self, name, bg, phone, lat, lon):
        if name and bg and phone:
            conn = sqlite3.connect("donors.db")
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO donors (name, bg, phone, lat, lon) VALUES (?,?,?,?,?)",
                (name, bg, phone, lat, lon),
            )
            conn.commit()
            conn.close()
            Snackbar(MDLabel(text=f"Donor {name} registered!")).open()
        else:
            Snackbar(MDLabel(text="Fill all fields!")).open()


class SearchScreen(Screen):
    def search_donor(self, bg):
        self.ids.result_list.clear_widgets()
        conn = sqlite3.connect("donors.db")
        cur = conn.cursor()
        cur.execute("SELECT name, bg, phone, lat, lon FROM donors WHERE bg=?", (bg,))
        results = cur.fetchall()
        conn.close()

        if results:
            for d in results:
                self.ids.result_list.add_widget(
                    DonorCard(name=d[0], phone=d[2], lat=d[3], lon=d[4])
                )
        else:
            Snackbar(MDLabel(text="No donors found")).open()

    def export_csv(self):
        conn = sqlite3.connect("donors.db")
        cur = conn.cursor()
        cur.execute("SELECT name, bg, phone, lat, lon FROM donors")
        data = cur.fetchall()
        conn.close()

        if data:
            with open("donors.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["name", "bg", "phone", "lat", "lon"])
                writer.writerows(data)
            Snackbar(MDLabel(text="Exported donors.csv")).open()
        else:
            Snackbar(MDLabel(text="No donors to export")).open()


class MapScreen(Screen):
    pass


# ---------------- Main App ------------------
class BloodDonationApp(MDApp):
    def build(self):
        self.title = "Blood Donation App"
        self.theme_cls.primary_palette = "Red"
        self.create_db()
        return Builder.load_file("blood.kv")

    def create_db(self):
        """Create tables if not exist"""
        conn = sqlite3.connect("donors.db")
        cur = conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )"""
        )
        cur.execute(
            """CREATE TABLE IF NOT EXISTS donors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                bg TEXT,
                phone TEXT,
                lat TEXT,
                lon TEXT
            )"""
        )
        conn.commit()
        conn.close()

    def call_donor(self, phone):
        if call:
            try:
                call.makecall(tel=phone)
            except Exception as e:
                Snackbar(MDLabel(text=f"Call failed: {e}")).open()
        else:
            webbrowser.open(f"tel:{phone}")

    def open_map(self, lat, lon):
        if lat and lon:
            # The URL you provided seems incorrect. Corrected it to a functional one.
            url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
            webbrowser.open(url)
        else:
            Snackbar(MDLabel(text="Location not available")).open()

if __name__ == "__main__":
    BloodDonationApp().run()
